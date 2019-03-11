import { IPlaylist } from "../root";

export interface IRootState {
    playlists: IPlaylist[];
    currentPlaylist: IPlaylist;
}
