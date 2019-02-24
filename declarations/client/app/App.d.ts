import * as React from "react";
import { IUser } from "../auth";
import { IBaseProps } from "../root";
import { IRoute } from "./app.domain";
export interface IClasses {
    root: any;
    appBar: any;
    appBarShift: any;
    menuButton: any;
    hide: any;
    drawer: any;
    drawerPaper: any;
    drawerHeader: any;
    content: any;
    contentShift: any;
}
export interface IState {
    open: boolean;
}
export interface IProps extends IBaseProps {
    user?: IUser;
    routes?: IRoute[];
    classes?: IClasses;
}
export declare class App extends React.Component<IProps> {
    render(): JSX.Element;
}
declare const connectedComponent: import("react-redux").ConnectedComponentClass<typeof App, Pick<IProps, never>>;
export default connectedComponent;
