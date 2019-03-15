import { IAction, IPlaylist, PlaylistType } from "../../root";

export const ACTION_TYPES = {
    GET_PLAYLIST: {
        REQUEST: "@playlists.master-list/GetPlaylistRequest",
        SUCCESS: "@playlists.master-list/GetPlaylistSuccess",
        FAILURE: "@playlists.master-list/GetPlaylistFailure",
    },
    VIEW_PLAYLIST: {
        REQUEST: "@playlists.master-list/ViewPlaylistRequest",
        SUCCESS: "@playlists.master-list/ViewPlaylistSuccess",
        FAILURE: "@playlists.master-list/ViewPlaylistFailure",
    },
    CREATE_PLAYLIST: {
        REQUEST: "@playlists.master-list/CreatePlaylistRequest",
        SUCCESS: "@playlists.master-list/CreatePlaylistSuccess",
        FAILURE: "@playlists.master-list/CreatePlaylistFailure",
    },
    UPDATE_PLAYLIST: {
        REQUEST: "@playlists.master-list/UpdatePlaylistRequest",
        SUCCESS: "@playlists.master-list/UpdatePlaylistSuccess",
        FAILURE: "@playlists.master-list/UpdatePlaylistFailure",
    },
    DELETE_PLAYLISTS: {
        REQUEST: "@playlists.master-list/DeletePlaylistsRequest",
        SUCCESS: "@playlists.master-list/DeletePlaylistsSuccess",
        FAILURE: "@playlists.master-list/DeletePlaylistsFailure",
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

export function getPlaylistFailureFactory(message: string): IGetPlaylistFailure {
    return {
        type: ACTION_TYPES.GET_PLAYLIST.FAILURE,
        message,
    };
}

export interface IViewPlaylistRequest extends IAction {
    playlist: IPlaylist;
}

export function viewPlaylistRequestFactory(playlist: IPlaylist): IViewPlaylistRequest {
    return {
        type: ACTION_TYPES.VIEW_PLAYLIST.REQUEST,
        playlist,
    };
}

export interface IViewPlaylistSuccess extends IAction { }

export function viewPlaylistSuccessFactory(): IViewPlaylistSuccess {
    return {
        type: ACTION_TYPES.VIEW_PLAYLIST.SUCCESS,
    };
}

export interface IViewPlaylistFailure extends IAction {
    message: string;
}

export function viewPlaylistFailureFactory(message: string): IViewPlaylistFailure {
    return {
        type: ACTION_TYPES.VIEW_PLAYLIST.FAILURE,
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
