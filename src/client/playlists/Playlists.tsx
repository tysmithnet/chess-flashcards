import {
    Grid,
    Table,
    TableHeaderRow,
  } from "@devexpress/dx-react-grid-material-ui";
import { Paper } from "@material-ui/core";
import * as React from "react";
import { connect } from "react-redux";
import { IBaseProps, IRootState } from "../root";
import { IPlaylist } from "./playlists.domain";
export interface IProps extends IBaseProps {
    gamePlaylistMeta: IPlaylist[];
    openingPlaylistMeta: IPlaylist[];
}

export class Playlists extends React.Component<IProps, {}> {
    constructor(props: IProps) {
        super(props);
    }

    public render() {
        return (
            <Paper>
                hi
            </Paper>
        );
    }
}

function mapStateToProps(state: IRootState): IProps {
    return {
        gamePlaylistMeta: null,
        openingPlaylistMeta: null,
    };
}

export const connectedComponent = connect(mapStateToProps)(Playlists);
