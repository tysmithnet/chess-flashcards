import { IAction, IGame, IMove, IOpening, IPlaylist, IPosition, PlaylistType } from "../../root";

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
    CHECK_MOVE: {
        REQUEST: "@playlists.viewer/CheckMoveRequest",
        SUCCESS: "@playlists.viewer/CheckMoveSuccess",
        FAILURE: "@playlists.viewer/CheckMoveFailure",
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
}

export function loadNextItemRequestFactory(): ILoadNextItemRequest {
    return {
        type: ACTION_TYPES.LOAD_NEXT_ITEM.REQUEST,
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
}

export function loadNextPositionRequestFactory(): ILoadNextPositionRequest {
    return {
        type: ACTION_TYPES.LOAD_NEXT_POSITION.REQUEST,
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

export interface ICheckMoveRequest extends IAction {
    move: IMove;
}

export function checkMoveRequestFactory(move: IMove): ICheckMoveRequest {
    return {
        type: ACTION_TYPES.CHECK_MOVE.REQUEST,
        move,
    };
}

export interface ICheckMoveSuccess extends IAction {
    move: IMove;
    success: boolean;
}

export function checkMoveSuccessFactory(move: IMove, success: boolean): ICheckMoveSuccess {
    return {
        type: ACTION_TYPES.CHECK_MOVE.SUCCESS,
        move,
        success,
    };
}

export interface ICheckMoveFailure extends IAction {
    message: string;
}

export function checkMoveFailureFactory(message: string): ICheckMoveFailure {
    return {
        type: ACTION_TYPES.CHECK_MOVE.FAILURE,
        message,
    };
}
