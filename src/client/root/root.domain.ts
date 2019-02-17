import { Dispatch } from "redux";
import { IRootState as IAppState } from "../app";
import { IRootState as IAuthState } from "../auth";
import { IRootState as IOpeningsState} from "../openings";

/**
 * Root of the state tree
 *
 * @export
 * @interface IRootState
 */
export interface IRootState {
    /**
     * State for the app domain
     *
     * @type {IAppState}
     * @memberof IRootState
     */
    app: IAppState;

    /**
     * State for the auth domain
     *
     * @type {IAuthState}
     * @memberof IRootState
     */
    auth: IAuthState;

    openings: IOpeningsState;
}

/**
 * Base interface for all component props
 *
 * @export
 * @interface IBaseProps
 */
export interface IBaseProps {
    /**
     * Function to dispatch actions
     *
     * @type {Dispatch}
     * @memberof IBaseProps
     */
    dispatch?: Dispatch;

    /**
     * Injection point for worker creation. Since workers are usable by any component
     * it is defined at this level.
     *
     * @memberof IBaseProps
     */
    createWorker?: () => Worker;
}

export interface IMove {
    src: string;
    dst: string;
}

export interface IOpening {
    id: string;
    ecoId: string;
    ecoName: string;
    variantName: string;
    moves: IMove[];
    moveText: string;
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
    if (square instanceof String) {
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

export function apply_move(position: string[], move: IMove): string[] {
    if (position == null || position.length !== 64) {
        throw new Error("Position must be a string array with 64 elements");
    }
    const copy = [...position];
    const from = convertSquare(move.src);
    const to = convertSquare(move.dst);
    const piece = copy[from.i];

    // castling
    if (piece.toLowerCase() === "k") {
        if (move.src === "e1") {
            if (move.dst === "g1") {
                copy[7] = null;
                copy[6] = "K";
                copy[5] = "R";
                copy[4] = null;
            } else if (move.dst === "c1") {
                copy[0] = null;
                copy[2] = "K";
                copy[3] = "R";
                copy[4] = null;
            }
        }
        if (move.src === "e8") {
            if (move.dst === "g8") {
                copy[7] = null;
                copy[6] = "k";
                copy[5] = "r";
                copy[4] = null;
            } else if (move.dst === "c8") {
                copy[0] = null;
                copy[2] = "k";
                copy[3] = "r";
                copy[4] = null;
            }
        }
    } else {
        copy[from.i] = null;
        copy[to.i] = piece;
    }
    return copy;
}
