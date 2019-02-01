import { Move as IMove } from "../../chess-api";
import { IAction } from "../../root";

export const ACTION_TYPES = {
    MAKE_MOVES_REQUEST: "@openings/discover/MakeMovesRequest",
    MAKE_MOVES_SUCCESS: "@openings/discover/MakeMovesSuccess",
    MAKE_MOVES_FAILURE: "@openings/discover/MakeMovesFailure",
};

export interface IMakeMovesRequest extends IAction {
    fen: string;
    moves: IMove[];
}

export function makeMovesRequestFactory(fen: string, moves: IMove[]): IMakeMovesRequest {
    return {
        type: ACTION_TYPES.MAKE_MOVES_REQUEST,
        fen,
        moves,
    };
}

export interface IMakeMovesSuccess extends IAction {
    fen: string; // next fen
    moves: IMove[]; // next legal moves
}

export function makeMovesSuccessFactory(fen: string, moves: IMove[]): IMakeMovesSuccess {
    return {
        type: ACTION_TYPES.MAKE_MOVES_SUCCESS,
        fen,
        moves,
    };
}

export interface IMakeMovesFailure extends IAction {
    message: string;
}

export function makeMovesFailureFactory(message: string): IMakeMovesFailure {
    return {
        type: ACTION_TYPES.MAKE_MOVES_FAILURE,
        message,
    };
}
