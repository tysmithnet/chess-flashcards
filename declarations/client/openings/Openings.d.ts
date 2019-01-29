import * as React from "react";
import { IState } from "../menu/menu.domain";
import { IProps } from "./openings.domain";
import "./openings.styles";
export declare class Openings extends React.Component<IProps, IState> {
    constructor(props: IProps);
    render(): JSX.Element;
    componentDidMount(): void;
}
export declare class HelloWorld extends React.Component<any> {
    render(): JSX.Element;
}
export declare const connectedComponent: React.ComponentClass<Pick<IProps, never>, any> & {
    WrappedComponent: React.ComponentType<IProps>;
};
