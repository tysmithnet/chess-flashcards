import { Theme } from "@material-ui/core";
import { RouterState } from "connected-react-router";
import { History, Location } from "history";
import { match } from "react-router";
import { Dispatch } from "redux";
import { IRootState as IAppState } from "../app";
import { IRootState as IAuthState } from "../auth";
import { IRootState as IGameState } from "../games";
import { IRootState as IOpeningsState } from "../openings";
import { IRootState as IPlaylistsState } from "../playlists";

export interface IRootState {
    app: IAppState;
    auth: IAuthState;
    games: IGameState;
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

export enum PlaylistType {
    opening = "opening",
    game = "game",
}

export interface IPlaylist {
    id: number;
    type: PlaylistType;
    name: string;
    ids: number[];
}

export const EMPTY_BOARD = new Array(64);

export const STARTING_POSITION = [
    "R", "N", "B", "Q", "K", "B", "N", "R",
    "P", "P", "P", "P", "P", "P", "P", "P",
    null, null, null, null, null, null, null, null,
    null, null, null, null, null, null, null, null,
    null, null, null, null, null, null, null, null,
    null, null, null, null, null, null, null, null,
    "p", "p", "p", "p", "p", "p", "p", "p",
    "r", "n", "b", "q", "k", "b", "n", "r",
];

export function convertSquare(square: string | number | number[]): { s: string, i: number, c: number[] } {
    const res = {
        s: "",
        i: 0,
        c: [] as number[],
    };
    if (typeof (square) === "string") {
        res.s = square as string;
        const col = square.charCodeAt(0) - 97;
        const row = parseInt(square.charAt(1), 10) - 1;
        const index = (row * 8) + col;
        res.i = index;
        res.c = [row, col];
    }
    if (typeof (square) === "number") {
        const row = Math.floor(square / 8);
        const col = square % 8;
        const index = (row * 8) + col;
        const alg = `${String.fromCharCode(97 + col)}${row + 1}`;
        res.s = alg;
        res.i = index;
        res.c = [row, col];
    }
    if (Array.isArray(square)) {
        res.c = square as number[];
        res.i = (square[0] * 64) + square[1];
        res.s = `${String.fromCharCode(97 + square[1])}${square[0] + 1}`;
    }
    return res;
}

export function applyMove(position: string[], move: IMove): string[] {
    if (position == null || position.length !== 64) {
        throw new Error("Position must be a string array with 64 elements");
    }
    const copy = [...position];
    const from = convertSquare(move.src);
    const to = convertSquare(move.dst);
    const piece = copy[from.i];
    if (!piece) {
        throw new Error("Move attempted to be made where no piece exists");
    }

    // castling
    let handled = false;
    if (piece.toLowerCase() === "k") {
        if (move.src === "e1") {
            if (move.dst === "g1") {
                copy[7] = null;
                copy[6] = "K";
                copy[5] = "R";
                copy[4] = null;
                handled = true;
            } else if (move.dst === "c1") {
                copy[0] = null;
                copy[2] = "K";
                copy[3] = "R";
                copy[4] = null;
                handled = true;
            }
        }
        if (move.src === "e8") {
            if (move.dst === "g8") {
                copy[56 + 7] = null;
                copy[56 + 6] = "k";
                copy[56 + 5] = "r";
                copy[56 + 4] = null;
                handled = true;
            } else if (move.dst === "c8") {
                copy[56 + 0] = null;
                copy[56 + 2] = "k";
                copy[56 + 3] = "r";
                copy[56 + 4] = null;
                handled = true;
            }
        }
    }
    if (!handled) {
        copy[from.i] = null;
        copy[to.i] = piece;
    }
    return copy;
}
