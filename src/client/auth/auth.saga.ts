import axios from "axios";
import { all, put, takeLatest } from "redux-saga/effects";
import { ACTION_TYPES, ILoginRequest } from "./auth.action";
import { Permissions } from "./auth.domain";

function* loginUser(username: string, password: string) {
    try {
        const res = yield axios.post("/api/login", {
            username,
            password,
        });
        const result = yield res.data;
        const roles = [];
        for (const p of result.permissions) {
            const lookup = Permissions.get(p);
            if (lookup) {
                roles.push(lookup);
            }
        }
        yield put({
            type: ACTION_TYPES.LOGIN_SUCCESS,
            user: {
                id: result.id,
                username: result.username,
                roles,
            },
        });
    } catch (error) {
        yield put({
            error,
            type: ACTION_TYPES.LOGIN_FAILURE,
        });
    }
}

/**
 * Respond to login requests
 *
 * @export
 */
export function* loginSaga() {
    yield takeLatest(ACTION_TYPES.LOGIN_REQUEST, (action: ILoginRequest) => {
        return loginUser(action.id, action.password);
    });
}

/**
 * Root saga for the auth domain
 *
 * @export
 */
export function* rootSaga() {
    yield all([loginSaga()]);
}
