import { IAction } from "../root";
import { IPlaylist } from "./playlists.domain";

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
    games: IPlaylist[];
    openings: IPlaylist[];
}

export function playlistMetaSuccessFactory(games: IPlaylist[], openings: IPlaylist[]): IPlaylistMetaSuccess {
    return {
        type: ACTION_TYPES.PLAYLIST_META.FAILURE,
        games,
        openings,
    };
}
