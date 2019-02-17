import { Dispatch } from "redux";
import { IRootState as IAppState } from "../app";
import { IRootState as IAuthState } from "../auth";
import { IRootState as IOpeningsState } from "../openings";
export interface IRootState {
    app: IAppState;
    auth: IAuthState;
    openings: IOpeningsState;
}
export interface IBaseProps {
    dispatch?: Dispatch;
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
export declare const EMPTY_BOARD: any[];
export declare const STARTING_POSITION: string[];
export declare function convertSquare(square: string | number | number[]): {
    s: string;
    i: number;
    c: number[];
};
export declare function applyMove(position: string[], move: IMove): string[];
