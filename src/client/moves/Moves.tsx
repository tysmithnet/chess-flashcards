import * as React from "react";
import { connect } from "react-redux";
import { Board } from "../board/Board";
import { IBaseProps, IMove, IRootState } from "../root";
import { randomMoveChallengeRequestFactory } from "./moves.action";
import {IRandomMoveChallenge } from "./moves.domain";
import "./moves.styles";

export interface IProps extends IBaseProps {
    challenge: IRandomMoveChallenge;
}

export interface IState {

}
export class Moves extends React.Component<IProps, IState> {
    constructor(props: IProps) {
        super(props);
    }

    public render() {
        if (this.props.challenge == null) {
            return <p>Loading...</p>;
        }
        return (
            <div className={"move-container"}>
                <div className="quiz-area">
                    <div>
                        <div className="title">TITLE</div>
                        <div className="board-area">
                            <Board position={this.props.challenge.position} legalMoves={this.props.challenge.moves} />
                        </div>
                    </div>
                </div>
            </div>
        );
    }

    public componentDidMount() {
        this.props.dispatch(randomMoveChallengeRequestFactory());
    }
}

function mapStateToProps(state: IRootState): IProps {
    return {
        challenge: state.moves.challenge,
    };
}

export const connectedComponent = connect(mapStateToProps)(Moves);
