import { IAction } from "../root";
import { ACTION_TYPES, IGetOpeningMetaSuccess } from "./openings.actions";
import { IRootState } from "./openings.domain";

function handleOpeningMetaSuccess(state: IRootState, action: IGetOpeningMetaSuccess): IRootState {
    return {
        ...state,
        meta: action.meta,
    };
}

export function reducer(state: IRootState, action: IAction): IRootState {
    switch (action.type) {
        case ACTION_TYPES.GET_OPENING_META.SUCCESS:
            return handleOpeningMetaSuccess(state, action as IGetOpeningMetaSuccess);
    }
    return {
        ...state,
    };
}
