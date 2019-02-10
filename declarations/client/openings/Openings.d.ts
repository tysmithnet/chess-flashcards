import * as React from "react";
import { Move, Opening, OpeningVariant } from "../chess-api";
import { IBaseProps } from "../root";
import "./openings.styles";
export interface IProps extends IBaseProps {
    openings: Opening[];
}
export interface IState {
    searchText: string;
    selectedOpenings: ISelectedOpening[];
    showDialog: boolean;
    current: ISelectedOpening;
    moveNum: number;
    position: string[];
    legalMoves: Move[];
}
export interface ISelectedOpening {
    eco: string;
    variant: OpeningVariant;
}
export declare class Openings extends React.Component<IProps, IState> {
    constructor(props: IProps);
    render(): JSX.Element;
    componentDidMount(): void;
    componentWillUnmount(): void;
    private handleMove;
    private createDialog;
    private showDialog;
    private hideDialog;
    private handleSearchTextChange;
}
export declare const connectedComponent: React.ComponentClass<Pick<IProps, never>, any> & {
    WrappedComponent: React.ComponentType<IProps>;
};
