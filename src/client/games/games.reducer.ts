import { IAction } from "../root";
import { ACTION_TYPES, IGameSearchResult } from "./games.action";
import { IRootState } from "./games.domain";

function handleSearchGamesSuccess(state: IRootState, action: IGameSearchResult): IRootState {
    return {
        ...state,
        searchResults: action.games,
    };
}

export function reducer(state: IRootState, action: IAction): IRootState {
    switch (action.type) {
        case ACTION_TYPES.SEARCH_GAMES.SUCCESS:
            return handleSearchGamesSuccess(state, action as IGameSearchResult);

    }
    return { ...state };
}
