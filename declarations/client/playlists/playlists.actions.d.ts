import { IAction } from "../root";
import { IPlaylist } from "./playlists.domain";
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
};
export interface IGetPlaylistRequest extends IAction {
    playlistType?: "game" | "opening";
    id?: number;
}
export declare function getPlaylistRequestFactory(type?: "game" | "opening"): IGetPlaylistRequest;
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
    playlistType: "opening" | "game";
    name: string;
    ids: number[];
}
export declare function createPlaylistRequestFactory(playlistType: "opening" | "game", name: string, ids: number[]): ICreatePlaylistRequest;
export interface ICreatePlaylistSuccess extends IAction {
    playlist: IPlaylist;
}
export declare function createPlaylistSuccessFactory(playlist: IPlaylist): ICreatePlaylistSuccess;
export interface ICreatePlaylistFailure extends IAction {
}
export declare function createPlaylistFailureFactory(): ICreatePlaylistFailure;
export interface IUpdatePlaylistRequest extends IAction {
    playlistType: "opening" | "game";
    id: number;
    name: string;
    ids: number[];
}
export declare function updatePlaylistRequestFactory(playlistType: "opening" | "game", id: number, name?: string, ids?: number[]): IUpdatePlaylistRequest;
export interface IUpdatePlaylistSuccess extends IAction {
    playlist: IPlaylist;
}
export declare function updatePlaylistSuccessFactory(playlist: IPlaylist): IUpdatePlaylistSuccess;
export interface IUpdatePlaylistFailure extends IAction {
    message: string;
}
export declare function updatePlaylistFailureFactory(message: string): IUpdatePlaylistFailure;
