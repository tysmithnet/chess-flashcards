import * as React from "react";
import { Move } from "../chess-api";
export declare const STARTING_POSITION: string[];
export interface IProps {
    position: string[];
    legalMoves: Move[];
}
export interface IState {
    selectedPiece: SVGElement;
    x: number;
    y: number;
}
export declare class Board extends React.Component<IProps, IState> {
    constructor(props: IProps);
    render(): JSX.Element;
    private handleMouseDown;
    private handleMouseMove;
}
