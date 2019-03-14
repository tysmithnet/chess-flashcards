import { IAction, IGameMeta } from "../root";

export const ACTION_TYPES = {
    GET_GAME_META: {
        REQUEST: "@games/GetGameMetaRequest",
        SUCCESS: "@games/GetGameMetaSuccess",
        FAILURE: "@games/GetGameMetaFailure",
    },
};

export interface IGetGameMetaRequest extends IAction { }

export function getGameMetaRequestFactory(): IGetGameMetaRequest {
    return {
        type: ACTION_TYPES.GET_GAME_META.REQUEST,
    };
}

export interface IGetGameMetaSuccess extends IAction {
    meta: IGameMeta[];
}

export function getGameMetaSuccessFactory(meta: IGameMeta[]): IGetGameMetaSuccess {
    return {
        type: ACTION_TYPES.GET_GAME_META.SUCCESS,
        meta,
    };
}

export interface IGetGameMetaFailure extends IAction {
    message: string;
}

export function getGameMetaFailureFactory(message: string): IGetGameMetaFailure {
    return {
        type: ACTION_TYPES.GET_GAME_META.FAILURE,
        message,
    };
}
