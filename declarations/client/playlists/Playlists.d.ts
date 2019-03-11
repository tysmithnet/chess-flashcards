import { Column, Filter, Sorting } from "@devexpress/dx-react-grid";
import { Theme } from "@material-ui/core";
import * as React from "react";
import { IBaseProps, IPlaylist } from "../root";
interface IProps extends IBaseProps {
    playlists: IPlaylist[];
    theme?: Theme;
    classes?: IClasses;
}
interface IState {
    columns: Column[];
    currentPage: number;
    pageSize: number;
    pageSizes: number[];
    filters: Filter[];
    searchValue: string;
    selection: number[];
    sorting: Sorting[];
    actionsButtonAnchor: HTMLButtonElement;
}
interface IClasses {
    button: any;
}
export declare class Playlists extends React.Component<IProps, IState> {
    constructor(props: IProps);
    render(): JSX.Element;
    private createActionsCell;
    private deleteSelected;
    private handleActionsClick;
    private handleActionsClose;
    private changeCurrentPage;
    private changePageSize;
    private changeFilters;
    private changeSearchValue;
    private changeSelection;
    private changeSorting;
}
export declare const connectedComponent: import("react-redux").ConnectedComponentClass<React.ComponentType<Pick<IProps, "playlists" | "dispatch" | "createWorker"> & import("@material-ui/core").StyledComponentProps<"button">>, Pick<Pick<IProps, "playlists" | "dispatch" | "createWorker"> & import("@material-ui/core").StyledComponentProps<"button">, "innerRef">>;
export {};
