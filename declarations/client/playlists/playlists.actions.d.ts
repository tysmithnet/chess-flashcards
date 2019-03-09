import { IAction } from "../root";
import { IPlaylist } from "./playlists.domain";
export declare const ACTION_TYPES: {
    PLAYLIST_META: {
        REQUEST: string;
        SUCCESS: string;
        FAILURE: string;
    };
};
export interface IPlaylistMetaRequest extends IAction {
}
export declare function playlistMetaRequestFactory(): IPlaylistMetaRequest;
export interface IPlaylistMetaSuccess extends IAction {
    games: IPlaylist[];
    openings: IPlaylist[];
}
export declare function playlistMetaSuccessFactory(games: IPlaylist[], openings: IPlaylist[]): IPlaylistMetaSuccess;
