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
    PlaylistType,
} from "../../root";
import { loadNextItemRequestFactory, loadNextPositionRequestFactory, loadPlaylistRequestFactory } from "./viewer.actions";

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

    public componentDidUpdate(prevProps: IProps) {
        if (!this.props.playlist) {
            this.props.dispatch(loadPlaylistRequestFactory(this.props.playlistType, this.props.playlistId));
            return;
        }
        if (!this.props.opening && !this.props.game) {
            this.props.dispatch(loadNextItemRequestFactory(this.props.playlist));
            return;
        }
        if (!this.props.position) {
            this.props.dispatch(loadNextPositionRequestFactory(this.props.playlist, this.props.opening, this.props.game, this.props.position));
            return;
        }
    }
}

function mapStateToProps(state: IRootState, ownProps: IRoutedProps): IProps {
    return {
        playlistType: (ownProps.match.params as any).type,
        playlistId: parseInt((ownProps.match.params as any).id, 10),
        opening: state.playlists.viewer.opening,
        playlist: state.playlists.viewer.playlist,
        position: state.playlists.viewer.position,
        game: state.playlists.viewer.game,
    };
}

export const connectedComponent = connect(mapStateToProps)(Viewer);
