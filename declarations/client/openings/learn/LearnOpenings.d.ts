import * as React from "react";
import { match } from "react-router";
import { Opening as IOpening } from "../../chess-api";
import { IBaseProps } from "../../root";
import "./learn.styles";
export interface IProps extends IBaseProps {
    match?: match<any>;
    history?: any;
    openings: IOpening[];
}
export declare class LearnOpenings extends React.Component<IProps> {
    constructor(props: IProps);
    render(): JSX.Element;
}
export declare const connectedComponent: React.ComponentClass<Pick<IProps, never>, any> & {
    WrappedComponent: React.ComponentType<IProps>;
};
