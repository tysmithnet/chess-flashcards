import * as React from "react";
import { Move as IMove } from "../../chess-api";
export interface IProps {
    moves: IMove[];
}
export interface IState {
    moveIndex: number;
}
export declare class OpeningBoard extends React.Component<IProps, IState> {
    constructor(props: IProps);
    render(): JSX.Element;
    private handleBackClick;
    private handleForwardClick;
}
