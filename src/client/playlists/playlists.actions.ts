import { IAction } from "../root";
import { IPlaylistMeta } from "./playlists.domain";

export const ACTION_TYPES = {
    PLAYLIST_META: {
        REQUEST: "@playlists/PlaylistMetaRequest",
        SUCCESS: "@playlists/PlaylistMetaSuccess",
        FAILURE: "@playlists/PlaylistMetaFailur",
    },
};

export interface IPlaylistMetaRequest extends IAction { }

export function playlistMetaRequestFactory(): IPlaylistMetaRequest {
    return {
        type: ACTION_TYPES.PLAYLIST_META.REQUEST,
    };
}

export interface IPlaylistMetaSuccess extends IAction {
    games: IPlaylistMeta[];
    openings: IPlaylistMeta[];
}

export function playlistMetaSuccessFactory(games: IPlaylistMeta[], openings: IPlaylistMeta[]): IPlaylistMetaSuccess {
    return {
        type: ACTION_TYPES.PLAYLIST_META.FAILURE,
        games,
        openings,
    };
}