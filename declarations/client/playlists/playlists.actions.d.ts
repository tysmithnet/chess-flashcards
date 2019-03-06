import { IAction } from "../root";
import { IPlaylistMeta } from "./playlists.domain";
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
    games: IPlaylistMeta[];
    openings: IPlaylistMeta[];
}
export declare function playlistMetaSuccessFactory(games: IPlaylistMeta[], openings: IPlaylistMeta[]): IPlaylistMetaSuccess;
