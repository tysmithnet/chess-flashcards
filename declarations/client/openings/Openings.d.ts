import * as React from "react";
import { IBaseProps, IOpening } from "../root";
export interface IProps extends IBaseProps {
    openings: IOpening[];
}
export declare class Openings extends React.Component<IProps> {
    constructor(props: IProps);
    render(): JSX.Element;
    componentDidMount(): void;
}
export declare const connectedComponent: import("react-redux").ConnectedComponentClass<typeof Openings, Pick<IProps, never>>;
