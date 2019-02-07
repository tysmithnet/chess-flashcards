import { Color } from "csstype";
import * as React from "react";
export interface IProps {
    dataSrc: string;
    fillColor: Color;
    strokeColor: Color;
    onMouseDown?: React.MouseEventHandler<SVGElement>;
    onMouseMove?: React.MouseEventHandler<SVGElement>;
    x: number;
    y: number;
}
export declare class King extends React.Component<IProps> {
    render(): JSX.Element;
}
export declare class Queen extends React.Component<IProps> {
    render(): JSX.Element;
}
export declare class Rook extends React.Component<IProps> {
    render(): JSX.Element;
}
export declare class Bishop extends React.Component<IProps> {
    render(): JSX.Element;
}
export declare class Knight extends React.Component<IProps> {
    render(): JSX.Element;
}
export declare class Pawn extends React.Component<IProps> {
    render(): JSX.Element;
}
