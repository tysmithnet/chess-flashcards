import { IAction } from "../../root";
import { ACTION_TYPES, IMakeMovesRequest, IMakeMovesSuccess} from "./discover.actions";
import { IRootState } from "./discover.domain";

export function handleMakeMovesSuccess(state: IRootState, action: IMakeMovesSuccess): IRootState {
    return {
        ...state,
        fen: action.fen,
        legalMoves: action.moves,
    };
}

export function reducer(state: IRootState, action: IAction): IRootState {
    switch (action.type) {
        case ACTION_TYPES.MAKE_MOVES_SUCCESS:
            return handleMakeMovesSuccess(state, action as IMakeMovesSuccess);
    }
    return { ...state };
}
