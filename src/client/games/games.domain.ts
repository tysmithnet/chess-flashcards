import { IGame, IGameMeta } from "../root";

export interface IRootState {
    meta: IGameMeta[];
    games: IGame[];
}
