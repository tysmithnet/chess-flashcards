import { all } from "redux-saga/effects";
import { rootSaga as auth } from "../auth/auth.saga";
import { rootSaga as games } from "../games";
import { rootSaga as home } from "../home";
import { rootSaga as openings } from "../openings";
import { rootSaga as playlists } from "../playlists";

/**
 * Root of the saga tree
 */
export function* rootSaga() {
    yield all([auth(), games(), home(), openings(), playlists()]);
}
