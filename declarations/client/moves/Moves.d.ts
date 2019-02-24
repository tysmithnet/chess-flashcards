import * as React from "react";
import { IBaseProps, IMove } from "../root";
import { IRandomMoveChallenge } from "./moves.domain";
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
export declare class Moves extends React.Component<IProps, IState> {
    constructor(props: IProps);
    componentDidUpdate(prevProps: IProps): void;
    render(): JSX.Element;
    componentDidMount(): void;
    componentWillUnmount(): void;
    private handleKeyUp;
    private goNextChallenge;
    private showThreat;
    private showOpportunity;
    private handleMove;
    private showFeedback;
}
export declare const connectedComponent: import("react-redux").ConnectedComponentClass<typeof Moves, Pick<IProps, never>>;
