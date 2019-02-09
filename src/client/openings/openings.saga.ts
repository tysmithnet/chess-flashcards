import axios from "axios";
import {camelArray, camelKeys} from "change-object-case";
import { all, call, put, takeLatest } from "redux-saga/effects";
import {Configuration, DefaultApi, DefaultApiFactory, Opening as IOpening } from "../chess-api";
import {ACTION_TYPES, ILoadOpeningsRequest, loadOpeningsFailureFactory, loadOpeningsSuccessFactory} from "./openings.action";

// tslint:disable-next-line:no-var-requires
const openingsJson = require("../openings.json");
const api = DefaultApiFactory();
function* getAllOpenings() {
    try {
        const converted = camelArray(openingsJson, {recursive: true, arrayRecursive: true}) as IOpening[];
        yield put(loadOpeningsSuccessFactory(converted));
    } catch (err) {
        yield put(loadOpeningsFailureFactory(err));
    }
}

export function* getAllOpeningsSaga() {
    yield takeLatest(ACTION_TYPES.LOAD_OPENINGS.REQUEST, (action: ILoadOpeningsRequest) => {
        return getAllOpenings();
    });
}

export function* rootSaga() {
    yield all([getAllOpeningsSaga()]);
}
