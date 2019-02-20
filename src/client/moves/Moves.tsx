import * as React from "react";
import { connect } from "react-redux";
import { Board } from "../board/Board";
import { IBaseProps, IMove } from "../root";
import { randomMoveChallengeRequestFactory } from "./moves.action";
import {IRandomMoveChallenge, IRootState} from "./moves.domain";

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
            <div>
                <Board position={this.props.challenge.position} legalMoves={this.props.challenge.moves}/>
            </div>
        );
    }

    public componentDidMount() {
        this.props.dispatch(randomMoveChallengeRequestFactory());
    }
}

function mapStateToProps(state: IRootState): IProps {
    return {
        challenge: state.challenge,
    };
}

export const connectedComponent = connect(mapStateToProps)(Moves);
