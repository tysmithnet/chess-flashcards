import { IAction } from "../root";

export const ACTION_TYPES = {
    OPENING_REPORT: {
        REQUEST: "@home/OpeningReportRequest",
        SUCCESS: "@home/OpeningReportSuccess",
        FAILURE: "@home/OpeningReportFailure",
    },
};

export interface IOpeningReportRequest extends IAction {}
export function openingReportRequestFactory(): IOpeningReportRequest {
    return {
        type: ACTION_TYPES.OPENING_REPORT.REQUEST,
    };
}
export interface IOpeningReportSuccess extends IAction {}
export function openingReportSuccessFactory(): IOpeningReportSuccess {
    return {
        type: ACTION_TYPES.OPENING_REPORT.SUCCESS,
    };
}
export interface IOpeningReportFailure extends IAction {
    message: string;
}
export function openingReportFailureFactory(message: string): IOpeningReportFailure {
    return {
        type: ACTION_TYPES.OPENING_REPORT.FAILURE,
        message,
    };
}
