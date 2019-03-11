import { all } from "redux-saga/effects";
import {rootSaga as masterListSaga} from "./master-list";
import {rootSaga as viewerSaga} from "./viewer";

export function* rootSaga() {
    yield all([masterListSaga(), viewerSaga()]);
}
