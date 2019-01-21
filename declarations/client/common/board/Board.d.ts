/// <reference types="react" />
import { Color } from "csstype";
import "./board.styles";
export interface IProps {
    darkcolor: Color;
    lightColor: Color;
}
export declare const Board: (props: IProps) => JSX.Element;
