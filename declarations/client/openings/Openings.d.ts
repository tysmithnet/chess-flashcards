import * as React from "react";
import { IBaseProps } from "../root";
import "./openings.styles";
export declare class Openings extends React.Component<IBaseProps> {
    private openings;
    constructor(props: IBaseProps);
    render(): JSX.Element;
}
export declare const connectedComponent: React.ComponentClass<Pick<IBaseProps, never>, any> & {
    WrappedComponent: React.ComponentType<IBaseProps>;
};
