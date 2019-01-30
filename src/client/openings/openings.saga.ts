import axios from "axios";
import { all, call, put, takeLatest } from "redux-saga/effects";
import {Configuration, DefaultApi, DefaultApiFactory } from "../chess-api";

import { ACTION_TYPES, getAllOpeningsFailureFactory, getAllOpeningsSuccessFactory, IGetAllOpeningsRequest, IGetOpeningDetailRequest } from "./openings.actions";

const api = DefaultApiFactory();
function* getAllOpenings() {
    try {
        const openings = yield call(api.openingsGet); // todo: cache
        yield put(getAllOpeningsSuccessFactory(openings));
    } catch (err) {
        yield put(getAllOpeningsFailureFactory(err));
    }
}

export function* getAllOpeningsSaga() {
    yield takeLatest(ACTION_TYPES.GET_ALL_OPENINGS_REQUEST, (action: IGetAllOpeningsRequest) => {
        return getAllOpenings();
    });
}

export function* getOpeningDetail(id: string) {
    try {
        const res = yield axios.get(`/chess/api/v1/openings/${id}`);
        const result = res.data;
        yield put(getAllOpeningsSuccessFactory(result));
    } catch (err) {
        yield put(getAllOpeningsFailureFactory(err));
    }
}

export function* getOpeningDetailSaga() {
    yield takeLatest(ACTION_TYPES.GET_OPENING_DETAIL_REQUEST, (action: IGetOpeningDetailRequest) => {
        return getOpeningDetail(action.id);
    });
}

export function* rootSaga() {
    yield all([getAllOpeningsSaga()]);
}
