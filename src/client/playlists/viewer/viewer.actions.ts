import { IAction, IGame, IOpening, IPlaylist, IPosition, PlaylistType } from "../../root";

export const ACTION_TYPES = {
    LOAD_PLAYLIST: {
        REQUEST: "@playlists.viewer/LoadPlaylistRequest",
        SUCCESS: "@playlists.viewer/LoadPlaylistSuccess",
        FAILURE: "@playlists.viewer/LoadPlaylistFailure",
    },
    LOAD_NEXT_ITEM: {
        REQUEST: "@playlists.viewer/LoadNextItemRequest",
        SUCCESS: "@playlists.viewer/LoadNextItemSuccess",
        FAILURE: "@playlists.viewer/LoadNextItemFailure",
    },
    LOAD_NEXT_POSITION: {
        REQUEST: "@playlists.viewer/LoadNextPositionRequest",
        SUCCESS: "@playlists.viewer/LoadNextPositionSuccess",
        FAILURE: "@playlists.viewer/LoadNextPositionFailure",
    },
};

export interface ILoadPlaylistRequest extends IAction {
    playlistType: PlaylistType;
    id: number;
}

export function loadPlaylistRequestFactory(playlistType: PlaylistType, id: number): ILoadPlaylistRequest {
    return {
        type: ACTION_TYPES.LOAD_PLAYLIST.REQUEST,
        playlistType,
        id,
    };
}

export interface ILoadPlaylistSuccess extends IAction {
    playlist: IPlaylist;
}

export function loadPlaylistSuccessFactory(playlist: IPlaylist): ILoadPlaylistSuccess {
    return {
        type: ACTION_TYPES.LOAD_PLAYLIST.SUCCESS,
        playlist,
    };
}

export interface ILoadPlaylistFailure extends IAction {
    message: string;
}

export function loadPlaylistFailureFactory(message: string): ILoadPlaylistFailure {
    return {
        type: ACTION_TYPES.LOAD_PLAYLIST.FAILURE,
        message,
    };
}

export interface ILoadNextItemRequest extends IAction {
    playlist: IPlaylist;
}

export function loadNextItemRequestFactory(playlist: IPlaylist): ILoadNextItemRequest {
    return {
        type: ACTION_TYPES.LOAD_NEXT_ITEM.REQUEST,
        playlist,
    };
}

export interface ILoadNextItemSuccess extends IAction {
    opening: IOpening;
    game: IGame;
}

export function loadNextItemSuccessFactory(opening: IOpening, game: IGame): ILoadNextItemSuccess {
    return {
        type: ACTION_TYPES.LOAD_NEXT_ITEM.SUCCESS,
        opening,
        game,
    };
}

export interface ILoadNextItemFailure extends IAction {
    message: string;
}

export function loadNextItemFailureFactory(message: string): ILoadNextItemFailure {
    return {
        type: ACTION_TYPES.LOAD_NEXT_ITEM.FAILURE,
        message,
    };
}

export interface ILoadNextPositionRequest extends IAction {
    playlist: IPlaylist;
    opening: IOpening;
    game: IGame;
    currentPosition: IPosition;
}

export function loadNextPositionRequestFactory(playlist: IPlaylist, opening: IOpening, game: IGame, currentPosition: IPosition): ILoadNextPositionRequest {
    return {
        type: ACTION_TYPES.LOAD_NEXT_POSITION.REQUEST,
        playlist,
        opening,
        game,
        currentPosition,
    };
}

export interface ILoadNextPositionSuccess extends IAction {
    position: IPosition;
}

export function loadNextPositionSuccessFactory(position: IPosition): ILoadNextPositionSuccess {
    return {
        type: ACTION_TYPES.LOAD_NEXT_POSITION.SUCCESS,
        position,
    };
}

export interface ILoadNextPositionFailure extends IAction {
    message: string;
}

export function loadNextPositionFailureFactory(message: string): ILoadNextPositionFailure {
    return {
        type: ACTION_TYPES.LOAD_NEXT_POSITION.FAILURE,
        message,
    };
}
