import * as React from "react";
import { match } from "react-router";
import { OpeningMeta as IOpeningMeta } from "../../chess-api";
import { IBaseProps } from "../../root";
import "./learn.styles";
export interface IProps extends IBaseProps {
    match?: match<any>;
    openings: IOpeningMeta[];
}
export declare class LearnOpening extends React.Component<IProps> {
    constructor(props: IProps);
    render(): JSX.Element;
}
export declare const connectedComponent: React.ComponentClass<Pick<IProps, never>, any> & {
    WrappedComponent: React.ComponentType<IProps>;
};
