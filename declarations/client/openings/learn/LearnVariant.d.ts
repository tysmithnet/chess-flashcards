import * as React from "react";
import { match } from "react-router";
import { Opening as IOpening } from "../../chess-api";
import { IBaseProps } from "../../root";
export interface IProps extends IBaseProps {
    match?: match<any>;
    openings: IOpening[];
}
export declare class LearnVariant extends React.Component<IProps> {
    constructor(props: IProps);
    render(): JSX.Element;
}
export declare const connectedComponent: React.ComponentClass<Pick<IProps, never>, any> & {
    WrappedComponent: React.ComponentType<IProps>;
};
