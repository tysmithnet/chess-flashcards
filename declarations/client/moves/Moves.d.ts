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
}
export declare class Moves extends React.Component<IProps, IState> {
    constructor(props: IProps);
    render(): JSX.Element;
    componentDidMount(): void;
    private handleMove;
}
export declare const connectedComponent: React.ComponentClass<Pick<IProps, never>, any> & {
    WrappedComponent: React.ComponentType<IProps>;
};
