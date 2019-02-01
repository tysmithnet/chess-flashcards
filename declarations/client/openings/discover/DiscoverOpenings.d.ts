import * as React from "react";
import { IProps } from "./discover.domain";
export declare class DiscoverOpenings extends React.Component<IProps> {
    constructor(props: IProps);
    render(): JSX.Element;
    componentDidMount(): void;
    private handleOnMove;
}
export declare const connectedComponent: React.ComponentClass<Pick<IProps, never>, any> & {
    WrappedComponent: React.ComponentType<IProps>;
};
