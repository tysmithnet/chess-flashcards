import { IAction } from "../root";
import { IRandomMoveChallenge } from "./moves.domain";
export declare const ACTION_TYPES: {
    RANDOM_MOVE_CHALLENGE: {
        REQUEST: string;
        SUCCESS: string;
        FAILURE: string;
    };
};
export interface IRandomMoveChallengeRequest extends IAction {
}
export declare function randomMoveChallengeRequestFactory(): IRandomMoveChallengeRequest;
export interface IRandomMoveChallengeSuccess extends IAction {
    payload: IRandomMoveChallenge;
}
export declare function randomMoveChallengeSuccessFactory(challenge: IRandomMoveChallenge): IRandomMoveChallengeSuccess;
export interface IRandomMoveChallengeFailure extends IAction {
    message: string;
}
export declare function randomMoveChallengeFailureFactory(message: string): IRandomMoveChallengeFailure;
