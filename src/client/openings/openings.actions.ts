import {Opening as IOpening} from "../chess-api";
import { IAction } from "../root";

export const ACTION_TYPES = {
    GET_ALL_OPENINGS_REQUEST: "@openings/GetAllOpeningsRequest",
    GET_ALL_OPENINGS_SUCCESS: "@openings/GetAllOpeningsRequest",
    GET_ALL_OPENINGS_FAILURE: "@openings/GetAllOpeningsRequest",
};

export interface IGetAllOpeningsRequest extends IAction { }

export interface IGetAllOpeningsSuccess extends IAction {
    payload: IOpening[];
}

export function GetAllOpeningsRequestFactory(): IGetAllOpeningsRequest {
    return {
        type: ACTION_TYPES.GET_ALL_OPENINGS_REQUEST,
    };
}

export function GetAllOpeningsSuccessFactory(openings: IOpening[]): IGetAllOpeningsSuccess {
    return {
        type: ACTION_TYPES.GET_ALL_OPENINGS_SUCCESS,
        payload: openings,
    };
}
