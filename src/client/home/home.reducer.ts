import { IAction } from "../root";
import { ACTION_TYPES, IOpeningReportSuccess } from "./home.actions";
import { IRootState } from "./home.domain";

function handleOpeningReportSuccess(state: IRootState, action: IOpeningReportSuccess): IRootState {
    return {
        ...state,
    };
}

export function reducer(state: IRootState, action: IAction): IRootState {
    switch (action.type) {
        case ACTION_TYPES.OPENING_REPORT.SUCCESS:
            return handleOpeningReportSuccess(state, action as IOpeningReportSuccess);
    }
    return {
        ...state,
    };
}
