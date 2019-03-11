import axios from "axios";
import { all, fork, put, takeLatest } from "redux-saga/effects";
import { getPlaylistRequestFactory } from "../playlists";
import { ACTION_TYPES, ILoginRequest, loginUserFailureFactory, loginUserSuccessFactory } from "./auth.action";

function* loginUser(action: ILoginRequest) {
    try {
        const res = yield axios.post("/api/login", {
            username: action.username,
            password: action.password,
        });
        const user = yield res.data;
        yield put(getPlaylistRequestFactory());
        yield put(loginUserSuccessFactory(user));
    } catch (error) {
        yield put(loginUserFailureFactory(error));
    }
}

function* loginSaga() {
    yield takeLatest(ACTION_TYPES.LOGIN_USER.REQUEST, loginUser);
}

function* checkLoggedInUserSaga() {
    try {
        const res = yield axios.get("/api/login");
        const user = yield res.data;
        yield put(getPlaylistRequestFactory());
        yield put(loginUserSuccessFactory(user));
    } catch (err) {
        console.log("No user logged in");
    }
}

export function* rootSaga() {
    yield all([checkLoggedInUserSaga(), loginSaga()]);
}
