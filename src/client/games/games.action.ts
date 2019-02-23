import { IFoundGame } from "../games";
import { IAction, IOpening } from "../root";

export const ACTION_TYPES = {
    SEARCH_GAMES: {
        REQUEST: "@games/SearchGames/Request",
        SUCCESS: "@games/SearchGames/Success",
        FAILURE: "@games/SearchGames/Failure",
    },
};

export interface IGameSearchRequest extends IAction {
    query: string;
}

export function gameSearchRequestFactory(query: string): IGameSearchRequest {
    return {
        type: ACTION_TYPES.SEARCH_GAMES.REQUEST,
        query,
    };
}

export interface IGameSearchResult extends IAction {
    games: IFoundGame[];
}

export function gameSearchResultFactory(games: IFoundGame[]): IGameSearchResult {
    return {
        type: ACTION_TYPES.SEARCH_GAMES.SUCCESS,
        games,
    };
}

export interface IGameSearchFailure extends IAction {
    message: string;
}

export function gameSearchFailureFactory(message: string): IGameSearchFailure {
    return {
        type: ACTION_TYPES.SEARCH_GAMES.FAILURE,
        message,
    };
}
