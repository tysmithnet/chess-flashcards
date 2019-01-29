import axios from "axios";
import { all, put, takeLatest } from "redux-saga/effects";
import { ACTION_TYPES, getAllOpeningsFailureFactory, getAllOpeningsSuccessFactory, IGetAllOpeningsRequest } from "./openings.actions";

function* getAllOpenings() {
    try {
        const cachedData = localStorage.getItem(ACTION_TYPES.GET_ALL_OPENINGS_REQUEST);
        if (cachedData) {
            const inflated = JSON.parse(cachedData);
            yield put(getAllOpeningsSuccessFactory(inflated));
        } else {
            const res = yield axios.get("/chess/api/v1/openings");
            const result = yield res.data;
            localStorage.setItem(ACTION_TYPES.GET_ALL_OPENINGS_REQUEST, JSON.stringify(res.data));
            yield put(getAllOpeningsSuccessFactory(result));
        }
    } catch (err) {
        yield put(getAllOpeningsFailureFactory(err));
    }
}

export function* getAllOpeningsSaga() {
    yield takeLatest(ACTION_TYPES.GET_ALL_OPENINGS_REQUEST, (action: IGetAllOpeningsRequest) => {
        return getAllOpenings();
    });
}

export function* rootSaga() {
    yield all([getAllOpeningsSaga()]);
}
