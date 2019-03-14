import { IAction } from "../root";
import { ACTION_TYPES, IGetGameMetaSuccess } from "./games.actions";
import { IRootState } from "./games.domain";

function handleGetGameMetaSuccess(state: IRootState, action: IGetGameMetaSuccess): IRootState {
    return {
        ...state,
    };
}

export function reducer(state: IRootState, action: IAction): IRootState {
    switch (action.type) {
        case ACTION_TYPES.GET_GAME_META.SUCCESS:
            return handleGetGameMetaSuccess(state, action as IGetGameMetaSuccess);
    }
    return {
        ...state,
    };
}
