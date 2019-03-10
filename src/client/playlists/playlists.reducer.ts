import { IAction } from "../root";
import { ACTION_TYPES, IGetPlaylistRequest, IGetPlaylistSuccess } from "./playlists.actions";
import { IRootState } from "./playlists.domain";

function handleGetPlaylistSuccess(state: IRootState, action: IGetPlaylistSuccess): IRootState {
    return {
        ...state,
        gamePlaylists: action.game,
        openingPlaylists: action.opening,
    };
}

export function reducer(state: IRootState, action: IAction): IRootState {
    switch (action.type) {
        case ACTION_TYPES.GET_PLAYLIST.SUCCESS:
            return handleGetPlaylistSuccess(state, action as IGetPlaylistSuccess);
    }
    return {
        ...state,
    };
}
