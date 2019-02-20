import { Dispatch } from "redux";
import { IRootState as IAppState } from "../app";
import { IRootState as IAuthState } from "../auth";
import { IRootState as IMoveState } from "../moves";
import { IRootState as IOpeningsState } from "../openings";
export interface IRootState {
    app: IAppState;
    auth: IAuthState;
    openings: IOpeningsState;
    moves: IMoveState;
}
export interface IBaseProps {
    dispatch?: Dispatch;
    createWorker?: () => Worker;
}
export interface IMove {
    src: string;
    dst: string;
    is_whites_move?: boolean;
    is_capture?: boolean;
    is_check?: boolean;
    is_checkmate?: boolean;
    is_stalemate?: boolean;
    is_castle?: boolean;
    is_enpassant?: boolean;
    is_insufficient_material?: boolean;
}
export interface IOpening {
    id: string;
    ecoId: string;
    ecoName: string;
    variantName: string;
    moves: IMove[];
    moveText: string;
}
export declare const EMPTY_BOARD: any[];
export declare const STARTING_POSITION: string[];
export declare function convertSquare(square: string | number | number[]): {
    s: string;
    i: number;
    c: number[];
};
export declare function applyMove(position: string[], move: IMove): string[];
