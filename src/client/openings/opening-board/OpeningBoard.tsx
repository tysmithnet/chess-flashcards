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
    constructor(props: IProps) {
        super(props);
        this.state = {
            moveIndex: -1,
        };
        this.handleBackClick = this.handleBackClick.bind(this);
        this.handleForwardClick = this.handleForwardClick.bind(this);
    }

    public render() {
        if (this.state.moveIndex < 0) {
            return (
                <div>
                    <Board viewOnly={true} />
                    <div>
                        <button onClick={this.handleBackClick}>back</button>
                        <button onClick={this.handleForwardClick}>forward</button>
                    </div>
                </div>
            );
        }
        const lastMove = this.props.moves[Math.min(this.props.moves.length - 1, this.state.moveIndex)];
        const converted = [lastMove.src as Key, lastMove.dst as Key];
        return (
            <div>
                <Board viewOnly={true} lastMove={converted} fen={lastMove.fenAfter}/>
                <div>
                    <button onClick={this.handleBackClick}>back</button>
                    <button onClick={this.handleForwardClick}>forward</button>
                </div>
            </div>
        );
    }

    private handleBackClick() {
        this.setState({
            moveIndex: this.state.moveIndex - 1,
        });
    }

    private handleForwardClick() {
        this.setState({
            moveIndex: this.state.moveIndex + 1,
        });
    }
}
