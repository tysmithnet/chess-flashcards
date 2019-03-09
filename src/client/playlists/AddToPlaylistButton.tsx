import { Button, Menu, MenuItem } from "@material-ui/core";
import * as React from "react";
import { connect } from "react-redux";
import { IBaseProps, IGameMeta, IOpeningMeta, IRootState } from "../root";
import { IPlaylist } from "./playlists.domain";

export interface IProps extends IBaseProps {
    gamePlaylistMeta?: IPlaylist[];
    openingPlaylistMeta?: IPlaylist[];
    selectedOpenings?: IOpeningMeta[];
    selectedGames?: IGameMeta[];
    buttonText?: string;
}

export interface IState {
    anchor: HTMLButtonElement;
}

class AddToPlaylistButton extends React.Component<IProps, IState> {
    constructor(props: IProps) {
        super(props);
        this.handleActionsClick = this.handleActionsClick.bind(this);
        this.handleActionsClose = this.handleActionsClose.bind(this);
        this.handlePlaylistSelected = this.handlePlaylistSelected.bind(this);
        this.handleCreateNew = this.handleCreateNew.bind(this);
        this.state = {
            anchor: null,
        };
    }

    public render() {
        let items = [
            <MenuItem key="create" onClick={this.handleCreateNew}>Create Playlist</MenuItem>,
        ];
        const existing = (this.props.openingPlaylistMeta || []).map(o => {
            return <MenuItem key={o.id} data-id={o.id} onClick={this.handleActionsClose}>{o.name}</MenuItem>;
        });
        items = [...items, ...existing];
        const text = this.props.buttonText ? this.props.buttonText : "Add to Playlist";
        return (
            <React.Fragment>
                <Button onClick={this.handleActionsClick}>{text}</Button>
                <Menu id="add-to-playlist" anchorEl={this.state.anchor} open={Boolean(this.state.anchor)} onClose={this.handleActionsClose}>
                    {items}
                </Menu>
            </React.Fragment>
        );
    }

    private handleCreateNew() {
        console.log("create new!");
    }

    private handleActionsClick(event: React.MouseEvent<HTMLButtonElement>) {
        this.setState({
            anchor: event.currentTarget,
        });
    }

    private handleActionsClose() {
        this.setState({
            anchor: null,
        });
    }

    private handlePlaylistSelected(event: React.MouseEvent<HTMLElement>) {
        const id = parseInt(event.currentTarget.getAttribute("data-id"), 10);
        console.log(`Playlist ${id} selected`);
    }
}

function mapStateToProps(state: IRootState, ownProps: IProps): IProps {
    return {
        gamePlaylistMeta: state.playlists.gamePlaylistMeta,
        openingPlaylistMeta: state.playlists.openingPlaylistMeta,
        buttonText: ownProps.buttonText,
        selectedOpenings: ownProps.selectedOpenings,
        selectedGames: ownProps.selectedGames,
    };
}

export const connectedComponent = connect(mapStateToProps)(AddToPlaylistButton);
