import { IntegratedPaging, PagingState } from "@devexpress/dx-react-grid";
import {
    Grid,
    PagingPanel,
    Table,
    TableHeaderRow,
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

interface IColumn {
    name: string;
    title: string;
}

export interface IState {
    columns: IColumn[];
    currentPage: number;
    pageSize: number;
    pageSizes: number[];
}

export class Openings extends React.Component<IProps, IState> {
    constructor(props: IProps) {
        super(props);
        this.changeCurrentPage = this.changeCurrentPage.bind(this);
        this.changePageSize = this.changePageSize.bind(this);
        this.state = {
            columns: [
                { name: "id", title: "Id" },
                { name: "eco", title: "ECO" },
                { name: "name", title: "Name" },
                { name: "numMoves", title: "No. Moves" },
            ],
            currentPage: 0,
            pageSize: 15,
            pageSizes: [15, 25, 50],
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
                    <PagingState
                        currentPage={this.state.currentPage}
                        onCurrentPageChange={this.changeCurrentPage}
                        pageSize={this.state.pageSize}
                        onPageSizeChange={this.changePageSize}
                    />
                    <IntegratedPaging />
                    <Table />
                    <TableHeaderRow />
                    <PagingPanel
                        pageSizes={this.state.pageSizes}
                    />
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
}

function mapStateToProps(state: IRootState): IProps {
    return {
        openings: null,
        openingMeta: state.openings.meta,
    };
}

export const connectedComponent = connect(mapStateToProps)(Openings);
