import { Opening } from "../chess-api";
import { IAction } from "../root";

export const ACTION_TYPES = {
    LOAD_OPENINGS: {
        REQUEST: "@Openings/LoadOpenings/Request",
        SUCCESS: "@Openings/LoadOpenings/Success",
        FAILURE: "@Openings/LoadOpenings/Failure",
    },
};

export interface ILoadOpeningsRequest extends IAction { }

export function loadOpeningsRequestFactory(): ILoadOpeningsRequest {
    return {
        type: ACTION_TYPES.LOAD_OPENINGS.REQUEST,
    };
}

export interface ILoadOpeningsSuccess extends IAction {
    openings: Opening[];
}

export function loadOpeningsSuccessFactory(openings: Opening[]): ILoadOpeningsSuccess {
    return {
        type: ACTION_TYPES.LOAD_OPENINGS.SUCCESS,
        openings,
    };
}

export interface ILoadOpeningsFailure extends IAction {
    message: string;
}

export function loadOpeningsFailureFactory(message: string): ILoadOpeningsFailure {
    return {
        type: ACTION_TYPES.LOAD_OPENINGS.FAILURE,
        message,
    };
}
