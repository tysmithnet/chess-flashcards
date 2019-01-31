import axios from "axios";
import {camelArray, camelKeys} from "change-object-case";
import { all, call, put, takeLatest } from "redux-saga/effects";
import {Configuration, DefaultApi, DefaultApiFactory, Opening as IOpening, OpeningMeta as IOpeningMeta } from "../chess-api";
import { ACTION_TYPES, getAllOpeningsFailureFactory, getAllOpeningsSuccessFactory, getOpeningDetailSuccessFactory, IGetAllOpeningsRequest, IGetOpeningDetailRequest } from "./openings.actions";

const api = DefaultApiFactory();
function* getAllOpenings() {
    try {
        const openings = yield call(api.openingsGet); // todo: cache
        const converted = camelArray(openings, {recursive: true, arrayRecursive: true}) as IOpeningMeta[];
        yield put(getAllOpeningsSuccessFactory(converted));
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
        const openings = yield call(api.openingsIdGet, id); // todo: cache
        const converted = camelKeys(openings, {recursive: true, arrayRecursive: true}) as IOpening;
        yield put(getOpeningDetailSuccessFactory(converted));
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
    yield all([getAllOpeningsSaga(), getOpeningDetailSaga()]);
}
