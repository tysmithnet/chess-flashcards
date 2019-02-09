import * as React from "react";
import { Opening } from "../chess-api";
import { IBaseProps } from "../root";
export interface IProps extends IBaseProps {
    openings: Opening[];
    selectedOpenings: Opening[];
}
export interface IState {
    searchTerm: string;
}
export declare class Openings extends React.Component<IProps, IState> {
    constructor(props: IProps);
    render(): JSX.Element;
    componentDidMount(): void;
}
export declare const connectedComponent: React.ComponentClass<Pick<IProps, never>, any> & {
    WrappedComponent: React.ComponentType<IProps>;
};
