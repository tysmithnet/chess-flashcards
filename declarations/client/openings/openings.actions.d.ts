import { IAction, IOpeningMeta } from "../root";
export declare const ACTION_TYPES: {
    GET_OPENING_META: {
        REQUEST: string;
        SUCCESS: string;
        FAILURE: string;
    };
};
export interface IGetOpeningMetaRequest extends IAction {
}
export declare function getOpeningMetaRequestFactory(): IGetOpeningMetaRequest;
export interface IGetOpeningMetaSuccess extends IAction {
    meta: IOpeningMeta[];
}
export declare function getOpeningMetaSuccessFactory(meta: IOpeningMeta[]): IGetOpeningMetaSuccess;
