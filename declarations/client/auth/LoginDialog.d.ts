import * as React from "react";
import { IBaseProps } from "../root";
export interface IProps extends IBaseProps {
    isOpen: boolean;
    onSubmit: (username: string, password: string) => void;
    onClose: () => void;
}
export interface IState {
    username: string;
    password: string;
}
export declare class LoginDialog extends React.Component<IProps, IState> {
    constructor(props: IProps);
    render(): JSX.Element;
    private handleSubmit;
    private handleUsernameChange;
    private handlePasswordChange;
}
