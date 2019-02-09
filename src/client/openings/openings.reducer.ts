import { IAction } from "../root";
import { ACTION_TYPES, ILoadOpeningsSuccess } from "./openings.action";
import { IRootState } from "./openings.domain";

function handleLoadOpeningsSuccess(state: IRootState, action: ILoadOpeningsSuccess): IRootState {
    return {
        ...state,
        openings: action.openings,
    };
}

export function reducer(state: IRootState, action: IAction): IRootState {
    switch (action.type) {
        case ACTION_TYPES.LOAD_OPENINGS.SUCCESS:
            return handleLoadOpeningsSuccess(state, action as ILoadOpeningsSuccess);

    }
    return { ...state };
}
