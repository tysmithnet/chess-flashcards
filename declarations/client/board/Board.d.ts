import { Color } from "csstype";
import * as React from "react";
import { Move } from "../chess-api";
import "./board.styles";
export declare const STARTING_POSITION: string[];
interface IPieceState {
    pieceLetter: string;
    origX: number;
    origY: number;
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
    position: string[];
    legalMoves: Move[];
}
export interface IState {
    pieceState: IPieceState[];
    selectedPieceIndex: number;
}
export declare class Board extends React.Component<IProps, IState> {
    private boardRef;
    constructor(props: IProps);
    render(): JSX.Element;
    private convertSquare;
    private createPieces;
    private initializeState;
    private createSquares;
    private handleContextMenu;
    private handleMouseDown;
    private handleMouseUp;
    private handleMouseMove;
    private convertPageCoordinatesToBoardRelative;
}
export {};
