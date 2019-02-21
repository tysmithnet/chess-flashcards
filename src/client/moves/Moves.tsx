import cn from "classnames";
import * as _ from "lodash";
import * as React from "react";
import { connect } from "react-redux";
import { Board } from "../board/Board";
import { applyMove, IBaseProps, IMove, IRootState, STARTING_POSITION } from "../root";
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
    position: string[];
    oppHelpNum: number;
    threatHelpNum: number;
}
export class Moves extends React.Component<IProps, IState> {
    constructor(props: IProps) {
        super(props);
        this.state = {
            position: props.challenge ? props.challenge.position : [],
            identifiedOpportunities: [],
            identifiedThreats: [],
            showFailure: false,
            showSuccess: false,
            oppHelpNum: 0,
            threatHelpNum: 0,
        };
        this.handleMove = this.handleMove.bind(this);
        this.handleKeyUp = this.handleKeyUp.bind(this);
        this.goNextChallenge = this.goNextChallenge.bind(this);
        this.showFeedback = this.showFeedback.bind(this);
        this.showOpportunity = this.showOpportunity.bind(this);
        this.showThreat = this.showThreat.bind(this);
    }

    public componentDidUpdate(prevProps: IProps) {
        if (prevProps.challenge !== this.props.challenge) {
            const position = this.props.challenge ? [...this.props.challenge.position] : [];
            this.setState({
                ...this.state,
                identifiedOpportunities: [],
                identifiedThreats: [],
                position,
                showFailure: false,
                showSuccess: false,
                oppHelpNum: 0,
                threatHelpNum: 0,
            });
        }
    }

    public render() {
        if (this.props.challenge == null) {
            return <p>Loading...</p>;
        }
        return (
            <div className={"move-container"}>
                <div className="quiz-area">
                    <div>
                        <div className="title">Checks and Captures</div>
                        <div className="board-area">
                            <div className={cn("board-mask", {success: this.state.showSuccess, failure: this.state.showFailure})} />
                            <Board position={this.state.position} legalMoves={[]} onMove={this.handleMove} isBlackPerspective={!this.props.challenge.isWhitesMove} />
                        </div>
                    </div>
                </div>
            </div>
        );
    }

    public componentDidMount() {
        this.props.dispatch(randomMoveChallengeRequestFactory());
        document.addEventListener("keyup", this.handleKeyUp);
    }

    public componentWillUnmount() {
        document.removeEventListener("keyup", this.handleKeyUp);
    }

    private handleKeyUp(event: KeyboardEvent) {
        if (event.code === "Escape") {
            return;
        } else if (event.code === "Space") {
            return this.goNextChallenge();
        } else if (event.code === "KeyO") {
            return this.showOpportunity();
        } else if (event.code === "KeyT") {
            return this.showThreat();
        }
    }

    private goNextChallenge() {
        this.props.dispatch(randomMoveChallengeRequestFactory());
        this.setState({
            ...this.state,
            identifiedOpportunities: [],
            identifiedThreats: [],
            showFailure: false,
            showSuccess: false,
        });
    }

    private showThreat() {
        if (!this.props.challenge || !this.props.challenge.threats.length) {
            return;
        }
        const index = this.state.threatHelpNum;
        const opp = this.props.challenge.threats[index];
        const position = this.props.challenge.position;
        const newIndex = index + 1 > this.props.challenge.threats.length - 1 ? 0 : index + 1;
        const newState = {
            ...this.state,
            position: applyMove(position, opp),
            threatHelpNum: newIndex,
        };
        this.setState(newState);
        setTimeout(() => {
            this.setState({
                ...this.state,
                position: this.props.challenge.position,
                threatHelpNum: newIndex,
            });
        }, 200);
    }

    private showOpportunity() {
        if (!this.props.challenge || !this.props.challenge.opportunities.length) {
            return;
        }
        const index = this.state.oppHelpNum;
        const opp = this.props.challenge.opportunities[index];
        const position = this.props.challenge.position;
        const newIndex = index + 1 > this.props.challenge.opportunities.length - 1 ? 0 : index + 1;
        const newState = {
            ...this.state,
            position: applyMove(position, opp),
            oppHelpNum: newIndex,
        };
        this.setState(newState);
        setTimeout(() => {
            this.setState({
                ...this.state,
                position: this.props.challenge.position,
                oppHelpNum: newIndex,
            });
        }, 200);
    }

    private handleMove(src: string, dst: string) {
        if (this.state.identifiedOpportunities.find(o => o.src === src && o.dst === dst)) {
            return;
        }
        if (this.state.identifiedThreats.find(o => o.src === src && o.dst === dst)) {
            return;
        }
        const opp = this.props.challenge.opportunities.find(o => o.src === src && o.dst === dst);
        const newIdOpp = [...this.state.identifiedOpportunities];
        let isSuccess = false;
        if (opp) {
            newIdOpp.push(opp);
            isSuccess = true;
        }
        const threat = this.props.challenge.threats.find(o => o.src === src && o.dst === dst);
        const newIdThr = [...this.state.identifiedThreats];
        if (threat) {
            newIdThr.push(threat);
            isSuccess = true;
        }
        const oppsMissing = _.differenceWith(this.props.challenge.opportunities, newIdOpp, _.isEqual);
        const threatsMissing = _.differenceWith(this.props.challenge.threats, newIdThr, _.isEqual);
        if (oppsMissing.length === 0 && threatsMissing.length === 0) {
            return this.props.dispatch(randomMoveChallengeRequestFactory());
        }
        this.setState({
            ...this.state,
            identifiedOpportunities: newIdOpp,
            identifiedThreats: newIdThr,
        });
        const newState = {
            ...this.state,
            identifiedOpportunities: newIdOpp,
            identifiedThreats: newIdThr,
        };
        this.showFeedback(isSuccess, newState);
    }

    private showFeedback(isSuccess: boolean, state: IState) {
        this.setState({
            ...state,
            showFailure: !isSuccess,
            showSuccess: isSuccess,
        });
        setTimeout(() => {
            this.setState({
                ...state,
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
