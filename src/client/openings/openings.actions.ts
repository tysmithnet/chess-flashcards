import {Opening as IOpening, OpeningMeta as IOpeningMeta} from "../chess-api";
import { IAction } from "../root";

export const ACTION_TYPES = {
    GET_ALL_OPENINGS_REQUEST: "@openings/GetAllOpeningsRequest",
    GET_ALL_OPENINGS_SUCCESS: "@openings/GetAllOpeningsSuccess",
    GET_ALL_OPENINGS_FAILURE: "@openings/GetAllOpeningsFailure",
};

export interface IGetAllOpeningsRequest extends IAction { }
export interface IGetAllOpeningsFailure extends IAction {
    message: string;
}
export interface IGetAllOpeningsSuccess extends IAction {
    payload: IOpeningMeta[];
}

export function getAllOpeningsRequestFactory(): IGetAllOpeningsRequest {
    return {
        type: ACTION_TYPES.GET_ALL_OPENINGS_REQUEST,
    };
}

export function getAllOpeningsSuccessFactory(openings: IOpeningMeta[]): IGetAllOpeningsSuccess {
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
