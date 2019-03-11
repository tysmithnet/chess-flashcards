import { IAction } from "../root";
import { ACTION_TYPES, IGetPlaylistRequest, IGetPlaylistSuccess } from "./playlists.actions";
import { IRootState } from "./playlists.domain";

function handleGetPlaylistSuccess(state: IRootState, action: IGetPlaylistSuccess): IRootState {
    return {
        ...state,
        playlists: [...(action.opening || []), ...(action.game || [])],
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
