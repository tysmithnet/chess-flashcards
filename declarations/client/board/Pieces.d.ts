import * as React from "react";
export interface IProps {
    dataSrc: string;
    isWhite: boolean;
    onMouseDown?: React.MouseEventHandler<SVGElement>;
    onMouseMove?: React.MouseEventHandler<SVGElement>;
    x: number;
    y: number;
}
export declare class Pawn extends React.Component<IProps> {
    constructor(props: IProps);
    render(): JSX.Element;
}
export declare class Knight extends React.Component<IProps> {
    constructor(props: IProps);
    render(): JSX.Element;
}
export declare class Bishop extends React.Component<IProps> {
    constructor(props: IProps);
    render(): JSX.Element;
}
export declare class Rook extends React.Component<IProps> {
    constructor(props: IProps);
    render(): JSX.Element;
}
export declare class Queen extends React.Component<IProps> {
    constructor(props: IProps);
    render(): JSX.Element;
}
export declare class King extends React.Component<IProps> {
    constructor(props: IProps);
    render(): JSX.Element;
}
