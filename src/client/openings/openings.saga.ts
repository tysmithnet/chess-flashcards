import axios from "axios";
import {camelArray, camelKeys} from "change-object-case";
import { all, call, put, takeLatest } from "redux-saga/effects";
import {Configuration, DefaultApi, DefaultApiFactory, Opening as IOpening } from "../chess-api";
import {rootSaga as discoverSaga} from "./discover";
import { ACTION_TYPES, getAllOpeningsFailureFactory, getAllOpeningsSuccessFactory, getOpeningDetailSuccessFactory, IGetAllOpeningsRequest, IGetOpeningDetailRequest } from "./openings.actions";

// tslint:disable-next-line:no-var-requires
const openingsJson = require("../openings.json");
const api = DefaultApiFactory();
function* getAllOpenings() {
    try {
        const converted = camelArray(openingsJson, {recursive: true, arrayRecursive: true}) as IOpening[];
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
    yield all([getAllOpeningsSaga(), getOpeningDetailSaga(), discoverSaga()]);
}
