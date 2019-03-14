import { IAction, IOpeningMeta } from "../root";

export const ACTION_TYPES = {
    GET_OPENING_META: {
        REQUEST: "@openings/GetOpeningMetaRequest",
        SUCCESS: "@openings/GetOpeningMetaSuccess",
        FAILURE: "@openings/GetOpeningMetaFailure",
    },
};

export interface IGetOpeningMetaRequest extends IAction { }

export function getOpeningMetaRequestFactory(): IGetOpeningMetaRequest {
    return {
        type: ACTION_TYPES.GET_OPENING_META.REQUEST,
    };
}

export interface IGetOpeningMetaSuccess extends IAction {
    meta: IOpeningMeta[];
}

export function getOpeningMetaSuccessFactory(meta: IOpeningMeta[]): IGetOpeningMetaSuccess {
    return {
        type: ACTION_TYPES.GET_OPENING_META.SUCCESS,
        meta,
    };
}

export interface IGetOpeningMetaFailure extends IAction {
    message: string;
}

export function getOpeningMetaFailureFactory(message: string): IGetOpeningMetaFailure {
    return {
        type: ACTION_TYPES.GET_OPENING_META.FAILURE,
        message,
    };
}
