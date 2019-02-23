import { IFoundGame } from "../games";
import { IAction } from "../root";
export declare const ACTION_TYPES: {
    SEARCH_GAMES: {
        REQUEST: string;
        SUCCESS: string;
        FAILURE: string;
    };
};
export interface IGameSearchRequest extends IAction {
    query: string;
}
export declare function gameSearchRequestFactory(query: string): IGameSearchRequest;
export interface IGameSearchResult extends IAction {
    games: IFoundGame[];
}
export declare function gameSearchResultFactory(games: IFoundGame[]): IGameSearchResult;
export interface IGameSearchFailure extends IAction {
    message: string;
}
export declare function gameSearchFailureFactory(message: string): IGameSearchFailure;
