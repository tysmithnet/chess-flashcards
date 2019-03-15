import {
    Column,
    Filter,
    FilteringState,
    IntegratedFiltering,
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
    PagingPanel,
    SearchPanel,
    Table,
    TableFilterRow,
    TableHeaderRow,
    TableSelection,
    Toolbar,
  } from "@devexpress/dx-react-grid-material-ui";
import { Button, createStyles, IconButton, Paper, Theme, withStyles } from "@material-ui/core";
import DeleteIcon from "@material-ui/icons/Delete";
import VisibilityIcon from "@material-ui/icons/Visibility";
import * as React from "react";
import { connect } from "react-redux";
import { IBaseProps, IPlaylist, IRootState } from "../../root";
import { deletePlaylistRequestFactory, viewPlaylistRequestFactory } from "./master-list.actions";
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

const styles = (theme: Theme) => createStyles({
    button: {
        margin: theme.spacing.unit,
      },
});

export class MasterList extends React.Component<IProps, IState> {
    constructor(props: IProps) {
        super(props);
        this.changeCurrentPage = this.changeCurrentPage.bind(this);
        this.changePageSize = this.changePageSize.bind(this);
        this.changeFilters = this.changeFilters.bind(this);
        this.changeSearchValue = this.changeSearchValue.bind(this);
        this.changeSelection = this.changeSelection.bind(this);
        this.changeSorting = this.changeSorting.bind(this);
        this.handleActionsClick = this.handleActionsClick.bind(this);
        this.handleActionsClose = this.handleActionsClose.bind(this);
        this.deleteSelected = this.deleteSelected.bind(this);
        this.createActionsCell = this.createActionsCell.bind(this);
        this.handleDeletePlaylist = this.handleDeletePlaylist.bind(this);
        this.handleViewPlaylist = this.handleViewPlaylist.bind(this);

        this.state = {
            columns: [
                { name: "id", title: "Id" },
                { name: "type", title: "Type" },
                { name: "name", title: "Name" },
                { name: null, title: "Actions", getCellValue: this.createActionsCell },
            ],
            currentPage: 0,
            pageSize: 10,
            pageSizes: [5, 10, 15, 25, 50, 100],
            filters: [],
            searchValue: "",
            selection: [],
            sorting: [],
            actionsButtonAnchor: null,
        };
    }

    public render() {
        const rows = this.props.playlists || [];
        return (
            <Paper>
                <Button onClick={this.deleteSelected}>Delete Selected</Button>
                <Grid
                    rows={rows}
                    columns={this.state.columns}
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
                    <DragDropProvider />
                    <IntegratedSorting />
                    <IntegratedFiltering />
                    <IntegratedPaging />
                    <IntegratedSelection />
                    <Table />
                    <TableHeaderRow showSortingControls={true} />
                    <TableSelection showSelectAll={true} />
                    <TableFilterRow />
                    <PagingPanel
                        pageSizes={this.state.pageSizes}
                    />
                    <Toolbar />
                    <SearchPanel />
                </Grid>
            </Paper>
        );
    }

    private createActionsCell(playlist: IPlaylist) {
        return (
            <React.Fragment>
                <IconButton
                    className={this.props.classes.button}
                    aria-label="Delete"
                    data-type={playlist.type}
                    data-id={playlist.id}
                    onClick={this.handleDeletePlaylist}
                >
                    <DeleteIcon />
                </IconButton>
                <IconButton
                    className={this.props.classes.button}
                    aria-label="View"
                    data-type={playlist.type}
                    data-id={playlist.id}
                    onClick={this.handleViewPlaylist}
                >
                    <VisibilityIcon />
                </IconButton>
            </React.Fragment>
        );
    }

    private handleDeletePlaylist(event: React.MouseEvent<HTMLButtonElement>) {
        const type = event.currentTarget.getAttribute("data-type");
        const id = parseInt(event.currentTarget.getAttribute("data-id"), 10);
        const playlist = this.props.playlists.find(p => p.type === type && p.id === id);
        if (playlist) {
            this.props.dispatch(deletePlaylistRequestFactory([playlist]));
        }
    }

    private handleViewPlaylist(event: React.MouseEvent<HTMLButtonElement>) {
        const type = event.currentTarget.getAttribute("data-type");
        const id = parseInt(event.currentTarget.getAttribute("data-id"), 10);
        const playlist = this.props.playlists.find(p => p.type === type && p.id === id);
        if (playlist) {
            this.props.dispatch(viewPlaylistRequestFactory(playlist));
        }
    }

    private deleteSelected() {
        const selectedPlaylists = this.state.selection.map(i => this.props.playlists[i]);
        this.props.dispatch(deletePlaylistRequestFactory(selectedPlaylists));
    }

    private handleActionsClick(event: React.MouseEvent<HTMLButtonElement>) {
        this.setState({
            ...this.state,
            actionsButtonAnchor: event.currentTarget,
        });
    }

    private handleActionsClose() {
        this.setState({
            ...this.state,
            actionsButtonAnchor: null,
        });
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
        playlists: state.playlists.masterList.playlists,
    };
}

const styledComponent = withStyles(styles, { withTheme: true})(MasterList);
export const connectedComponent = connect(mapStateToProps)(styledComponent);
