import { createStyles, Paper, Theme, withStyles } from "@material-ui/core";
import classNames from "classnames";
import * as React from "react";
import { connect } from "react-redux";
import { Board } from "../../board/Board";
import {arrayToFen, fenToArray} from "../../common/chess";
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

interface IClasses {
    boardArea: any;
}

const styles = (theme: Theme) => createStyles({
    boardArea: {
        width: 500,
        height: 500,
    },
});

interface IProps extends IBaseProps {
    playlistType: PlaylistType;
    playlistId: number;
    playlist: IPlaylist;
    opening: IOpening;
    game: IGame;
    position: IPosition;
    classes?: IClasses;
    theme?: Theme;
}

export class Viewer extends React.Component<IProps> {
    constructor(props: IProps) {
        super(props);
    }

    public render() {
        if (!this.props.position) {
            return <p>Loading...</p>;
        }
        const fen = fenToArray(this.props.position.pieces);
        return (
            <Paper>
                <div className={this.props.classes.boardArea}>
                    <Board position={fen} legalMoves={[]} />
                </div>
            </Paper>
        );
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

const styledComponent = withStyles(styles, { withTheme: true})(Viewer);
export const connectedComponent = connect(mapStateToProps)(styledComponent);
