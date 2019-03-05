import { Theme } from "@material-ui/core";
import { Dispatch } from "redux";
import { IRootState as IAppState } from "../app";
import { IRootState as IAuthState } from "../auth";
export interface IRootState {
    app: IAppState;
    auth: IAuthState;
}
export interface IBaseProps {
    dispatch?: Dispatch;
    createWorker?: () => Worker;
    theme?: Theme;
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
    ecoId: string;
    ecoName: string;
    variantName: string;
    positions: IPosition[];
}
export interface IGame {
    id: number;
    slug: string;
    headers: Map<string, string>;
    positions: IPosition[];
}
export interface IGamePlaylist {
    id: number;
    name: string;
    games: IGame[];
}
export interface IOpeningPlaylist {
    id: number;
    name: string;
    openings: IOpening[];
}
export interface IMove {
    src: string;
    dst: string;
}
export declare const EMPTY_BOARD: any[];
export declare const STARTING_POSITION: string[];
export declare function convertSquare(square: string | number | number[]): {
    s: string;
    i: number;
    c: number[];
};
export declare function applyMove(position: string[], move: IMove): string[];
