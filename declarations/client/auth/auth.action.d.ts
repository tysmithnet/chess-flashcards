import { IAction } from "../root";
import { IUser } from "./auth.domain";
export declare const ACTION_TYPES: {
    LOGIN_USER: {
        REQUEST: string;
        SUCCESS: string;
        FAILURE: string;
    };
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
export declare function loginUserRequestFactory(username: string, password: string): ILoginRequest;
export declare function loginUserSuccessFactory(user: IUser): ILoginSuccess;
export declare function loginUserFailureFactory(message: string): ILoginUserFailure;
