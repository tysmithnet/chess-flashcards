import { all } from "redux-saga/effects";
import { rootSaga as auth } from "../auth/auth.saga";
import { rootSaga as openings } from "../openings/openings.saga";

/**
 * Root of the saga tree
 */
export function* rootSaga() {
    yield all([auth(), openings()]);
}
