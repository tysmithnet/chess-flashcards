import * as _ from "lodash";
import * as React from "react";
import { connect } from "react-redux";
import { Board, EMPTY_BOARD, STARTING_POSITION } from "../board/Board";
import { Move, Opening, OpeningVariant } from "../chess-api";
import { fenToArray } from "../common/fen";
import { IBaseProps, IRootState } from "../root";
import { loadOpeningsRequestFactory } from "./openings.action";
import "./openings.styles";

export interface IProps extends IBaseProps {
    openings: Opening[];
}

export interface IState {
    searchText: string;
    selectedOpenings: ISelectedOpening[];
    showDialog: boolean;
    current: ISelectedOpening;
    moveNum: number;
    position: string[];
    legalMoves: Move[];
    backStack: ISelectedOpening[];
    isBlackPerspective: boolean;
}

export interface ISelectedOpening {
    eco: string;
    variant: OpeningVariant;
}

export interface IPreset {
    title: string;
    selectedOpenings: ISelectedOpening[];
}

export class Openings extends React.Component<IProps, IState> {
    constructor(props: IProps) {
        super(props);
        this.state = {
            searchText: "",
            selectedOpenings: [],
            showDialog: false,
            current: null,
            moveNum: null,
            position: EMPTY_BOARD,
            legalMoves: [],
            backStack: [],
            isBlackPerspective: false,
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
        this.handleRuyLopezPreset = this.handleRuyLopezPreset.bind(this);
    }

    public render() {
        if (!this.props.openings) {
            return <h3>Loading...</h3>;
        }
        let dialog = null;
        if (this.state.showDialog) {
            dialog = this.createDialog();
        }
        let currentTitle = "Select openings";

        if (this.state.current) {
            currentTitle = `${this.state.current.eco} - ${this.state.current.variant.name}`;
        }
        return (
            <div className="openings">
                <h1 className="title" onClick={this.showDialog}>{currentTitle}</h1>
                <div className="board-area">
                    <Board position={this.state.position} legalMoves={[]} onMove={this.handleMove} isBlackPerspective={this.state.isBlackPerspective}/>
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

    private createPresets() {
        if (this.props.openings == null) {
            return null;
        }
        return (
            <ul>
                <li key="Ruy Lopez" onClick={this.handleRuyLopezPreset}>Ruy Lopez</li>
            </ul>
        );
    }

    private handleRuyLopezPreset() {
        const openings = this.props.openings.filter(o => /C[6-9][0-9]/.test(o.id));
        const selected: ISelectedOpening[] = _.flatten(openings.map(o => o.variants.map(v => {
            return {
                eco: o.id,
                variant: v,
            };
        })));
        this.setState({
            ...this.state,
            current: selected[0],
            moveNum: 0,
            position: STARTING_POSITION,
            showDialog: false,
            selectedOpenings: selected,
            backStack: [selected[0]],
            legalMoves: [],
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
        }
    }

    private flipBoard() {
        this.setState({
            ...this.state,
            isBlackPerspective: !this.state.isBlackPerspective,
        });
    }

    private giveHint() {
        const curMove = this.state.current.variant.moves[this.state.moveNum];
        this.handleMove(curMove.src, curMove.dst, true);
    }

    private goNextOpening() {
        const ran = Math.floor(Math.random() * this.state.selectedOpenings.length);
        const current = this.state.selectedOpenings[ran];
        const position = STARTING_POSITION;
        const newBackStack = [...this.state.backStack, this.state.current];
        this.setState({
            ...this.state,
            current,
            position,
            legalMoves: null,
            moveNum: 0,
            backStack: newBackStack,
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
        const newCurrent = newBackStack[newBackStack.length - 1];
        this.setState({
            ...this.state,
            current: newCurrent,
            moveNum: 0,
            position: STARTING_POSITION,
            legalMoves: [],
            backStack: newBackStack,
        });
    }

    private handleMove(src: string, dst: string, pauseOnComplete = false) {
        // check the move against the current move number, if it matches, update the position and get new legal moves
        const expectedMove = this.state.current.variant.moves[this.state.moveNum];
        if (expectedMove.src === src && expectedMove.dst === dst) {
            console.log("CORRECT!");
            // apply move to position
            const nextPosition = fenToArray(expectedMove.fenAfter);
            // get legal moves for position
            // set current move++
            const nextMoveNum = this.state.moveNum + 1;

            if (nextMoveNum >= this.state.current.variant.moves.length) {
                if (!pauseOnComplete) {
                    return this.goNextOpening();
                } else {
                    setTimeout(this.goNextOpening, 1000);
                }
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
        const rows = this.props.openings.map((o, oi) => {
            const eco = o.id;
            const filtered = o.variants.filter(v => {
                return o.id.toLowerCase().indexOf(this.state.searchText.toLowerCase()) > -1
                    || v.name.toLowerCase().indexOf(this.state.searchText.toLowerCase()) > -1;
            });
            return filtered.map((v, vi) => {
                const isChecked = this.state.selectedOpenings.find(o2 => o2.eco === eco && o2.variant.name === v.name) != null;
                return (
                    <tr key={`${eco} - ${v.name} - ${vi}`}>
                        <td><input type="checkbox" data-eco={eco} data-name={v.name} checked={isChecked} onChange={this.handleVariantSelected} /></td>
                        <td>{eco}</td>
                        <td>{v.name}</td>
                    </tr>
                );
            });
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
        const eco = event.currentTarget.getAttribute("data-eco");
        const name = event.currentTarget.getAttribute("data-name");
        const opening = this.props.openings.find(o => o.id === eco);
        const variant = opening.variants.find(v => v.name === name);
        if (checked) {
            const newSelected = [...this.state.selectedOpenings];
            newSelected.push({
                eco,
                variant,
            });
            this.setState({
                ...this.state,
                selectedOpenings: newSelected,
            });
        } else {
            const newSelected = _.remove([...this.state.selectedOpenings], o => {
                return o.eco === eco && o.variant === variant;
            });
            this.setState({
                ...this.state,
                selectedOpenings: newSelected,
            });
        }
    }

    private hideDialog(selectedOpenings: ISelectedOpening[] = null) {
        if (selectedOpenings) {
            this.setState({
                ...this.state,
                selectedOpenings,
            });
        }

        if (this.state.current == null && this.state.selectedOpenings != null && this.state.selectedOpenings.length) {
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
