import { Theme } from "@material-ui/core/styles";
import * as React from "react";
import { IUser } from "../auth";
import { IBaseProps } from "../root";
import { IRoute } from "./app.domain";
interface IClasses {
    root: any;
    appBar: any;
    appBarShift: any;
    menuButton: any;
    grow: any;
    hide: any;
    drawer: any;
    drawerPaper: any;
    drawerHeader: any;
    content: any;
    contentShift: any;
}
export interface IState {
    open: boolean;
    loginDialogOpen: boolean;
}
export interface IProps extends IBaseProps {
    user?: IUser;
    routes?: IRoute[];
    classes?: IClasses;
    theme?: Theme;
}
export declare class App extends React.Component<IProps, IState> {
    private classes;
    private theme;
    constructor(props: IProps);
    render(): JSX.Element;
    private handleLoginDialogOpen;
    private handleLoginDialogClose;
    private handleOpen;
    private handleClose;
    private handleLoginSubmit;
}
declare const connectedComponent: import("react-redux").ConnectedComponentClass<React.ComponentType<Pick<IProps, "user" | "routes" | "dispatch" | "createWorker"> & import("@material-ui/core").StyledComponentProps<"content" | "hide" | "root" | "appBar" | "appBarShift" | "grow" | "menuButton" | "drawer" | "drawerPaper" | "drawerHeader" | "contentShift">>, Pick<Pick<IProps, "user" | "routes" | "dispatch" | "createWorker"> & import("@material-ui/core").StyledComponentProps<"content" | "hide" | "root" | "appBar" | "appBarShift" | "grow" | "menuButton" | "drawer" | "drawerPaper" | "drawerHeader" | "contentShift">, "innerRef">>;
export default connectedComponent;
