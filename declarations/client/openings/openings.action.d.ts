import { IAction, IOpening } from "../root";
export declare const ACTION_TYPES: {
    LOAD_OPENINGS: {
        REQUEST: string;
        SUCCESS: string;
        FAILURE: string;
    };
};
export interface ILoadOpeningsRequest extends IAction {
}
export declare function loadOpeningsRequestFactory(): ILoadOpeningsRequest;
export interface ILoadOpeningsSuccess extends IAction {
    openings: IOpening[];
}
export declare function loadOpeningsSuccessFactory(openings: IOpening[]): ILoadOpeningsSuccess;
export interface ILoadOpeningsFailure extends IAction {
    message: string;
}
export declare function loadOpeningsFailureFactory(message: string): ILoadOpeningsFailure;
