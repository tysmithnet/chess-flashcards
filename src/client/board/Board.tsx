import cn from "classnames";
import { Color } from "csstype";
import * as React from "react";
import { Move } from "../chess-api";
import "./board.styles";
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

export const STARTING_POSITION = [
    "R", "N", "B", "Q", "K", "B", "N", "R",
    "P", "P", "P", "P", "P", "P", "P", "P",
    null, null, null, null, null, null, null, null,
    null, null, null, null, null, null, null, null,
    null, null, null, null, null, null, null, null,
    null, null, null, null, null, null, null, null,
    "p", "p", "p", "p", "p", "p", "p", "p",
    "r", "n", "b", "q", "k", "b", "n", "r",
];

interface IPieceState {
    pieceLetter: string;
    square: string;
}

export interface IArrow {
    src: string;
    dst: string;
    color: Color;
}

export interface IProps {
    position: string[]; // ["R", "N", "B", "Q" ...] starting from A1, A2, .. H8, null represents empty
    legalMoves: Move[];
}

export interface IState {
    pieceState: IPieceState[];
    selectedPieceIndex: number;
    mouseX: number;
    mouseY: number;
}

export class Board extends React.Component<IProps, IState> {
    private boardRef: React.RefObject<SVGSVGElement>;
    constructor(props: IProps) {
        super(props);
        this.boardRef = React.createRef();
        this.handleMouseDown = this.handleMouseDown.bind(this);
        this.handleMouseUp = this.handleMouseUp.bind(this);
        this.handleMouseMove = this.handleMouseMove.bind(this);
        this.handleContextMenu = this.handleContextMenu.bind(this);
        this.initializeState(props);
    }

    public render() {
        const squares = this.createSquares();
        return (
            <div className={"board"}>
                {squares}
            </div>
        );
    }

    private convertSquare(square: string | number | number[]): {s: string, i: number, c: number[]} {
        const res = {
            s: "",
            i: 0,
            c: [] as number[],
        };
        if (square instanceof String) {
            res.s = square as string;
            const col = square.charCodeAt(0) - 97;
            const row = parseInt(square.charAt(1), 10) - 1;
            const index = (row * 8) + col;
            res.i = index;
            res.c = [row, col];
        }
        if (typeof(square) === "number") {
            const row = Math.floor(square / 8);
            const col = square % 8;
            const index = (row * 8) + col;
            const alg = `${String.fromCharCode(97 + col)}${row + 1}`;
            res.s = alg;
            res.i = index;
            res.c = [row, col];
        }
        if (Array.isArray(square)) {
            res.c = square as number[];
            res.i = (square[0] * 64) + square[1];
            res.s = `${String.fromCharCode(97 + square[1])}${square[0] + 1}`;
        }
        return res;
    }

    private createPieces(): JSX.Element[] {
        const pieces = [];
        for (const cur of this.state.pieceState) {
            let style = {};
            if (this.state.selectedPieceIndex != null &&
                this.state.pieceState[this.state.selectedPieceIndex].square === cur.pieceLetter) {
                style = {
                    position: "fixed",
                    top: this.state.mouseX,
                    left: this.state.mouseY,
                };
            }
            const isBlack = cur.pieceLetter.toLowerCase() === cur.pieceLetter;
            let piece = null;
            let src = null;
            switch (cur.pieceLetter.toLowerCase()) {
                case "p":
                    src = isBlack ? BlackPawn : WhitePawn;
                    piece = <img className={"piece"} key={cur.square} data-src={cur.square} src={src} />;
                    break;
                case "n":
                    src = isBlack ? BlackKnight : WhiteKnight;
                    piece = <img className={"piece"} key={cur.square} data-src={cur.square} src={src} />;
                    break;
                case "b":
                    src = isBlack ? BlackBishop : WhiteBishop;
                    piece = <img className={"piece"} key={cur.square} data-src={cur.square} src={src} />;
                    break;
                case "r":
                    src = isBlack ? BlackRook : WhiteRook;
                    piece = <img className={"piece"} key={cur.square} data-src={cur.square} src={src} />;
                    break;
                case "q":
                    src = isBlack ? BlackQueen : WhiteQueen;
                    piece = <img className={"piece"} key={cur.square} data-src={cur.square} src={src} />;
                    break;
                case "k":
                    src = isBlack ? BlackKing : WhiteKing;
                    piece = <img className={"piece"} key={cur.square} data-src={cur.square} src={src} />;
                    break;
            }
            pieces.push(piece);
        }
        return pieces;
    }

    private initializeState(props: IProps): void {
        const pieceState: IPieceState[] = [];
        for (let i = 0; i < 64; i++) {
            const pieceLetter = props.position[i];
            if (pieceLetter == null) {
                continue;
            }
            const row = Math.floor(i / 8);
            const col = i % 8;
            const loc = this.convertSquare([row, col]);

            pieceState.push({
                pieceLetter,
                square: loc.s,
            });
        }
        this.state = {
            pieceState,
            selectedPieceIndex: null,
            mouseX: 0,
            mouseY: 0,
        };
    }

    private createSquares(): JSX.Element[] {
        const pieces = this.createPieces();
        const rects: JSX.Element[] = [];
        for (let rank = 7; rank >= 0; rank--) {
            for (let file = 0; file < 8; file++) {
                const name = String.fromCharCode(97 + file) + (rank + 1);
                const isBlack = (rank + file) % 2 === 0;
                let rect = null;
                const pieceAtSquare = pieces.find(p => p.key === name);
                if (pieceAtSquare != null) {
                    rect = (
                        <div key={name} data-src={name} className={cn("square", {white: !isBlack, black: isBlack})}>
                            {pieceAtSquare}
                        </div>
                    );
                } else {
                    rect = <div key={name} data-src={name} className={cn("square", {white: !isBlack, black: isBlack})} />;
                }
                rects.push(rect);
            }
        }
        return rects;
    }

    private handleContextMenu(event: React.MouseEvent<SVGElement>) {
        return;
    }

    private handleMouseDown(event: React.MouseEvent<SVGElement>) {
        return;
    }

    private handleMouseUp(event: React.MouseEvent<SVGElement>) {
        return;
    }

    private handleMouseMove(event: React.MouseEvent<SVGElement>) {
        return ;
    }
}
