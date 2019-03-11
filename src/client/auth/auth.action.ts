import { IAction } from "../root";
import { IUser } from "./auth.domain";

export const ACTION_TYPES = {
    LOGIN_USER: {
        REQUEST: "@auth/LoginUserRequest",
        SUCCESS: "@auth/LoginUserSuccess",
        FAILURE: "@auth/LoginUserFailure",
    },
};

export interface ILoginRequest extends IAction {
    username: string;
    password: string;
}
export interface ILoginSuccess extends IAction {
    user: IUser;
}

export interface ILoginUserFailure extends IAction {
    message: any;
}

export function loginUserRequestFactory(username: string, password: string): ILoginRequest {
    return {
        username,
        password,
        type: ACTION_TYPES.LOGIN_USER.REQUEST,
    };
}

export function loginUserSuccessFactory(user: IUser): ILoginSuccess {
    return {
        type: ACTION_TYPES.LOGIN_USER.SUCCESS,
        user,
    };
}

export function loginUserFailureFactory(message: string): ILoginUserFailure {
    return {
        type: ACTION_TYPES.LOGIN_USER.FAILURE,
        message,
    };
}
