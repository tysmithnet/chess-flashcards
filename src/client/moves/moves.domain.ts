import { IMove } from "../root";

export interface IRootState {
    challenge: IRandomMoveChallenge;
}

export interface IRandomMoveChallenge {
    position: string[];
    moves: IMove[];
}
