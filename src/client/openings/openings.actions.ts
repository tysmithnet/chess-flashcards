import { Opening as IOpening } from "../chess-api";
import { IAction } from "../root";

export const ACTION_TYPES = {
    GET_ALL_OPENINGS_REQUEST: "@openings/GetAllOpeningsRequest",
    GET_ALL_OPENINGS_SUCCESS: "@openings/GetAllOpeningsSuccess",
    GET_ALL_OPENINGS_FAILURE: "@openings/GetAllOpeningsFailure",
    GET_OPENING_DETAIL_REQUEST: "@openings/GetOpeningDetailRequest",
    GET_OPENING_DETAIL_SUCCESS: "@openings/GetOpeningDetailSuccess",
    GET_OPENING_DETAIL_FAILURE: "@openings/GetOpeningDetailFailure",
};

export interface IGetAllOpeningsRequest extends IAction { }
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

export function getAllOpeningsRequestFactory(): IGetAllOpeningsRequest {
    return {
        type: ACTION_TYPES.GET_ALL_OPENINGS_REQUEST,
    };
}

export function getAllOpeningsSuccessFactory(openings: IOpening[]): IGetAllOpeningsSuccess {
    return {
        type: ACTION_TYPES.GET_ALL_OPENINGS_SUCCESS,
        payload: openings,
    };
}

export function getAllOpeningsFailureFactory(error: string): IGetAllOpeningsFailure {
    return {
        type: ACTION_TYPES.GET_ALL_OPENINGS_FAILURE,
        message: error,
    };
}

export function getOpeningDetailRequestFactory(id: string): IGetOpeningDetailRequest {
    return {
        id,
        type: ACTION_TYPES.GET_OPENING_DETAIL_REQUEST,
    };
}

export function getOpeningDetailSuccessFactory(opening: IOpening): IGetOpeningDetailSuccess {
    return {
        type: ACTION_TYPES.GET_OPENING_DETAIL_SUCCESS,
        payload: opening,
    };
}

export function getOpeningDetailFailureFactory(error: string): IGetOpeningDetailFailure {
    return {
        type: ACTION_TYPES.GET_OPENING_DETAIL_FAILURE,
        message: error,
    };
}
