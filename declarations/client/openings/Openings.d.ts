import * as React from "react";
import { IProps } from "./openings.domain";
import "./openings.styles";
export declare class Openings extends React.Component<IProps> {
    constructor(props: IProps);
    render(): JSX.Element;
    componentDidMount(): void;
}
export declare const connectedComponent: React.ComponentClass<Pick<IProps, never>, any> & {
    WrappedComponent: React.ComponentType<IProps>;
};
