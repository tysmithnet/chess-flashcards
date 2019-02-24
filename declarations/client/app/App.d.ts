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
export declare function App(props: IProps): JSX.Element;
declare const styledComponent: React.ComponentType<Pick<Pick<IProps, never>, never> & import("@material-ui/styles/withStyles").StyledComponentProps<"content" | "hide" | "root" | "appBar" | "appBarShift" | "menuButton" | "drawer" | "drawerPaper" | "drawerHeader" | "contentShift">>;
export default styledComponent;
