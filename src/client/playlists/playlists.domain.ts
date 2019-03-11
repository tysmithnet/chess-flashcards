import { IPlaylist } from "../root";

export interface IRootState {
    gamePlaylists: IPlaylist[];
    openingPlaylists: IPlaylist[];
}
