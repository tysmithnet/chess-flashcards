import axios from "axios";
import { camelArray } from "change-object-case";
import { all, put, takeLatest } from "redux-saga/effects";
import { IOpeningMeta } from "../root";
import { ACTION_TYPES, getOpeningMetaSuccessFactory } from "./openings.actions";

function* getOpeningMeta() {
    try {
        const result = yield axios.get("/api/opening/meta");
        const converted = camelArray(result.data) as IOpeningMeta[];
        yield put(getOpeningMetaSuccessFactory(converted));
    } catch (err) {
        console.error(err);
    }
}

function* getOpeningMetaSaga() {
    yield takeLatest(ACTION_TYPES.GET_OPENING_META.REQUEST, getOpeningMeta);
}

export function* rootSaga() {
    yield all([getOpeningMetaSaga()]);
}
