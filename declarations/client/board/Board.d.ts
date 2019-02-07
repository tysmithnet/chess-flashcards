import { Color } from "csstype";
import * as React from "react";
import { Move } from "../chess-api";
export declare const STARTING_POSITION: string[];
interface IPieceState {
    piece: JSX.Element;
    x: number;
    y: number;
    square: string;
}
export interface IArrow {
    src: string;
    dst: string;
    color: Color;
}
export interface IProps {
    darkSquareColor?: Color;
    lightSquareColor?: Color;
    position: string[];
    legalMoves: Move[];
}
export interface IState {
    pieceState: IPieceState[];
}
export declare class Board extends React.Component<IProps, IState> {
    private squares;
    constructor(props: IProps);
    componentDidUpdate(): void;
    render(): JSX.Element;
    private convertSquare;
    private initializeState;
    private createSquares;
    private handleContextMenu;
    private handleMouseDown;
    private handleMouseUp;
    private handleMouseMove;
}
export {};
