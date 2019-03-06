import {
    Grid,
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
}

export class Openings extends React.Component<IProps, IState> {
    constructor(props: IProps) {
        super(props);
        this.state = {
            columns: [
                { name: "id", title: "Id" },
                { name: "eco", title: "ECO" },
                { name: "name", title: "Name" },
                { name: "numMoves", title: "No. Moves" },
            ],
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
                    <Table />
                    <TableHeaderRow />
                </Grid>
            </Paper>
        );
    }

    public componentDidMount() {
        this.props.dispatch(getOpeningMetaRequestFactory());
    }
}

function mapStateToProps(state: IRootState): IProps {
    return {
        openings: null,
        openingMeta: state.openings.meta,
    };
}

export const connectedComponent = connect(mapStateToProps)(Openings);
