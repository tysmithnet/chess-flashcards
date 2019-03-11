import { Column, Filter, Grouping, Sorting } from "@devexpress/dx-react-grid";
import * as React from "react";
import { IBaseProps, IPlaylist } from "../root";
export interface IProps extends IBaseProps {
    playlists: IPlaylist[];
}
export interface IState {
    columns: Column[];
    currentPage: number;
    pageSize: number;
    pageSizes: number[];
    filters: Filter[];
    searchValue: string;
    grouping: Grouping[];
    selection: number[];
    sorting: Sorting[];
    actionsButtonAnchor: HTMLButtonElement;
}
export declare class Playlists extends React.Component<IProps, IState> {
    constructor(props: IProps);
    render(): JSX.Element;
    private deleteSelected;
    private handleActionsClick;
    private handleActionsClose;
    private changeCurrentPage;
    private changePageSize;
    private changeFilters;
    private changeSearchValue;
    private changeGrouping;
    private changeSelection;
    private changeSorting;
}
export declare const connectedComponent: import("react-redux").ConnectedComponentClass<typeof Playlists, Pick<IProps, never>>;
