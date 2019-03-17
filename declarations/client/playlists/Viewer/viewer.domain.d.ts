import { IGame, IOpening, IPlaylist, IPosition } from "../../root";
export interface IRootState {
    playlist: IPlaylist;
    opening: IOpening;
    position: IPosition;
    game: IGame;
    isLearnMovesMode: boolean;
    learnMovePositionIndex: number;
    attempts: number;
    successes: number;
}
export declare enum ViewerMode {
    LearnMoves = "LearnMoves",
    MakeMoves = "MakeMoves"
}
