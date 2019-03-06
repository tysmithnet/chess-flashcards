import * as React from "react";
import { IBaseProps, IOpening, IOpeningMeta } from "../root";
export interface IProps extends IBaseProps {
    openings: IOpening[];
    openingMeta: IOpeningMeta[];
}
interface IColumnFilter {
    columnName: string;
    value: string;
}
interface IColumn {
    name: string;
    title: string;
}
export interface IState {
    columns: IColumn[];
    currentPage: number;
    pageSize: number;
    pageSizes: number[];
    filters: IColumnFilter[];
}
export declare class Openings extends React.Component<IProps, IState> {
    constructor(props: IProps);
    render(): JSX.Element;
    componentDidMount(): void;
    private changeCurrentPage;
    private changePageSize;
    private changeFilters;
}
export declare const connectedComponent: import("react-redux").ConnectedComponentClass<typeof Openings, Pick<IProps, never>>;
export {};
