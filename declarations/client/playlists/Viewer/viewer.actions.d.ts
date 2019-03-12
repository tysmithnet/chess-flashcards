import { IAction, IGame, IOpening, IPlaylist, IPosition, PlaylistType } from "../../root";
export declare const ACTION_TYPES: {
    LOAD_PLAYLIST: {
        REQUEST: string;
        SUCCESS: string;
        FAILURE: string;
    };
    LOAD_NEXT_ITEM: {
        REQUEST: string;
        SUCCESS: string;
        FAILURE: string;
    };
    LOAD_NEXT_POSITION: {
        REQUEST: string;
        SUCCESS: string;
        FAILURE: string;
    };
};
export interface ILoadPlaylistRequest extends IAction {
    playlistType: PlaylistType;
    id: number;
}
export declare function loadPlaylistRequestFactory(playlistType: PlaylistType, id: number): ILoadPlaylistRequest;
export interface ILoadPlaylistSuccess extends IAction {
    playlist: IPlaylist;
}
export declare function loadPlaylistSuccessFactory(playlist: IPlaylist): ILoadPlaylistSuccess;
export interface ILoadPlaylistFailure extends IAction {
    message: string;
}
export declare function loadPlaylistFailureFactory(message: string): ILoadPlaylistFailure;
export interface ILoadNextItemRequest extends IAction {
    playlist: IPlaylist;
}
export declare function loadNextItemRequestFactory(playlist: IPlaylist): ILoadNextItemRequest;
export interface ILoadNextItemSuccess extends IAction {
    opening: IOpening;
    game: IGame;
}
export declare function loadNextItemSuccessFactory(opening: IOpening, game: IGame): ILoadNextItemSuccess;
export interface ILoadNextItemFailure extends IAction {
    message: string;
}
export declare function loadNextItemFailureFactory(message: string): ILoadNextItemFailure;
export interface ILoadNextPositionRequest extends IAction {
    playlist: IPlaylist;
    opening: IOpening;
    game: IGame;
    currentPosition: IPosition;
}
export declare function loadNextPositionRequestFactory(playlist: IPlaylist, opening: IOpening, game: IGame, currentPosition: IPosition): ILoadNextPositionRequest;
export interface ILoadNextPositionSuccess extends IAction {
    position: IPosition;
}
export declare function loadNextPositionSuccessFactory(position: IPosition): ILoadNextPositionSuccess;
export interface ILoadNextPositionFailure extends IAction {
    message: string;
}
export declare function loadNextPositionFailureFactory(message: string): ILoadNextPositionFailure;
