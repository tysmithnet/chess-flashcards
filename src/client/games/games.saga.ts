import axios from "axios";
import { all, put, takeLatest } from "redux-saga/effects";
import { ACTION_TYPES, gameSearchResultFactory, IGameSearchRequest } from "./games.action";

function* searchForGames(action: IGameSearchRequest) {
    try {
        const results = yield axios.get("/api/search/games", {
            data: {
                q: action.query,
            },
        });
        yield put(gameSearchResultFactory(results.data));
    } catch (error) {
        console.log(error);
    }
}

function* gameSearchSaga() {
    yield takeLatest(ACTION_TYPES.SEARCH_GAMES.REQUEST, (action: IGameSearchRequest) => {
        return searchForGames(action);
    });
}

export function* rootSaga() {
    yield all([gameSearchSaga()]);
}
