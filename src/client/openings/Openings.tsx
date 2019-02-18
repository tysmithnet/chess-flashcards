import * as Fuse from "fuse.js";
import * as _ from "lodash";
import * as React from "react";
import { connect } from "react-redux";
import { Board } from "../board/Board";
import { fenToArray } from "../common/fen";
import { applyMove, EMPTY_BOARD, IBaseProps, IMove, IOpening, IRootState, STARTING_POSITION } from "../root";
import { loadOpeningsRequestFactory } from "./openings.action";
import {PRESETS} from "./openings.presets";
import "./openings.styles";

export interface IProps extends IBaseProps {
    openings: IOpening[];
}

export interface IState {
    openings: Map<string, IOpening>;
    searchText: string;
    selectedOpenings: Set<string>;
    showDialog: boolean;
    current: IOpening;
    moveNum: number;
    position: string[];
    legalMoves: IMove[];
    backStack: string[];
    isBlackPerspective: boolean;
    isBackOfCard: boolean;
}

export class Openings extends React.Component<IProps, IState> {

    constructor(props: IProps) {
        super(props);
        this.state = {
            openings: (props.openings || []).reduce((m, c) => {
                m.set(c.id, c);
                return m;
            }, new Map<string, IOpening>()),
            searchText: "",
            selectedOpenings: new Set<string>(),
            showDialog: false,
            current: null,
            moveNum: null,
            position: EMPTY_BOARD,
            legalMoves: [],
            backStack: [],
            isBlackPerspective: false,
            isBackOfCard: true,
        };
        this.handleSearchTextChange = this.handleSearchTextChange.bind(this);
        this.showDialog = this.showDialog.bind(this);
        this.hideDialog = this.hideDialog.bind(this);
        this.handleMove = this.handleMove.bind(this);
        this.goBackOpening = this.goBackOpening.bind(this);
        this.goNextOpening = this.goNextOpening.bind(this);
        this.handleKeyUp = this.handleKeyUp.bind(this);
        this.redoCurrentOpening = this.redoCurrentOpening.bind(this);
        this.handleVariantSelected = this.handleVariantSelected.bind(this);
        this.handlePresetSelected = this.handlePresetSelected.bind(this);
        this.handleMouseWheelOverBoard = this.handleMouseWheelOverBoard.bind(this);
    }

    public componentDidUpdate(prevProps: IProps) {
        if (prevProps.openings !== this.props.openings) {
            this.setState({
                ...this.state,
                openings: this.props.openings.reduce((m, c) => {
                    m.set(c.id, c);
                    return m;
                }, new Map<string, IOpening>()),
            });
        }
    }

    public render() {
        if (!this.props.openings) {
            return <h3>Loading...</h3>;
        }
        let dialog = null;
        if (this.state.showDialog) {
            dialog = this.createDialog();
        }

        let body = this.createDemonstrateQuiz();
        if (this.state.isBackOfCard) {
            body = this.createRecognizeQuiz();
        }

        return (
            <div className="openings">
                <div className="quiz-area">
                    {body}
                </div>
                {dialog}
            </div>
        );
    }

    public componentDidMount() {
        this.props.dispatch(loadOpeningsRequestFactory());
        document.addEventListener("keyup", this.handleKeyUp);
    }

    public componentWillUnmount() {
        document.removeEventListener("keyup", this.handleKeyUp);
    }

    private createRecognizeQuiz() {
        const currentTitle = "Select openings";
        return (
            <div>
                <h1 className="title" onClick={this.showDialog}>{currentTitle}</h1>
                <div className="board-area" onWheel={this.handleMouseWheelOverBoard}>
                    <Board position={this.state.position} legalMoves={[]} onMove={this.handleMove} isBlackPerspective={this.state.isBlackPerspective} />
                </div>
            </div>
        );
    }

    private handleMouseWheelOverBoard(event: React.WheelEvent<HTMLDivElement>) {
        const isNextMove = event.deltaY < 0;
        let nextIndex = Math.min(this.state.moveNum + 1, this.state.current.moves.length - 1);
        if (!isNextMove) {
            nextIndex = Math.max(this.state.moveNum - 1, 0);
        }
        let position = STARTING_POSITION;
        for (let i = 0; i < nextIndex; i++) {
            position = applyMove(position, this.state.current.moves[i]);
        }
        this.setState({
            ...this.state,
            position,
            moveNum: nextIndex,
        });
    }

    private createDemonstrateQuiz() {
        let currentTitle = "Select openings";

        if (this.state.current) {
            currentTitle = `${this.state.current.ecoId} - ${this.state.current.variantName}`;
        }
        return (
            <div>
                <h1 className="title" onClick={this.showDialog}>{currentTitle}</h1>
                <div className="board-area">
                    <Board position={this.state.position} legalMoves={[]} onMove={this.handleMove} isBlackPerspective={this.state.isBlackPerspective} />
                </div>
            </div>
        );
    }

    private createPresets() {
        if (this.props.openings == null) {
            return null;
        }
        const items = PRESETS.map(p => {
            return (
                <li key={p.title} data-title={p.title} onClick={this.handlePresetSelected}>{p.title}</li>
            );
        });
        return (
            <ul>
                {items}
            </ul>
        );
    }

    private handlePresetSelected(event: React.MouseEvent<HTMLLIElement>) {
        const title = event.currentTarget.getAttribute("data-title");
        const preset = PRESETS.find(p => p.title === title);
        const openings = preset.getSelectedOpenings(this.props.openings);
        this.setState({
            ...this.state,
            selectedOpenings: new Set(openings),
        });
    }

    private handleKeyUp(event: KeyboardEvent) {
        if (event.code === "Escape") {
            return this.hideDialog();
        } else if (event.code === "Space" && !this.state.showDialog) {
            return this.goNextOpening();
        } else if (event.code === "KeyR" && !this.state.showDialog) {
            return this.redoCurrentOpening();
        } else if (event.code === "KeyB" && !this.state.showDialog) {
            return this.goBackOpening();
        } else if (event.code === "KeyH" && !this.state.showDialog) {
            return this.giveHint();
        } else if (event.code === "KeyF" && !this.state.showDialog) {
            return this.flipBoard();
        } else if (event.code === "KeyM" && !this.state.showDialog) {
            return this.flipMode();
        }
    }

    private flipMode() {
        this.setState({
            ...this.state,
            isBackOfCard: !this.state.isBackOfCard,
        });
    }

    private flipBoard() {
        this.setState({
            ...this.state,
            isBlackPerspective: !this.state.isBlackPerspective,
        });
    }

    private giveHint() {
        const curMove = this.state.current.moves[this.state.moveNum];
        this.handleMove(curMove.src, curMove.dst);
    }

    private goNextOpening() {
        const ran = Math.floor(Math.random() * this.state.selectedOpenings.size);
        const id = Array.from(this.state.selectedOpenings.keys())[ran];
        const selected: IOpening = this.state.openings.get(id);
        const newBackStack = [...this.state.backStack, id];
        this.setState({
            ...this.state,
            current: selected,
            backStack: newBackStack,
            moveNum: 0,
            position: STARTING_POSITION,
        });
    }

    private redoCurrentOpening() {
        this.setState({
            ...this.state,
            position: STARTING_POSITION,
            moveNum: 0,
        });
    }

    private goBackOpening() {
        const newBackStack = [...this.state.backStack];
        if (newBackStack.length < 2) {
            return;
        }
        newBackStack.pop();
        const lastId = _.last(newBackStack);
        this.setState({
            ...this.state,
            current: this.state.openings.get(lastId),
            moveNum: 0,
            position: STARTING_POSITION,
            legalMoves: [],
            backStack: newBackStack,
        });
    }

    private handleMove(src: string, dst: string) {
        // check the move against the current move number, if it matches, update the position and get new legal moves
        const expectedMove = this.state.current.moves[this.state.moveNum];
        if (expectedMove.src === src && expectedMove.dst === dst) {
            console.log("CORRECT!");
            // apply move to position
            const nextPosition = applyMove(this.state.position, {src, dst});
            // get legal moves for position
            // set current move++
            const nextMoveNum = this.state.moveNum + 1;

            if (nextMoveNum >= this.state.current.moves.length) {
                setTimeout(this.goNextOpening, 1000);
            }

            this.setState({
                ...this.state,
                legalMoves: [],
                position: nextPosition,
                moveNum: nextMoveNum,
            });
        } else {
            console.log("INCORRECT!");
            this.setState({
                ...this.state,
            });
        }
    }

    private createDialog() {
        const rows: JSX.Element[] = [];
        const fuse = new Fuse(Array.from(this.state.openings.values()), {
            keys: ["variantName", "moveText", "ecoId"],
            threshold: 0.1,
        });
        const matches = fuse.search(this.state.searchText);
        this.state.openings.forEach((v, k) => {
            if (matches.indexOf(v) === -1 && this.state.searchText.length) {
                return;
            }
            const isChecked = this.state.selectedOpenings.has(k);
            rows.push((
                <tr key={v.id}>
                    <td><input type="checkbox" data-id={v.id} checked={isChecked} onChange={this.handleVariantSelected} /></td>
                    <td>{v.ecoId}</td>
                    <td>{v.variantName}</td>
                </tr>
            ));
        });
        const flattened = _.flatten(rows);
        return (
            <div className="selection-dialog">
                <div className="table-container">
                    <input className="search-bar" value={this.state.searchText} onChange={this.handleSearchTextChange} />
                    <table>
                        <thead>
                            <tr>
                                <th />
                                <th>ECO</th>
                                <th>Name</th>
                            </tr>
                        </thead>
                        <tbody>
                            {flattened}
                        </tbody>
                    </table>
                </div>
                <div className="preset-container">
                    {this.createPresets()}
                </div>
            </div>
        );
    }

    private showDialog() {
        this.setState({
            ...this.state,
            showDialog: true,
        });
    }

    private handleVariantSelected(event: React.ChangeEvent<HTMLInputElement>) {
        const checked = event.currentTarget.checked;
        const copy = new Set(this.state.selectedOpenings);
        const id = event.currentTarget.getAttribute("data-id");
        if (checked) {
            copy.add(id);
        } else {
            copy.delete(id);
        }
        this.setState({
            ...this.state,
            selectedOpenings: copy,
        });
    }

    private hideDialog() {
        if (this.state.current == null && this.state.selectedOpenings != null && this.state.selectedOpenings.size) {
            this.goNextOpening();
        }
        this.setState({
            ...this.state,
            showDialog: false,
        });
    }

    private handleSearchTextChange(event: React.ChangeEvent<HTMLInputElement>) {
        const text = event.currentTarget.value;
        this.setState({
            ...this.state,
            searchText: text,
        });
    }
}

function mapStateToProps(state: IRootState): IProps {
    return {
        openings: state.openings.openings,
    };
}

export const connectedComponent = connect(mapStateToProps)(Openings);
