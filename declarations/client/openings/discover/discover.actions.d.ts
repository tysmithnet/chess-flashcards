import { Move as IMove } from "../../chess-api";
import { IAction } from "../../root";
export declare const ACTION_TYPES: {
    MAKE_MOVES_REQUEST: string;
    MAKE_MOVES_SUCCESS: string;
    MAKE_MOVES_FAILURE: string;
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
