import * as React from "react";
import { Opening } from "../chess-api";
export interface IProps {
    openings: Opening[];
    selectedOpenings: Opening[];
}
export interface IState {
    searchTerm: string;
}
export declare class Openings extends React.Component<IProps> {
    render(): JSX.Element;
}
export declare const connectedComponent: React.ComponentClass<Pick<IProps, never>, any> & {
    WrappedComponent: React.ComponentType<IProps>;
};
