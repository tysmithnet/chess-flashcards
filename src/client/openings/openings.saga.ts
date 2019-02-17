import {camelArray} from "change-object-case";
import { all, put, takeLatest } from "redux-saga/effects";
import { IOpening } from "../root";
import {ACTION_TYPES, ILoadOpeningsRequest, loadOpeningsFailureFactory, loadOpeningsSuccessFactory} from "./openings.action";

// tslint:disable-next-line:no-var-requires
const openingsJson = require("../openings.json");
function* getAllOpenings() {
    try {
        const converted = camelArray(openingsJson, {recursive: true, arrayRecursive: true}) as IOpening[];
        yield put(loadOpeningsSuccessFactory(converted));
    } catch (err) {
        yield put(loadOpeningsFailureFactory(err));
    }
}

export function* getAllOpeningsSaga() {
    yield takeLatest(ACTION_TYPES.LOAD_OPENINGS.REQUEST, () => {
        return getAllOpenings();
    });
}

export function* rootSaga() {
    yield all([getAllOpeningsSaga()]);
}
