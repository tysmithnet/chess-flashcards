import { IAction, IPlaylist, PlaylistType } from "../../root";
export declare const ACTION_TYPES: {
    GET_PLAYLIST: {
        REQUEST: string;
        SUCCESS: string;
        FAILURE: string;
    };
    CREATE_PLAYLIST: {
        REQUEST: string;
        SUCCESS: string;
        FAILURE: string;
    };
    UPDATE_PLAYLIST: {
        REQUEST: string;
        SUCCESS: string;
        FAILURE: string;
    };
    DELETE_PLAYLISTS: {
        REQUEST: string;
        SUCCESS: string;
        FAILURE: string;
    };
};
export interface IGetPlaylistRequest extends IAction {
    playlistType?: PlaylistType;
    id?: number;
}
export declare function getPlaylistRequestFactory(type?: PlaylistType): IGetPlaylistRequest;
export interface IGetPlaylistSuccess extends IAction {
    game: IPlaylist[];
    opening: IPlaylist[];
}
export declare function getPlaylistSuccessFactory(game: IPlaylist[], opening: IPlaylist[]): IGetPlaylistSuccess;
export interface IGetPlaylistFailure extends IAction {
    message: string;
}
export declare function getPlaylistFailureFactory(message: string): {
    type: string;
    message: string;
};
export interface ICreatePlaylistRequest extends IAction {
    playlistType: PlaylistType;
    name: string;
    ids: number[];
}
export declare function createPlaylistRequestFactory(playlistType: PlaylistType, name: string, ids: number[]): ICreatePlaylistRequest;
export interface ICreatePlaylistSuccess extends IAction {
    playlist: IPlaylist;
}
export declare function createPlaylistSuccessFactory(playlist: IPlaylist): ICreatePlaylistSuccess;
export interface ICreatePlaylistFailure extends IAction {
}
export declare function createPlaylistFailureFactory(): ICreatePlaylistFailure;
export interface IUpdatePlaylistRequest extends IAction {
    playlistType: PlaylistType;
    id: number;
    name: string;
    ids: number[];
}
export declare function updatePlaylistRequestFactory(playlistType: PlaylistType, id: number, name?: string, ids?: number[]): IUpdatePlaylistRequest;
export interface IUpdatePlaylistSuccess extends IAction {
    playlist: IPlaylist;
}
export declare function updatePlaylistSuccessFactory(playlist: IPlaylist): IUpdatePlaylistSuccess;
export interface IUpdatePlaylistFailure extends IAction {
    message: string;
}
export declare function updatePlaylistFailureFactory(message: string): IUpdatePlaylistFailure;
export interface IDeletePlaylistsRequest extends IAction {
    playlists: IPlaylist[];
}
export declare function deletePlaylistRequestFactory(playlists: IPlaylist[]): IDeletePlaylistsRequest;
export interface IDeletePlaylistsSuccess extends IAction {
}
export declare function deletePlaylistsSuccessFactory(): IDeletePlaylistsSuccess;
export interface IDeletePlaylistsFailure extends IAction {
    message: string;
}
export declare function deletePlaylistsFailureFactory(message: string): IDeletePlaylistsFailure;
