import axios from "axios";
import {camelKeys} from "change-object-case";
import { all, put, takeLatest } from "redux-saga/effects";
import {fenToArray} from "../common/fen";
import {ACTION_TYPES, randomMoveChallengeFailureFactory, randomMoveChallengeSuccessFactory} from "./moves.action";
import { IRandomMoveChallenge } from "./moves.domain";

// tslint:disable-next-line:no-var-requires
function* getRandomMoveChallenge() {
    try {
        const challenge: {data: any, status: number} = yield axios.get("/api/random-move-challenge");
        if (challenge.status !== 200) {
            throw new Error("Could not get response from api");
        }
        challenge.data.position = fenToArray(challenge.data.fen);
        const converted = camelKeys(challenge.data, {recursive: true, arrayRecursive: true}) as IRandomMoveChallenge;
        yield put(randomMoveChallengeSuccessFactory(converted));
    } catch (err) {
        yield put(randomMoveChallengeFailureFactory(err));
    }
}

export function* getRandomMoveChallengeSaga() {
    yield takeLatest(ACTION_TYPES.RANDOM_MOVE_CHALLENGE.REQUEST, () => {
        return getRandomMoveChallenge();
    });
}

export function* rootSaga() {
    yield all([getRandomMoveChallengeSaga()]);
}
