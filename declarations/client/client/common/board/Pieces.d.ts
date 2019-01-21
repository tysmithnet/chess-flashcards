/// <reference types="react" />
import { Color } from "csstype";
export interface IProps {
    fillColor: Color;
    strokeColor: Color;
    x: number;
    y: number;
}
export declare const King: (props: IProps) => JSX.Element;
export declare const Queen: (props: IProps) => JSX.Element;
export declare const Rook: (props: IProps) => JSX.Element;
export declare const Bishop: (props: IProps) => JSX.Element;
export declare const Knight: (props: IProps) => JSX.Element;
export declare const Pawn: (props: IProps) => JSX.Element;
