import { Theme } from "@material-ui/core";
import { RouterState } from "connected-react-router";
import { History, Location } from "history";
import { match } from "react-router";
import { Dispatch } from "redux";
import { IRootState as IAppState } from "../app";
import { IRootState as IAuthState } from "../auth";
import { IRootState as IGameState } from "../games";
import { IRootState as IHomeState } from "../home";
import { IRootState as IOpeningsState } from "../openings";
import { IRootState as IPlaylistsState } from "../playlists";
export interface IRootState {
    app: IAppState;
    auth: IAuthState;
    games: IGameState;
    home: IHomeState;
    playlists: IPlaylistsState;
    openings: IOpeningsState;
    router: RouterState;
}
export interface IBaseProps {
    dispatch?: Dispatch;
    createWorker?: () => Worker;
    theme?: Theme;
}
export interface IRoutedProps {
    history: History;
    location: Location;
    match: match;
}
export interface IPosition {
    pieces: string;
    turn: boolean;
    whiteCanCastleKingside: boolean;
    whiteCanCastleQueenside: boolean;
    blackCanCastleKingside: boolean;
    blackCanCastleQueenside: boolean;
    enPassantSquare: number;
    halfmoveClock: number;
    fullmoveNumber: number;
    isCheck: boolean;
    isCheckmate: boolean;
    isStalemate: boolean;
}
export interface IOpening {
    id: number;
    slug: string;
    eco: string;
    name: string;
    positions: IPosition[];
}
export interface IGameMeta {
    id: number;
    slug: string;
    name: string;
    numMoves: number;
}
export interface IOpeningMeta {
    id: number;
    slug: string;
    eco: string;
    name: string;
    numMoves: number;
}
export interface IGame {
    id: number;
    slug: string;
    headers: Map<string, string>;
    positions: IPosition[];
}
export interface IMove {
    src: string;
    dst: string;
}
export declare enum PlaylistType {
    opening = "opening",
    game = "game"
}
export interface IPlaylist {
    id: number;
    type: PlaylistType;
    name: string;
    ids: number[];
}
export declare const EMPTY_BOARD: any[];
export declare const STARTING_POSITION: string[];
export declare function convertSquare(square: string | number | number[]): {
    s: string;
    i: number;
    c: number[];
};
export declare function applyMove(position: string[], move: IMove): string[];
