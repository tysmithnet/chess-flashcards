import { Color } from "csstype";
import * as React from "react";
import { Move } from "../chess-api";
import "./board.styles";
export declare const EMPTY_BOARD: any[];
export declare const STARTING_POSITION: string[];
interface IPieceState {
    pieceLetter: string;
    square: string;
}
export interface IArrow {
    src: string;
    dst: string;
    color: Color;
}
export interface ISelectedSquare {
    square: string;
    color: Color;
}
export interface IProps {
    position: string[];
    legalMoves: Move[];
    freeMove?: boolean;
    isBlackPerspective?: boolean;
    onMove?: (src: string, dst: string) => void;
}
export interface IState {
    pieceState: IPieceState[];
    selectedPieceIndex: number;
    arrows: IArrow[];
    selectedSquares: ISelectedSquare[];
    rightMouseDownSquare: string;
}
export declare function convertSquare(square: string | number | number[]): {
    s: string;
    i: number;
    c: number[];
};
export declare class Board extends React.Component<IProps, IState> {
    static getDerivedStateFromProps(props: IProps, state: IState): IState;
    private boardRef;
    constructor(props: IProps);
    render(): JSX.Element;
    private createPieces;
    private createSquares;
    private handleDrop;
    private movePiece;
    private handleDragStart;
    private handleDragOver;
    private handleContextMenu;
    private handleMouseDown;
    private handleMouseUp;
    private handleMouseMove;
}
export {};
