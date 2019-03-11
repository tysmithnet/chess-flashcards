import * as React from "react";
import { connect } from "react-redux";
import {
    IBaseProps,
    IGame,
    IOpening,
    IPlaylist,
    IPosition,
    IRootState,
    IRoutedProps,
    PlaylistType } from "../../root";

interface IProps extends IBaseProps {
    playlistType: PlaylistType;
    playlistId: number;
    playlist: IPlaylist;
    opening: IOpening;
    game: IGame;
    position: IPosition;
}

export class Viewer extends React.Component<IProps> {
    constructor(props: IProps) {
        super(props);
    }

    public render() {
        return <h1>{`${this.props.playlistType} - ${this.props.playlistId}`}</h1>;
    }

    public componentDidMount() {
        this.props.dispatch({type: "sayhello"});
    }
}

function mapStateToProps(state: IRootState, ownProps: IRoutedProps): IProps {
    return {
        playlistType: (ownProps.match.params as any).type,
        playlistId: parseInt((ownProps.match.params as any).id, 10),
        // opening: state.playlists.viewer.opening,
        opening: null,
        // playlist: state.playlists.viewer.playlist,
        playlist: null,
        // position: state.playlists.viewer.position,
        position: null,
        // game: state.playlists.viewer.game,
        game: null,
    };
}

export const connectedComponent = connect(mapStateToProps)(Viewer);
