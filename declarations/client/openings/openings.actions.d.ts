import { Opening as IOpening } from "../chess-api";
import { IAction } from "../root";
export declare const ACTION_TYPES: {
    GET_ALL_OPENINGS_REQUEST: string;
    GET_ALL_OPENINGS_SUCCESS: string;
    GET_ALL_OPENINGS_FAILURE: string;
    GET_OPENING_DETAIL_REQUEST: string;
    GET_OPENING_DETAIL_SUCCESS: string;
    GET_OPENING_DETAIL_FAILURE: string;
};
export interface IGetAllOpeningsRequest extends IAction {
}
export interface IGetAllOpeningsFailure extends IAction {
    message: string;
}
export interface IGetAllOpeningsSuccess extends IAction {
    payload: IOpening[];
}
export interface IGetOpeningDetailRequest extends IAction {
    id: string;
}
export interface IGetOpeningDetailFailure extends IAction {
    message: string;
}
export interface IGetOpeningDetailSuccess extends IAction {
    payload: IOpening;
}
export declare function getAllOpeningsRequestFactory(): IGetAllOpeningsRequest;
export declare function getAllOpeningsSuccessFactory(openings: IOpening[]): IGetAllOpeningsSuccess;
export declare function getAllOpeningsFailureFactory(error: string): IGetAllOpeningsFailure;
export declare function getOpeningDetailRequestFactory(id: string): IGetOpeningDetailRequest;
export declare function getOpeningDetailSuccessFactory(opening: IOpening): IGetOpeningDetailSuccess;
export declare function getOpeningDetailFailureFactory(error: string): IGetOpeningDetailFailure;
