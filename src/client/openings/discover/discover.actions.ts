import { Move as IMove, Opening as IOpening } from "../../chess-api";
import { IAction } from "../../root";

export const ACTION_TYPES = {
    // make moves
    MAKE_MOVES_REQUEST: "@openings/discover/MakeMovesRequest",
    MAKE_MOVES_SUCCESS: "@openings/discover/MakeMovesSuccess",
    MAKE_MOVES_FAILURE: "@openings/discover/MakeMovesFailure",

    // match openings
    MATCH_OPENINGS_REQUEST: "@openings/discover/MatchOpeningsRequest",
    MATCH_OPENINGS_SUCCESS: "@openings/discover/MatchOpeningsSuccess",
    MATCH_OPENINGS_FAILURE: "@openings/discover/MatchOpeningsFailure",
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

export interface IMatchOpeningsRequest extends IAction {
    fen: string;
}

export function matchOpeningsRequestFactory(fen: string): IMatchOpeningsRequest {
    return {
        fen,
        type: ACTION_TYPES.MATCH_OPENINGS_REQUEST,
    };
}

export interface IMatchOpeningsFailure extends IAction {
    err: string;
}

export function matchOpeningsFailureFactory(err: string): IMatchOpeningsFailure {
    return {
        err,
        type: ACTION_TYPES.MATCH_OPENINGS_FAILURE,
    };
}

export interface IMatchOpeningsSuccess extends IAction {
    openings: IOpening[];
}

export function matchOpeningsSuccessFactory(openings: IOpening[]): IMatchOpeningsSuccess {
    return {
        type: ACTION_TYPES.MATCH_OPENINGS_SUCCESS,
        openings,
    };
}
