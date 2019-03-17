import { IAction, PlaylistType } from "../../root";
import { ACTION_TYPES, IChangeLearnPositionRequest, IChangeModeRequest, IGetStatsSuccess, ILoadNextItemSuccess, ILoadNextPositionSuccess, ILoadPlaylistSuccess } from "./viewer.actions";
import { IRootState, ViewerMode } from "./viewer.domain";

function  handleLoadPlaylistSuccess(state: IRootState, action: ILoadPlaylistSuccess): IRootState {
    return {
        ...state,
        playlist: action.playlist,
    };
}

function handleLoadNextItemSuccess(state: IRootState, action: ILoadNextItemSuccess): IRootState {
    return {
        ...state,
        opening: state.playlist.type === PlaylistType.opening ? action.opening : null,
        game: state.playlist.type === PlaylistType.game ? action.game : null,
        isLearnMovesMode: false,
        learnMovePositionIndex: 0,
        attempts: null,
        successes: null,
        position: null,
    };
}

function handleLoadNextPositionSuccess(state: IRootState, action: ILoadNextPositionSuccess): IRootState {
    return {
        ...state,
        position: action.position,
    };
}

function handleChangeMode(state: IRootState, action: IChangeModeRequest): IRootState {
    return {
        ...state,
        isLearnMovesMode: action.mode === ViewerMode.LearnMoves,
    };
}

function handleChangeLearnPosition(state: IRootState, action: IChangeLearnPositionRequest): IRootState {
    return {
        ...state,
        learnMovePositionIndex: action.index,
    };
}

function handleGetStats(state: IRootState, action: IGetStatsSuccess): IRootState {
    return {
        ...state,
        attempts: action.attempts,
        successes: action.successes,
    };
}

function handleReset(): IRootState {
    return {
        attempts: 0,
        game: null,
        isLearnMovesMode: false,
        learnMovePositionIndex: 0,
        opening: null,
        playlist: null,
        position: null,
        successes: 0,
    };
}

export function reducer(state: IRootState, action: IAction): IRootState {
    switch (action.type) {
        case ACTION_TYPES.LOAD_PLAYLIST.SUCCESS:
            return handleLoadPlaylistSuccess(state, action as ILoadPlaylistSuccess);
        case ACTION_TYPES.LOAD_NEXT_ITEM.SUCCESS:
            return handleLoadNextItemSuccess(state, action as ILoadNextItemSuccess);
        case ACTION_TYPES.LOAD_NEXT_POSITION.SUCCESS:
            return handleLoadNextPositionSuccess(state, action as ILoadNextPositionSuccess);
        case ACTION_TYPES.CHANGE_MODE:
            return handleChangeMode(state, action as IChangeModeRequest);
        case ACTION_TYPES.CHANGE_LEARN_POSITION:
            return handleChangeLearnPosition(state, action as IChangeLearnPositionRequest);
        case ACTION_TYPES.GET_STATS.SUCCESS:
            return handleGetStats(state, action as IGetStatsSuccess);
        case ACTION_TYPES.RESET:
            return handleReset();
    }
    return {
        ...state,
    };
}
