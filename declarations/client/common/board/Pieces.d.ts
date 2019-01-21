/// <reference types="react" />
import { Color } from "csstype";
export interface IProps {
    fillColor: Color;
    strokeColor: Color;
}
export declare const Bishop: (props: IProps) => JSX.Element;
export declare const Knight: (props: IProps) => JSX.Element;
export declare const Pawn: (props: IProps) => JSX.Element;
