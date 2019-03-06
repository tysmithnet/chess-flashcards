export interface IRootState {
    gamePlaylistMeta: IPlaylistMeta[];
    openingPlaylistMeta: IPlaylistMeta[];
}

export interface IPlaylistMeta {
    id: number;
    name: string;
    numItems: number;
}
