import { Column, Filter, Grouping, Sorting } from "@devexpress/dx-react-grid";
import * as React from "react";
import { IBaseProps, IOpening, IOpeningMeta } from "../root";
export interface IProps extends IBaseProps {
    openings: IOpening[];
    openingMeta: IOpeningMeta[];
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
}
export declare class Openings extends React.Component<IProps, IState> {
    constructor(props: IProps);
    render(): JSX.Element;
    componentDidMount(): void;
    private changeCurrentPage;
    private changePageSize;
    private changeFilters;
    private changeSearchValue;
    private changeGrouping;
    private changeSelection;
    private changeSorting;
}
export declare const connectedComponent: import("react-redux").ConnectedComponentClass<typeof Openings, Pick<IProps, never>>;
