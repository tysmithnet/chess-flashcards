export interface IRootState {
    gamePlaylists: IPlaylist[];
    openingPlaylists: IPlaylist[];
}

export interface IPlaylist {
    id: number;
    name: string;
    ids: number[];
}
