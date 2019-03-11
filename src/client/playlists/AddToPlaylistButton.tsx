import { Button, Dialog, DialogActions, DialogContent, DialogTitle, Menu, MenuItem, TextField } from "@material-ui/core";
import * as React from "react";
import { connect } from "react-redux";
import { IUser } from "../auth";
import { IBaseProps, IGameMeta, IOpeningMeta, IPlaylist, IRootState, PlaylistType } from "../root";
import { createPlaylistRequestFactory, getPlaylistRequestFactory, updatePlaylistRequestFactory } from "./playlists.actions";

export interface IProps extends IBaseProps {
    type: PlaylistType;
    user?: IUser;
    gamePlaylists?: IPlaylist[];
    openingPlaylists?: IPlaylist[];
    selectedOpenings?: IOpeningMeta[];
    selectedGames?: IGameMeta[];
    buttonText?: string;
}

export interface IState {
    anchor: HTMLButtonElement;
    isCreatePlaylistFormOpen: boolean;
    newPlaylistName: string;
}

class AddToPlaylistButton extends React.Component<IProps, IState> {
    constructor(props: IProps) {
        super(props);
        this.handleActionsClick = this.handleActionsClick.bind(this);
        this.handleActionsClose = this.handleActionsClose.bind(this);
        this.handlePlaylistSelected = this.handlePlaylistSelected.bind(this);
        this.handleCreateNew = this.handleCreateNew.bind(this);
        this.handleCreatePlaylistDialogCancel = this.handleCreatePlaylistDialogCancel.bind(this);
        this.handleCreatePlaylistSubmit = this.handleCreatePlaylistSubmit.bind(this);
        this.handleNewPlaylistNameChange = this.handleNewPlaylistNameChange.bind(this);
        this.handleAddToPlaylist = this.handleAddToPlaylist.bind(this);
        this.state = {
            anchor: null,
            isCreatePlaylistFormOpen: false,
            newPlaylistName: "",
        };
    }

    public render() {
        if (!this.props.user) {
            return this.renderNoLoggedInUser();
        }
        let items = [
            <MenuItem key="create" onClick={this.handleCreateNew}>Create Playlist</MenuItem>,
        ];
        const existing = (this.props.openingPlaylists || []).map(o => {
            return <MenuItem key={o.id} data-id={o.id} onClick={this.handleAddToPlaylist}>{o.name}</MenuItem>;
        });
        items = [...items, ...existing];
        const text = this.props.buttonText ? this.props.buttonText : "Add to Playlist";
        return (
            <React.Fragment>
                <Button onClick={this.handleActionsClick}>{text}</Button>
                <Menu id="add-to-playlist" anchorEl={this.state.anchor} open={Boolean(this.state.anchor)} onClose={this.handleActionsClose}>
                    {items}
                </Menu>
                <Dialog open={this.state.isCreatePlaylistFormOpen}>
                    <DialogTitle id="form-dialog-title">Login</DialogTitle>
                    <DialogContent>
                        <TextField
                            autoFocus={true}
                            margin="dense"
                            id="playlist-name"
                            label="Playlist Name"
                            value={this.state.newPlaylistName}
                            onChange={this.handleNewPlaylistNameChange}
                            fullWidth={true}
                        />
                    </DialogContent>
                    <DialogActions>
                        <Button onClick={this.handleCreatePlaylistSubmit} color="primary">
                        Create
                        </Button>
                        <Button onClick={this.handleCreatePlaylistDialogCancel} color="primary">
                        Cancel
                        </Button>
                    </DialogActions>
                    </Dialog>
            </React.Fragment>
        );
    }

    private handleAddToPlaylist(event: React.MouseEvent<HTMLElement>) {
        this.setState({
            ...this.state,
            anchor: null,
        });
        let playlist: IPlaylist = null;
        const id = parseInt(event.currentTarget.getAttribute("data-id"), 10);
        // tslint:disable-next-line:prefer-conditional-expression
        if (this.props.type === "opening") {
            playlist = this.props.openingPlaylists.find(p => p.id === id);
        } else {
            playlist = this.props.gamePlaylists.find(p => p.id === id);
        }
        const ids = [...playlist.ids, ...this.props.selectedOpenings.map(o => o.id)];
        this.props.dispatch(updatePlaylistRequestFactory(this.props.type, id, null, ids));
    }

    private handleNewPlaylistNameChange(event: React.ChangeEvent<HTMLInputElement>) {
        this.setState({
            ...this.state,
            newPlaylistName: event.currentTarget.value,
        });
    }

    private handleCreatePlaylistDialogCancel() {
        this.setState({
            ...this.state,
            isCreatePlaylistFormOpen: false,
        });
    }

    private handleCreatePlaylistSubmit() {
        this.setState({
            ...this.state,
            isCreatePlaylistFormOpen: false,
        });
        let ids: number[] = [];
        if (this.props.type === "opening") {
           ids = [...(this.props.selectedOpenings || []).map(o => o.id)];
        }
        if (this.props.type === "game") {
            ids = [...(this.props.selectedGames || []).map(o => o.id)];
         }
        this.props.dispatch(createPlaylistRequestFactory(this.props.type, this.state.newPlaylistName, ids));
    }

    private renderNoLoggedInUser() {
        return <Button disabled={true}>Login First</Button>;
    }

    private handleCreateNew() {
        this.setState({
            ...this.state,
            isCreatePlaylistFormOpen: true,
        });
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
        type: ownProps.type,
        user: state.auth.user,
        gamePlaylists: state.playlists.gamePlaylists,
        openingPlaylists: state.playlists.openingPlaylists,
        buttonText: ownProps.buttonText,
        selectedOpenings: ownProps.selectedOpenings,
        selectedGames: ownProps.selectedGames,
    };
}

export const connectedComponent = connect(mapStateToProps)(AddToPlaylistButton);
