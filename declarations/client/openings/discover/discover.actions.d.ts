import { Move as IMove, Opening as IOpening } from "../../chess-api";
import { IAction } from "../../root";
export declare const ACTION_TYPES: {
    MAKE_MOVES_REQUEST: string;
    MAKE_MOVES_SUCCESS: string;
    MAKE_MOVES_FAILURE: string;
    MATCH_OPENINGS_REQUEST: string;
    MATCH_OPENINGS_SUCCESS: string;
    MATCH_OPENINGS_FAILURE: string;
};
export interface IMakeMovesRequest extends IAction {
    fen: string;
    moves: IMove[];
}
export declare function makeMovesRequestFactory(fen: string, moves: IMove[]): IMakeMovesRequest;
export interface IMakeMovesSuccess extends IAction {
    fen: string;
    moves: IMove[];
}
export declare function makeMovesSuccessFactory(fen: string, moves: IMove[]): IMakeMovesSuccess;
export interface IMakeMovesFailure extends IAction {
    message: string;
}
export declare function makeMovesFailureFactory(message: string): IMakeMovesFailure;
export interface IMatchOpeningsRequest extends IAction {
    fen: string;
}
export declare function matchOpeningsRequestFactory(fen: string): IMatchOpeningsRequest;
export interface IMatchOpeningsFailure extends IAction {
    err: string;
}
export declare function matchOpeningsFailureFactory(err: string): IMatchOpeningsFailure;
export interface IMatchOpeningsSuccess extends IAction {
    openings: IOpening[];
}
export declare function matchOpeningsSuccessFactory(openings: IOpening[]): IMatchOpeningsSuccess;
