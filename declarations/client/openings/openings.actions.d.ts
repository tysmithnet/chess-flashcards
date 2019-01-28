import { Opening as IOpening } from "../chess-api";
import { IAction } from "../root";
export declare const ACTION_TYPES: {
    GET_ALL_OPENINGS_REQUEST: string;
    GET_ALL_OPENINGS_SUCCESS: string;
    GET_ALL_OPENINGS_FAILURE: string;
};
export interface IGetAllOpeningsRequest extends IAction {
}
export interface IGetAllOpeningsFailure extends IAction {
    message: string;
}
export interface IGetAllOpeningsSuccess extends IAction {
    payload: IOpening[];
}
export declare function getAllOpeningsRequestFactory(): IGetAllOpeningsRequest;
export declare function getAllOpeningsSuccessFactory(openings: IOpening[]): IGetAllOpeningsSuccess;
export declare function getAllOpeningsFailureFactory(error: string): IGetAllOpeningsFailure;
