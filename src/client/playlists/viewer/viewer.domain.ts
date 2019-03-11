import { IGame, IOpening, IPlaylist, IPosition } from "../../root";

export interface IRootState {
    playlist: IPlaylist;
    opening: IOpening;
    position: IPosition;
    game: IGame;
}
