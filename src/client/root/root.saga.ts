import { all } from "redux-saga/effects";
import { rootSaga as auth } from "../auth/auth.saga";

/**
 * Root of the saga tree
 */
export function* rootSaga() {
    yield all([auth()]);
}
