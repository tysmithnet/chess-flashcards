import { IAction, PlaylistType } from "../../root";
import { ACTION_TYPES, ILoadNextItemSuccess, ILoadNextPositionSuccess, ILoadPlaylistSuccess } from "./viewer.actions";
import { IRootState } from "./viewer.domain";

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
    };
}

function handleLoadNextPositionSuccess(state: IRootState, action: ILoadNextPositionSuccess): IRootState {
    return {
        ...state,
        position: action.position,
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
    }
    return {
        ...state,
    };
}
