import { Color } from "csstype";
import * as React from "react";
import { IMove } from "../root";
import "./board.styles";
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
    legalMoves: IMove[];
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
