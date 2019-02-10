import * as React from "react";
import { Opening, OpeningVariant } from "../chess-api";
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
}
export interface ISelectedOpening {
    eco: string;
    variant: OpeningVariant;
}
export declare class Openings extends React.Component<IProps, IState> {
    constructor(props: IProps);
    render(): JSX.Element;
    componentDidMount(): void;
    showDialog(): void;
    private handleVariantSelected;
    private handleSearchTextChange;
}
export declare const connectedComponent: React.ComponentClass<Pick<IProps, never>, any> & {
    WrappedComponent: React.ComponentType<IProps>;
};
