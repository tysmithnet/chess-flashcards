import * as React from "react";
import { IBaseProps, IMove } from "../root";
export interface IMoveCollection {
    position: string[];
    checks: IMove[];
    captures: IMove[];
    legalMoves: IMove[];
    checkmates: IMove[];
    stalemates: IMove[];
}
export interface IProps extends IBaseProps {
    position: string[];
}
export interface IState {
}
export declare class Moves extends React.Component<IBaseProps, IState> {
    render(): JSX.Element;
}
export declare const connectedComponent: React.ComponentClass<Pick<IBaseProps, never>, any> & {
    WrappedComponent: React.ComponentType<IBaseProps>;
};
