export interface IRootState {
    gamePlaylistMeta: IPlaylist[];
    openingPlaylistMeta: IPlaylist[];
}

export interface IPlaylist {
    id: number;
    name: string;
    ids: number[];
}
