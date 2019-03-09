import * as React from "react";
import { IBaseProps, IGameMeta, IOpeningMeta } from "../root";
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
declare class AddToPlaylistButton extends React.Component<IProps, IState> {
    constructor(props: IProps);
    render(): JSX.Element;
    private handleCreateNew;
    private handleActionsClick;
    private handleActionsClose;
    private handlePlaylistSelected;
}
export declare const connectedComponent: import("react-redux").ConnectedComponentClass<typeof AddToPlaylistButton, Pick<IProps, never> & IProps>;
export {};
