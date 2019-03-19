import { IAction } from "../root";
export declare const ACTION_TYPES: {
    OPENING_REPORT: {
        REQUEST: string;
        SUCCESS: string;
        FAILURE: string;
    };
};
export interface IOpeningReportRequest extends IAction {
}
export declare function openingReportRequestFactory(): IOpeningReportRequest;
export interface IOpeningReportSuccess extends IAction {
}
export declare function openingReportSuccessFactory(): IOpeningReportSuccess;
export interface IOpeningReportFailure extends IAction {
    message: string;
}
export declare function openingReportFailureFactory(message: string): IOpeningReportFailure;
