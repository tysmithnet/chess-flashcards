import { IAction } from "../root";
import { ACTION_TYPES, IPlaylistMetaRequest, IPlaylistMetaSuccess } from "./playlists.actions";
import { IRootState } from "./playlists.domain";

function handlePlaylistMetaSuccess(state: IRootState, action: IPlaylistMetaSuccess): IRootState {
    return {
        ...state,
        gamePlaylistMeta: action.games,
        openingPlaylistMeta: action.openings,
    };
}

export function reducer(state: IRootState, action: IAction): IRootState {
    switch (action.type) {
        case ACTION_TYPES.PLAYLIST_META.SUCCESS:
            return handlePlaylistMetaSuccess(state, action as IPlaylistMetaSuccess);
    }
    return {
        ...state,
    };
}
