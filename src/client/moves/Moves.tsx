import cn from "classnames";
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
    identifiedOpportunities: IMove[];
    identifiedThreats: IMove[];
    showSuccess: boolean;
    showFailure: boolean;
}
export class Moves extends React.Component<IProps, IState> {
    constructor(props: IProps) {
        super(props);
        this.state = {
            identifiedOpportunities: [],
            identifiedThreats: [],
            showFailure: false,
            showSuccess: false,
        };
        this.handleMove = this.handleMove.bind(this);
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
                            <div className={cn("board-mask", {success: this.state.showSuccess, failure: this.state.showFailure})} />
                            <Board position={this.props.challenge.position} legalMoves={[]} onMove={this.handleMove} />
                        </div>
                    </div>
                </div>
            </div>
        );
    }

    public componentDidMount() {
        this.props.dispatch(randomMoveChallengeRequestFactory());
    }

    private handleMove(src: string, dst: string) {
        if (this.state.identifiedOpportunities.find(x => x.src === src && x.dst === dst)) {
            return;
        }
        if (this.state.identifiedThreats.find(x => x.src === src && x.dst === dst)) {
            return;
        }
        const opp = this.props.challenge.opportunities.find(o => o.src === src && o.dst === o.dst);
        const newIdOpp = [...this.state.identifiedOpportunities];
        let isSuccess = false;
        if (opp) {
            newIdOpp.push(opp);
            isSuccess = true;
        }
        const threat = this.props.challenge.threats.find(o => o.src === src && o.dst === o.dst);
        const newIdThr = [...this.state.identifiedThreats];
        if (threat) {
            newIdThr.push(threat);
            isSuccess = true;
        }
        this.setState({
            ...this.state,
            identifiedOpportunities: newIdOpp,
            identifiedThreats: newIdThr,
            showFailure: !isSuccess,
            showSuccess: isSuccess,
        });
        setTimeout(() => {
            this.setState({
                ...this.state,
                showFailure: false,
                showSuccess: false,
            });
        }, 200);
    }
}

function mapStateToProps(state: IRootState): IProps {
    return {
        challenge: state.moves.challenge,
    };
}

export const connectedComponent = connect(mapStateToProps)(Moves);
