import { Column,
    Filter,
    FilteringState,
    Grouping,
    GroupingState,
    IntegratedFiltering,
    IntegratedGrouping,
    IntegratedPaging,
    IntegratedSelection,
    IntegratedSorting,
    PagingState,
    SearchState,
    SelectionState,
    Sorting,
    SortingState } from "@devexpress/dx-react-grid";
import {
    DragDropProvider,
    Grid,
    GroupingPanel,
    PagingPanel,
    SearchPanel,
    Table,
    TableFilterRow,
    TableGroupRow,
    TableHeaderRow,
    TableSelection,
    Toolbar,
} from "@devexpress/dx-react-grid-material-ui";
import { Paper } from "@material-ui/core";
import * as React from "react";
import { connect } from "react-redux";
import { IBaseProps, IOpening, IOpeningMeta, IRootState } from "../root";
import { getOpeningMetaRequestFactory } from "./openings.actions";

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

export class Openings extends React.Component<IProps, IState> {
    constructor(props: IProps) {
        super(props);
        this.changeCurrentPage = this.changeCurrentPage.bind(this);
        this.changePageSize = this.changePageSize.bind(this);
        this.changeFilters = this.changeFilters.bind(this);
        this.changeSearchValue = this.changeSearchValue.bind(this);
        this.changeGrouping = this.changeGrouping.bind(this);
        this.changeSelection = this.changeSelection.bind(this);
        this.changeSorting = this.changeSorting.bind(this);
        this.state = {
            columns: [
                { name: "id", title: "Id" },
                { name: "eco", title: "ECO" },
                { name: "name", title: "Name" },
                { name: "numMoves", title: "No. Moves" },
            ],
            currentPage: 0,
            pageSize: 15,
            pageSizes: [15, 25, 50, 100, 500, 1000, 5000],
            filters: [],
            searchValue: "",
            grouping: [],
            selection: [],
            sorting: [],
        };
    }

    public render() {
        const columns = this.state.columns;
        const rows = this.props.openingMeta || [];
        return (
            <Paper>
                <Grid
                    rows={rows}
                    columns={columns}
                >
                    <SelectionState
                        selection={this.state.selection}
                        onSelectionChange={this.changeSelection}
                    />
                    <PagingState
                        currentPage={this.state.currentPage}
                        onCurrentPageChange={this.changeCurrentPage}
                        pageSize={this.state.pageSize}
                        onPageSizeChange={this.changePageSize}
                    />
                    <FilteringState
                        filters={this.state.filters}
                        onFiltersChange={this.changeFilters}
                    />
                    <SearchState
                        value={this.state.searchValue}
                        onValueChange={this.changeSearchValue}
                    />
                    <SortingState
                        sorting={this.state.sorting}
                        onSortingChange={this.changeSorting}
                    />
                    <GroupingState
                        grouping={this.state.grouping}
                        onGroupingChange={this.changeGrouping}
                    />
                    <DragDropProvider />
                    <IntegratedSorting />
                    <IntegratedFiltering />
                    <IntegratedPaging />
                    <IntegratedSelection />
                    <IntegratedGrouping />
                    <Table />
                    <TableHeaderRow showGroupingControls={true} showSortingControls={true} />
                    <TableSelection showSelectAll={true} />
                    <TableFilterRow />
                    <PagingPanel
                        pageSizes={this.state.pageSizes}
                    />
                    <TableGroupRow />
                    <Toolbar />
                    <SearchPanel />
                    <GroupingPanel showGroupingControls={true} />
                </Grid>
            </Paper>
        );
    }

    public componentDidMount() {
        this.props.dispatch(getOpeningMetaRequestFactory());
    }

    private changeCurrentPage(pageNumber: number) {
        this.setState({
            ...this.state,
            currentPage: pageNumber,
        });
    }

    private changePageSize(size: number) {
        this.setState({
            ...this.state,
            pageSize: size,
        });
    }

    private changeFilters(filters: Filter[]) {
        this.setState({
            ...this.state,
            filters,
        });
    }

    private changeSearchValue(value: string) {
        this.setState({
            ...this.state,
            searchValue: value,
        });
    }

    private changeGrouping(grouping: Grouping[]) {
        this.setState({
            ...this.state,
            grouping,
        });
    }

    private changeSelection(selection: number[]) {
        this.setState({
            ...this.state,
            selection,
        });
    }

    private changeSorting(sorting: Sorting[]) {
        this.setState({
            ...this.state,
            sorting,
        });
    }
}

function mapStateToProps(state: IRootState): IProps {
    return {
        openings: null,
        openingMeta: state.openings.meta,
    };
}

export const connectedComponent = connect(mapStateToProps)(Openings);
