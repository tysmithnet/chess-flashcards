import * as React from "react";
import { IUser } from "../auth";
import { IBaseProps, IGameMeta, IOpeningMeta } from "../root";
import { IPlaylist } from "./playlists.domain";
export interface IProps extends IBaseProps {
    type: "opening" | "game";
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
declare class AddToPlaylistButton extends React.Component<IProps, IState> {
    constructor(props: IProps);
    render(): JSX.Element;
    private handleAddToPlaylist;
    private handleNewPlaylistNameChange;
    private handleCreatePlaylistDialogCancel;
    private handleCreatePlaylistSubmit;
    private renderNoLoggedInUser;
    private handleCreateNew;
    private handleActionsClick;
    private handleActionsClose;
    private handlePlaylistSelected;
}
export declare const connectedComponent: import("react-redux").ConnectedComponentClass<typeof AddToPlaylistButton, Pick<IProps, never> & IProps>;
export {};
