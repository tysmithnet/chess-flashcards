import axios from "axios";
import * as React from "react";
import { connect } from "react-redux";
import { IBaseProps, IPlaylist, IRootState, PlaylistType } from "../root";

interface IProps extends IBaseProps {
    playlist?: IPlaylist;
    type?: PlaylistType;
    id?: number;
}

interface IState {

}

export class Viewer extends React.Component<IProps, IState> {
    public render() {
        return <h1>{this.props.type} - {this.props.id}</h1>;
    }
}

function mapStateToProps(state: IRootState, ownProps: IProps): IProps {
    if (ownProps && ownProps.playlist) {
        return {
            playlist: ownProps.playlist,
        };
    }
    if (!state.router) {
        return { };
    }
    const location = state.router.location;
    const parts = location.pathname.split("/");
    const type = parts[2] as PlaylistType;
    const id = parseInt(parts[3], 10);
    return {
        type,
        id,
    };
}

export const connectedComponent = connect(mapStateToProps)(Viewer);
