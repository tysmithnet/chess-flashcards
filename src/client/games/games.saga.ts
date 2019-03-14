import axios from "axios";
import { camelArray } from "change-object-case";
import { all, put, takeLatest } from "redux-saga/effects";
import { IOpeningMeta } from "../root";
import { ACTION_TYPES, getGameMetaFailureFactory, getGameMetaSuccessFactory } from "./games.actions";

function* getGameMeta() {
    try {
        const res = yield axios.get("/api/game/meta");
        const data = yield res.data;
        const converted = camelArray(data) as IOpeningMeta[];
        yield put(getGameMetaSuccessFactory(converted));
    } catch (err) {
        yield put(getGameMetaFailureFactory(err));
    }
}

function* getGameMetaSaga() {
    yield takeLatest(ACTION_TYPES.GET_GAME_META.REQUEST, getGameMeta);
}

export function* rootSaga() {
    return all([getGameMetaSaga()]);
}
