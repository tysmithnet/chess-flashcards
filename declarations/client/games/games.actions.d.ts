import { IAction, IGameMeta } from "../root";
export declare const ACTION_TYPES: {
    GET_GAME_META: {
        REQUEST: string;
        SUCCESS: string;
        FAILURE: string;
    };
};
export interface IGetGameMetaRequest extends IAction {
}
export declare function getGameMetaRequestFactory(): IGetGameMetaRequest;
export interface IGetGameMetaSuccess extends IAction {
    meta: IGameMeta[];
}
export declare function getGameMetaSuccessFactory(meta: IGameMeta[]): IGetGameMetaSuccess;
export interface IGetGameMetaFailure extends IAction {
    message: string;
}
export declare function getGameMetaFailureFactory(message: string): IGetGameMetaFailure;
