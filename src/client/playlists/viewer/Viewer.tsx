import { createStyles, Icon, IconButton, Paper, Theme, withStyles } from "@material-ui/core";
import Flip from "@material-ui/icons/Autorenew";
import ChevronLeft from "@material-ui/icons/ChevronLeft";
import ChevronRight from "@material-ui/icons/ChevronRight";
import Help from "@material-ui/icons/Help";
import Play from "@material-ui/icons/PlayCircleFilledOutlined";
import SkipNext from "@material-ui/icons/SkipNext";
import classNames from "classnames";
import * as React from "react";
import { connect } from "react-redux";
import { Board } from "../../board/Board";
import {arrayToFen, fenToArray} from "../../common/chess";
import {
    IBaseProps,
    IGame,
    IMove,
    IOpening,
    IPlaylist,
    IPosition,
    IRootState,
    IRoutedProps,
    PlaylistType,
} from "../../root";
import { connectedComponent as Stats } from "./Stats";
import {
    changeLearnPositionRequestFactory,
    changeModeRequestFactory,
    checkMoveRequestFactory,
    loadNextItemRequestFactory,
    loadNextPositionRequestFactory,
    loadPlaylistRequestFactory} from "./viewer.actions";
import { ViewerMode } from "./viewer.domain";

interface IClasses {
    root: any;
    horizontalCenter: any;
    boardArea: any;
}

const styles = (theme: Theme) => createStyles({
    root: {
        display: "flex",
        flexDirection: "column",
    },
    horizontalCenter: {
        display: "flex",
        justifyContent: "center",
    },
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
    isLearnMovesMode: boolean;
    learnMovePositionIndex: number;
}

interface IState {
    isBlackPerspective: boolean;
}

export class Viewer extends React.Component<IProps, IState> {
    constructor(props: IProps) {
        super(props);
        this.handleMove = this.handleMove.bind(this);
        this.ensureDataIsLoaded = this.ensureDataIsLoaded.bind(this);
        this.handleFlipBoard = this.handleFlipBoard.bind(this);
        this.handleChangeToLearnMovesMode = this.handleChangeToLearnMovesMode.bind(this);
        this.handleChangeToMakeMovesMode = this.handleChangeToMakeMovesMode.bind(this);
        this.handleLearnGoForward = this.handleLearnGoForward.bind(this);
        this.handleLearnGoBack = this.handleLearnGoBack.bind(this);
        this.handleSkip = this.handleSkip.bind(this);
        this.state = {
            isBlackPerspective: false,
        };
    }

    public render() {
        if (!this.props.position) {
            return <p>Loading...</p>;
        }
        if (this.props.isLearnMovesMode) {
            return this.renderLearnMovesMode();
        } else {
            return this.renderMakeMovesMode();
        }
    }

    public componentDidMount() {
        this.ensureDataIsLoaded();
    }

    public componentDidUpdate(prevProps: IProps, prevState: IState) {
        this.ensureDataIsLoaded();
    }

    private renderLearnMovesMode() {
        const positions = this.props.playlist.type === PlaylistType.game ? this.props.game.positions : this.props.opening.positions;
        const currentPosition = positions[this.props.learnMovePositionIndex];
        const fen = fenToArray(currentPosition.pieces);
        return (
            <div className={this.props.classes.root}>
                <Stats />
                <div className={this.props.classes.horizontalCenter}>
                    <div>
                        <div className={this.props.classes.boardArea}>
                            <Board position={fen} legalMoves={[]} isBlackPerspective={this.state.isBlackPerspective} />
                        </div>
                        <div className={this.props.classes.horizontalCenter}>
                            {this.getButtons()}
                        </div>
                    </div>
                </div>
            </div>
        );
    }

    private renderMakeMovesMode() {
        const fen = fenToArray(this.props.position.pieces);
        return (
            <div className={this.props.classes.root}>
                <Stats />
                <div className={this.props.classes.horizontalCenter}>
                    <div>
                        <div className={this.props.classes.boardArea}>
                            <Board position={fen} legalMoves={[]} isBlackPerspective={this.state.isBlackPerspective} onMove={this.handleMove} />
                        </div>
                        <div className={this.props.classes.horizontalCenter}>
                            {this.getButtons()}
                        </div>
                    </div>
                </div>
            </div>
        );
    }

    private getButtons() {
        let helpOrPlay = null;
        let learnButtons = null;
        if (this.props.isLearnMovesMode) {
            helpOrPlay = (
                <IconButton onClick={this.handleChangeToMakeMovesMode}>
                    <Play />
                </IconButton>
            );
            learnButtons = (
                <React.Fragment>
                    <IconButton onClick={this.handleLearnGoBack} aria-label="Go Back">
                        <ChevronLeft />
                    </IconButton>
                    <IconButton onClick={this.handleLearnGoForward} aria-label="Go Forward">
                        <ChevronRight />
                    </IconButton>
                </React.Fragment>
            );
        } else {
            helpOrPlay = (
                <IconButton onClick={this.handleChangeToLearnMovesMode}>
                    <Help/>
                </IconButton>
            );
        }
        return (
            <React.Fragment>
                <IconButton onClick={this.handleFlipBoard} aria-label="Flip Board">
                    <Flip />
                </IconButton>
                {helpOrPlay}
                {learnButtons}
                <IconButton onClick={this.handleSkip} aria-label="Skip">
                    <SkipNext />
                </IconButton>
            </React.Fragment>
        );
    }

    private handleSkip() {
        this.props.dispatch(loadNextItemRequestFactory());
    }

    private handleLearnGoForward() {
        const positions = this.props.playlist.type === PlaylistType.game ? this.props.game.positions : this.props.opening.positions;
        const nextIndex = Math.min(positions.length - 1, this.props.learnMovePositionIndex + 1);
        this.props.dispatch(changeLearnPositionRequestFactory(nextIndex));
    }

    private handleLearnGoBack() {
        const nextIndex = Math.max(0, this.props.learnMovePositionIndex - 1);
        this.props.dispatch(changeLearnPositionRequestFactory(nextIndex));
    }

    private handleFlipBoard() {
        this.setState({
            ...this.state,
            isBlackPerspective: !this.state.isBlackPerspective,
        });
    }

    private handleChangeToLearnMovesMode() {
        this.props.dispatch(changeModeRequestFactory(ViewerMode.LearnMoves));
    }

    private handleChangeToMakeMovesMode() {
        this.props.dispatch(changeModeRequestFactory(ViewerMode.MakeMoves));
    }

    private ensureDataIsLoaded() {
        if (!this.props.playlist) {
            this.props.dispatch(loadPlaylistRequestFactory(this.props.playlistType, this.props.playlistId));
            return;
        }
        if (!this.props.opening && !this.props.game) {
            this.props.dispatch(loadNextItemRequestFactory());
            return;
        }
        if (!this.props.position) {
            this.props.dispatch(loadNextPositionRequestFactory());
            return;
        }
    }

    private handleMove(src: string, dst: string) {
        this.props.dispatch(checkMoveRequestFactory({src, dst}));
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
        isLearnMovesMode: state.playlists.viewer.isLearnMovesMode || false,
        learnMovePositionIndex: state.playlists.viewer.learnMovePositionIndex || 0,
    };
}

const styledComponent = withStyles(styles, { withTheme: true})(Viewer);
export const connectedComponent = connect(mapStateToProps)(styledComponent);
