import { IAction } from "../root";
import { IRandomMoveChallenge } from "./moves.domain";

export const ACTION_TYPES = {
    RANDOM_MOVE_CHALLENGE: {
        REQUEST: "@moves/RandomMoveChallenge/Request",
        SUCCESS: "@moves/RandomMoveChallenge/Success",
        FAILURE: "@moves/RandomMoveChallenge/Failure",
    },
};

export interface IRandomMoveChallengeRequest extends IAction { }
export function randomMoveChallengeRequestFactory(): IRandomMoveChallengeRequest {
    return {
        type: ACTION_TYPES.RANDOM_MOVE_CHALLENGE.REQUEST,
    };
}
export interface IRandomMoveChallengeSuccess extends IAction {
    payload: IRandomMoveChallenge;
}
export function randomMoveChallengeSuccessFactory(challenge: IRandomMoveChallenge): IRandomMoveChallengeSuccess {
    return {
        type: ACTION_TYPES.RANDOM_MOVE_CHALLENGE.SUCCESS,
        payload: challenge,
    };
}
export interface IRandomMoveChallengeFailure extends IAction {
    message: string;
}

export function randomMoveChallengeFailureFactory(message: string): IRandomMoveChallengeFailure {
    return {
        type: ACTION_TYPES.RANDOM_MOVE_CHALLENGE.FAILURE,
        message,
    };
}
