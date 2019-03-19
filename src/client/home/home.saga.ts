import axios from "axios";
import { all, delay, put, takeLatest } from "redux-saga/effects";
import { ACTION_TYPES, IOpeningReportRequest, openingReportFailureFactory } from "./home.actions";
import { IOpeningReportLine } from "./home.domain";

function* getOpeningReport(action: IOpeningReportRequest) {
    yield delay(10);
}

function* getOpeningReportSaga() {
    yield takeLatest(ACTION_TYPES.OPENING_REPORT.REQUEST, getOpeningReport);
}

export function* rootSaga() {
    yield all([getOpeningReportSaga()]);
}
