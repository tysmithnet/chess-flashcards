import { Move as IMove } from "../../chess-api";

export const ACTION_TYPES = {
    MAKE_MOVE_REQUEST: "@openings/discover/MakeMoveRequest",
    MAKE_MOVE_SUCCESS: "@openings/discover/MakeMoveRequest",
    MAKE_MOVE_FAILURE: "@openings/discover/MakeMoveRequest",
};

export interface IMakeMoveRequest {
    fen: string;
    move: IMove;
}

export interface IMakeMoveResponse {
    fen: string;
    moves: IMove[];
}

export interface IMakeMoveFailure {
    message: string;
}
