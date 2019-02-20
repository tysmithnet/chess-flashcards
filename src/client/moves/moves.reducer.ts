import { IAction } from "../root";
import { ACTION_TYPES, IRandomMoveChallengeFailure, IRandomMoveChallengeRequest, IRandomMoveChallengeSuccess } from "./moves.action";
import { IRootState } from "./moves.domain";

function handleRandomMoveChallengeSuccess(state: IRootState, action: IRandomMoveChallengeSuccess): IRootState {
    return {
        ...state,
        challenge: {...action.payload},
    };
}

export function reducer(state: IRootState, action: IAction): IRootState {
    switch (action.type) {
        case ACTION_TYPES.RANDOM_MOVE_CHALLENGE.SUCCESS:
            return handleRandomMoveChallengeSuccess(state, action as IRandomMoveChallengeSuccess);

    }
    return { ...state };
}
