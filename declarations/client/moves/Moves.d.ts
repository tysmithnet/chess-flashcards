import * as React from "react";
import { IBaseProps } from "../root";
import { IRandomMoveChallenge } from "./moves.domain";
import "./moves.styles";
export interface IProps extends IBaseProps {
    challenge: IRandomMoveChallenge;
}
export interface IState {
}
export declare class Moves extends React.Component<IProps, IState> {
    constructor(props: IProps);
    render(): JSX.Element;
    componentDidMount(): void;
}
export declare const connectedComponent: React.ComponentClass<Pick<IProps, never>, any> & {
    WrappedComponent: React.ComponentType<IProps>;
};
