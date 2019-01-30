import { IAction } from "../root";
import { ACTION_TYPES, IGetAllOpeningsSuccess } from "./openings.actions";
import { IRootState } from "./openings.domain";

/**
 * Apply the changes resulting from a successful login
 * @param state Current state
 * @param loginSuccess Login success message
 */
function handleGetAllOpeningsSuccess(
    state: IRootState,
    getAllOpeningsSuccess: IGetAllOpeningsSuccess,
): IRootState {
    return {
        ...state,
        openingMetaData: getAllOpeningsSuccess.payload,
    };
}

/**
 * Reducer for the Auth domain
 * @param state Current state
 * @param action Action to apply
 */
export function reducer(state: IRootState, action: IAction): IRootState {
    switch (action.type) {
        case ACTION_TYPES.GET_ALL_OPENINGS_SUCCESS:
            return handleGetAllOpeningsSuccess(state, action as IGetAllOpeningsSuccess);
    }
    return { ...state };
}
