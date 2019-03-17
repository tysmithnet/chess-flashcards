import { IGame, IOpening, IPlaylist, IPosition } from "../../root";

export interface IRootState {
    playlist: IPlaylist;
    opening: IOpening;
    position: IPosition;
    game: IGame;
    isLearnMovesMode: boolean;
    learnMovePositionIndex: number; // todo: this doesn't feel great
}

export enum ViewerMode {
    LearnMoves = "LearnMoves",
    MakeMoves = "MakeMoves",
}
