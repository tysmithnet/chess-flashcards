import * as _ from "lodash";
import * as React from "react";
import { connect } from "react-redux";
import { Board } from "../board/Board";
import { applyMove, EMPTY_BOARD, IBaseProps, IMove, IOpening, IRootState, STARTING_POSITION } from "../root";
import { loadOpeningsRequestFactory } from "./openings.action";
import "./openings.styles";

export interface IProps extends IBaseProps {
    openings: IOpening[];
}

export interface IState {
    searchText: string;
    selectedOpenings: ISelectedOpening[];
    showDialog: boolean;
    current: ISelectedOpening;
    moveNum: number;
    position: string[];
    legalMoves: IMove[];
    backStack: ISelectedOpening[];
    isBlackPerspective: boolean;
}

export interface ISelectedOpening {
    eco: string;
    variant: IOpening;
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
            currentTitle = "CHANGE ME";
        }
        return (
            <div className="openings">
                <div className="quiz-area">
                    <div>
                        <h1 className="title" onClick={this.showDialog}>{currentTitle}</h1>
                        <div className="board-area">
                            <Board position={this.state.position} legalMoves={[]} onMove={this.handleMove} isBlackPerspective={this.state.isBlackPerspective} />
                        </div>
                    </div>
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
            <h3>presets</h3>
        );
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
        this.handleMove(curMove.src, curMove.dst);
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

    private handleMove(src: string, dst: string) {
        const copy = applyMove(this.state.position, {src, dst});
        this.setState({
            ...this.state,
            position: copy,
        });
    }

    private createDialog() {
        return <h1>DIALOG</h1>;
    }

    private showDialog() {
        this.setState({
            ...this.state,
            showDialog: true,
        });
    }

    private handleVariantSelected(event: React.ChangeEvent<HTMLInputElement>) {
        return;
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
