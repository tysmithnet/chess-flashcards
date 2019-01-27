/// <reference types="react" />
import { Color } from "csstype";
import { IPieceLocation } from "../../../shared/chess";
export interface IProps {
    darkSquareColor: Color;
    lightSquareColor: Color;
    darkPieceColor: Color;
    lightPieceColor: Color;
    pieceLocations: IPieceLocation[];
}
export declare const Board: (props: IProps) => JSX.Element;
