import { Config as IConfig } from "chessground/config";
import * as React from "react";
import { IBaseProps } from "../../root";
import "./3d.css";
import "./board.css";
import "./theme.css";
export interface IProps extends IConfig, IBaseProps {
}
export declare class Board extends React.Component<IProps> {
    private ref;
    private ground;
    constructor(props: IBaseProps);
    render(): JSX.Element;
    componentDidMount(): void;
    componentWillUnmount(): void;
    componentWillReceiveProps(nextProps: IProps): void;
}
