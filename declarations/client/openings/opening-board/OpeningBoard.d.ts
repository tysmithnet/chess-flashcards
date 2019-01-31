import * as React from "react";
import { Move as IMove } from "../../chess-api";
export interface IProps {
    moves: IMove[];
}
export interface IState {
    moveIndex: number;
}
export declare class OpeningBoard extends React.Component<IProps, IState> {
    private curMoves;
    constructor(props: IProps);
    render(): JSX.Element;
    componentDidUpdate(): void;
    private handleBackClick;
    private handleForwardClick;
}
