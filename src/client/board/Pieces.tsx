import * as React from "react";
const BlackBishop =  require("./images/bb.png");
const BlackKing =  require("./images/bk.png");
const BlackKnight =  require("./images/bn.png");
const BlackPawn =  require("./images/bp.png");
const BlackQueen =  require("./images/bq.png");
const BlackRook =  require("./images/br.png");
const WhiteBishop =  require("./images/wb.png");
const WhiteKing =  require("./images/wk.png");
const WhiteKnight =  require("./images/wn.png");
const WhitePawn =  require("./images/wp.png");
const WhiteQueen =  require("./images/wq.png");
const WhiteRook =  require("./images/wr.png");

export interface IProps {
    dataSrc: string; // a1..h8
    isWhite: boolean;
    onMouseDown?: React.MouseEventHandler<SVGElement>;
    onMouseMove?: React.MouseEventHandler<SVGElement>;
    x: number;
    y: number;
}

export class Pawn extends React.Component<IProps> {
    constructor(props: IProps) {
        super(props);
    }

    public render() {
        let src = BlackPawn;
        if (this.props.isWhite) {
            src = WhitePawn;
        }
        return <img data-src={this.props.dataSrc} src={src} />;
    }
}

export class Knight extends React.Component<IProps> {
    constructor(props: IProps) {
        super(props);
    }

    public render() {
        let src = BlackKnight;
        if (this.props.isWhite) {
            src = WhiteKnight;
        }
        return <img data-src={this.props.dataSrc} src={src} />;
    }
}

export class Bishop extends React.Component<IProps> {
    constructor(props: IProps) {
        super(props);
    }

    public render() {
        let src = BlackBishop;
        if (this.props.isWhite) {
            src = WhiteBishop;
        }
        return <img data-src={this.props.dataSrc} src={src} />;
    }
}

export class Rook extends React.Component<IProps> {
    constructor(props: IProps) {
        super(props);
    }

    public render() {
        let src = BlackRook;
        if (this.props.isWhite) {
            src = WhiteRook;
        }
        return <img data-src={this.props.dataSrc} src={src} />;
    }
}

export class Queen extends React.Component<IProps> {
    constructor(props: IProps) {
        super(props);
    }

    public render() {
        let src = BlackQueen;
        if (this.props.isWhite) {
            src = WhiteQueen;
        }
        return <img data-src={this.props.dataSrc} src={src} />;
    }
}

export class King extends React.Component<IProps> {
    constructor(props: IProps) {
        super(props);
    }

    public render() {
        let src = BlackKing;
        if (this.props.isWhite) {
            src = WhiteKing;
        }
        return <img data-src={this.props.dataSrc} src={src} />;
    }
}
