import { IAction, IGame, IMove, IOpening, IPlaylist, IPosition, PlaylistType } from "../../root";
import { ViewerMode } from "./viewer.domain";

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
    GET_STATS: {
        REQUEST: "@playlists.viewer/GetStatsRequest",
        SUCCESS: "@playlists.viewer/GetStatsSuccess",
        FAILURE: "@playlists.viewer/GetStatsFailure",
    },
    RESET: "@playlists.viewer/Reset",
    CHANGE_MODE: "@playlists.viewer/ChangeMode",
    CHANGE_LEARN_POSITION: "@playlists.viewer/ChangeLearnPosition",
    SET_MOVE_POSITION: "@playlists.viewer/SetMovePosition",
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

export interface IChangeLearnPositionRequest extends IAction {
    index: number;
}

export function changeLearnPositionRequestFactory(index: number): IChangeLearnPositionRequest {
    return {
        type: ACTION_TYPES.CHANGE_LEARN_POSITION,
        index,
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

export interface IChangeModeRequest extends IAction {
    mode: ViewerMode;
}

export function changeModeRequestFactory(mode: ViewerMode): IChangeModeRequest {
    return {
        type: ACTION_TYPES.CHANGE_MODE,
        mode,
    };
}

export interface IGetStatsRequest extends IAction {
    playlistType: PlaylistType;
    id: number;
}

export function getStatsRequestFactory(playlistType: PlaylistType, id: number): IGetStatsRequest {
    return {
        type: ACTION_TYPES.GET_STATS.REQUEST,
        playlistType,
        id,
    };
}

export interface IGetStatsSuccess extends IAction {
    attempts: number;
    successes: number;
}

export function getStatsSuccessFactory(attempts: number, successes: number): IGetStatsSuccess {
    return {
        type: ACTION_TYPES.GET_STATS.SUCCESS,
        attempts,
        successes,
    };
}

export interface IGetStatsFailure extends IAction {
    message: string;
}

export function getStatsFailureFactory(message: string): IGetStatsFailure {
    return {
        type: ACTION_TYPES.GET_STATS.FAILURE,
        message,
    };
}

export interface IResetRequest extends IAction { }
export function resetRequestFactory(): IResetRequest {
    return {
        type: ACTION_TYPES.RESET,
    };
}

export interface ISetMovePosition extends IAction {
    position: IPosition;
}
export function setMovePositionFactory(position: IPosition): ISetMovePosition {
    return {
        type: ACTION_TYPES.SET_MOVE_POSITION,
        position,
    };
}
