import { IGame, IOpening, IPlaylist, IPosition } from "../../root";

export interface IRootState {
    playlist: IPlaylist;
    opening: IOpening;
    position: IPosition;
    game: IGame;
    isLearnMovesMode: boolean;
    learnMovePositionIndex: number; // todo: this doesn't feel great
    attempts: number;
    successes: number;
}

export enum ViewerMode {
    LearnMoves = "LearnMoves",
    MakeMoves = "MakeMoves",
}
