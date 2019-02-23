import { all } from "redux-saga/effects";
import { rootSaga as auth } from "../auth/auth.saga";
import { rootSaga as games} from "../games";
import { rootSaga as moves } from "../moves";
import { rootSaga as openings } from "../openings";

/**
 * Root of the saga tree
 */
export function* rootSaga() {
    yield all([auth(), openings(), moves(), games()]);
}
