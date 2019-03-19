import * as React from "react";
import { IUser } from "../auth";
import { IBaseProps } from "../root/root.domain";
interface IProps extends IBaseProps {
    user: IUser;
}
export declare class Home extends React.Component<IProps> {
    constructor(props: IProps);
    render(): JSX.Element;
}
export declare const connectedComponent: import("react-redux").ConnectedComponentClass<typeof Home, Pick<IProps, never>>;
export {};
