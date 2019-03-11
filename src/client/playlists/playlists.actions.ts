import { IAction, IPlaylist, PlaylistType } from "../root";

export const ACTION_TYPES = {
    GET_PLAYLIST: {
        REQUEST: "@playlists/GetPlaylistRequest",
        SUCCESS: "@playlists/GetPlaylistSuccess",
        FAILURE: "@playlists/GetPlaylistFailure",
    },
    CREATE_PLAYLIST: {
        REQUEST: "@playlists/CreatePlaylistRequest",
        SUCCESS: "@playlists/CreatePlaylistSuccess",
        FAILURE: "@playlists/CreatePlaylistFailure",
    },
    UPDATE_PLAYLIST: {
        REQUEST: "@playlists/UpdatePlaylistRequest",
        SUCCESS: "@playlists/UpdatePlaylistSuccess",
        FAILURE: "@playlists/UpdatePlaylistFailure",
    },
    DELETE_PLAYLISTS: {
        REQUEST: "@playlists/DeletePlaylistsRequest",
        SUCCESS: "@playlists/DeletePlaylistsSuccess",
        FAILURE: "@playlists/DeletePlaylistsFailure",
    },
};

export interface IGetPlaylistRequest extends IAction {
    playlistType?: PlaylistType;
    id?: number;
}

export function getPlaylistRequestFactory(type?: PlaylistType): IGetPlaylistRequest {
    return {
        type: ACTION_TYPES.GET_PLAYLIST.REQUEST,
        playlistType: type,
    };
}

export interface IGetPlaylistSuccess extends IAction {
    game: IPlaylist[];
    opening: IPlaylist[];
}

export function getPlaylistSuccessFactory(game: IPlaylist[], opening: IPlaylist[]): IGetPlaylistSuccess {
    return {
        type: ACTION_TYPES.GET_PLAYLIST.SUCCESS,
        game,
        opening,
    };
}

export interface IGetPlaylistFailure extends IAction {
    message: string;
}

export function getPlaylistFailureFactory(message: string) {
    return {
        type: ACTION_TYPES.GET_PLAYLIST.FAILURE,
        message,
    };
}

export interface ICreatePlaylistRequest extends IAction {
    playlistType: PlaylistType;
    name: string;
    ids: number[];
}

export function createPlaylistRequestFactory(playlistType: PlaylistType, name: string, ids: number[]): ICreatePlaylistRequest {
    return {
        type: ACTION_TYPES.CREATE_PLAYLIST.REQUEST,
        playlistType,
        name,
        ids,
    };
}

export interface ICreatePlaylistSuccess extends IAction {
    playlist: IPlaylist;
}

export function createPlaylistSuccessFactory(playlist: IPlaylist): ICreatePlaylistSuccess {
    return {
        type: ACTION_TYPES.CREATE_PLAYLIST.SUCCESS,
        playlist,
    };
}

export interface ICreatePlaylistFailure extends IAction { }

export function createPlaylistFailureFactory(): ICreatePlaylistFailure {
    return {
        type: ACTION_TYPES.CREATE_PLAYLIST.FAILURE,
    };
}

export interface IUpdatePlaylistRequest extends IAction {
    playlistType: PlaylistType;
    id: number;
    name: string;
    ids: number[];
}

export function updatePlaylistRequestFactory(playlistType: PlaylistType, id: number, name?: string, ids?: number[]): IUpdatePlaylistRequest {
    return {
        type: ACTION_TYPES.UPDATE_PLAYLIST.REQUEST,
        id,
        name,
        playlistType,
        ids,
    };
}

export interface IUpdatePlaylistSuccess extends IAction {
    playlist: IPlaylist;
}

export function updatePlaylistSuccessFactory(playlist: IPlaylist): IUpdatePlaylistSuccess {
    return {
        type: ACTION_TYPES.UPDATE_PLAYLIST.SUCCESS,
        playlist,
    };
}

export interface IUpdatePlaylistFailure extends IAction {
    message: string;
}

export function updatePlaylistFailureFactory(message: string): IUpdatePlaylistFailure {
    return {
        type: ACTION_TYPES.UPDATE_PLAYLIST.FAILURE,
        message,
    };
}

export interface IDeletePlaylistsRequest extends IAction {
    playlists: IPlaylist[];
}

export function deletePlaylistRequestFactory(playlists: IPlaylist[]): IDeletePlaylistsRequest {
    return {
        type: ACTION_TYPES.DELETE_PLAYLISTS.REQUEST,
        playlists,
    };
}

export interface IDeletePlaylistsSuccess extends IAction { }

export function deletePlaylistsSuccessFactory(): IDeletePlaylistsSuccess {
    return {
        type: ACTION_TYPES.DELETE_PLAYLISTS.SUCCESS,
    };
}

export interface IDeletePlaylistsFailure extends IAction {
    message: string;
}

export function deletePlaylistsFailureFactory(message: string): IDeletePlaylistsFailure {
    return {
        type: ACTION_TYPES.DELETE_PLAYLISTS.FAILURE,
        message,
    };
}
