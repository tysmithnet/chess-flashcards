import * as React from "react";
import { IBaseProps } from "../root";
export interface IProps extends IBaseProps {
    isOpen: boolean;
    onSubmit: (username: string, password: string) => void;
    onClose: (event?: React.SyntheticEvent, reason?: string) => void;
}
export interface IState {
    username: string;
    password: string;
}
export declare class LoginDialog extends React.Component<IProps, IState> {
    constructor(props: IProps);
    render(): JSX.Element;
    private handleKeyUp;
    private handleSubmit;
    private handleUsernameChange;
    private handlePasswordChange;
}
