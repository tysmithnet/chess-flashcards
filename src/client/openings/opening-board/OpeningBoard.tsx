import {Key} from "chessground/types";
import * as React from "react";
import {Move as IMove} from "../../chess-api";
import {Board} from "../../common/board";

export interface IProps {
    moves: IMove[];
}

export interface IState {
    moveIndex: number;
}

export class OpeningBoard extends React.Component<IProps, IState> {
    private curMoves: IMove[];
    constructor(props: IProps) {
        super(props);
        this.state = {
            moveIndex: 0,
        };
        this.handleBackClick = this.handleBackClick.bind(this);
        this.handleForwardClick = this.handleForwardClick.bind(this);
        this.curMoves = this.props.moves;
    }

    public render() {
        const numMoves = this.props.moves.length;
        const hasNext = this.state.moveIndex < numMoves - 1;
        const hasPrevious = this.state.moveIndex > 0;
        const move = this.props.moves[Math.min(this.state.moveIndex, numMoves - 1)];
        const fen = move.fenAfter;
        const lastMove = [move.src, move.dst] as Key[];
        return (
            <div>
                <Board viewOnly={true} fen={fen} lastMove={lastMove} />
                <div>
                    <button disabled={!hasPrevious} onClick={this.handleBackClick}>back</button>
                    <button disabled={!hasNext} onClick={this.handleForwardClick}>forward</button>
                </div>
            </div>
        );
    }

    public componentDidUpdate() {
        if (this.props.moves !== this.curMoves) {
            this.curMoves = this.props.moves;
            this.setState({
                moveIndex: 0,
            });
        }
    }

    private handleBackClick() {
        this.setState({
            moveIndex: Math.max(this.state.moveIndex - 1, 0),
        });
    }

    private handleForwardClick() {
        this.setState({
            moveIndex: Math.min(this.state.moveIndex + 1, this.props.moves.length - 1),
        });
    }
}
