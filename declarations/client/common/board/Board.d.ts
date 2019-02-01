import { Config as IConfig } from "chessground/config";
import { Key, Piece } from "chessground/types";
import * as React from "react";
import { Move as IMove } from "../../chess-api";
import { IBaseProps } from "../../root";
import "./3d.css";
import "./board.css";
import "./theme.css";
export interface IProps extends IConfig, IBaseProps {
    moves?: IMove[];
    onMove?: (src: Key, dst: Key, capturedPiece?: Piece) => void;
}
export declare class Board extends React.Component<IProps> {
    private ref;
    private ground;
    constructor(props: IBaseProps);
    render(): JSX.Element;
    componentDidMount(): void;
    componentWillUnmount(): void;
    componentWillReceiveProps(nextProps: IProps): void;
    private convertMovesToDests;
}
