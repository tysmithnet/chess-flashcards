import { Color } from "csstype";
import * as React from "react";
import { Move } from "../chess-api";
import { Bishop, King, Knight, Pawn, Queen, Rook } from "./Pieces";

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
    piece: JSX.Element;
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
    darkSquareColor?: Color;
    lightSquareColor?: Color;
    position: string[]; // ["R", "N", "B", "Q" ...] starting from A1, A2, .. H8, null represents empty
    legalMoves: Move[];
}

export interface IState {
    pieceState: IPieceState[];
}

export class Board extends React.Component<IProps, IState> {
    private squares: JSX.Element[];
    constructor(props: IProps) {
        super(props);
        this.squares = this.createSquares();
        this.initializeState(props);
        this.handleMouseDown = this.handleMouseDown.bind(this);
        this.handleMouseUp = this.handleMouseUp.bind(this);
        this.handleMouseMove = this.handleMouseMove.bind(this);
        this.handleContextMenu = this.handleContextMenu.bind(this);
    }

    public componentDidUpdate() {
        this.initializeState(this.props);
    }

    public render() {
        const pieces = this.state.pieceState.map(p => p.piece);
        const rects = this.createSquares();
        return (
            <svg className="board" viewBox="0 0 512 512">
                {rects}
                {pieces}
            </svg>
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
            const x = col * 64;
            const y = 512 - (64 * (row + 1));
            const isBlack = pieceLetter.toLowerCase() === pieceLetter;
            const fill = isBlack ? "#2d2d2d" : "white";
            const stroke = "black";
            let piece = null;
            switch (pieceLetter.toLowerCase()) {
                case "p":
                    piece = <Pawn key={loc.s} fillColor={fill} strokeColor={stroke} x={x} y={y} />;
                    break;
                case "n":
                    piece = <Knight key={loc.s} fillColor={fill} strokeColor={stroke} x={x} y={y} />;
                    break;
                case "b":
                    piece = <Bishop key={loc.s} fillColor={fill} strokeColor={stroke} x={x} y={y} />;
                    break;
                case "r":
                    piece = <Rook key={loc.s} fillColor={fill} strokeColor={stroke} x={x} y={y} />;
                    break;
                case "q":
                    piece = <Queen key={loc.s} fillColor={fill} strokeColor={stroke} x={x} y={y} />;
                    break;
                case "k":
                    piece = <King key={loc.s} fillColor={fill} strokeColor={stroke} x={x} y={y} />;
                    break;
            }
            pieceState.push({
                piece,
                square: loc.s,
                x,
                y,
            });
        }
        this.state = {
            pieceState,
        };
    }

    private createSquares(): JSX.Element[] {
        const rects: JSX.Element[] = [];
        for (let rank = 0; rank < 8; rank++) {
            for (let file = 0; file < 8; file++) {
                const name = String.fromCharCode(97 + file) + (rank + 1);
                const color = (rank + file) % 2 === 0 ? this.props.darkSquareColor : this.props.lightSquareColor;
                const rect = (
                    <rect
                        data-name={name}
                        onContextMenu={this.handleContextMenu}
                        onMouseDown={this.handleMouseDown}
                        onMouseUp={this.handleMouseUp}
                        onMouseMove={this.handleMouseMove}
                        key={`${rank}${file}`}
                        width={64}
                        height={64}
                        x={file * 64}
                        y={512 - (64 * (rank + 1))}
                        fill={color}
                    />);
                rects.push(rect);
            }
        }
        return rects;
    }

    private handleContextMenu(event: React.MouseEvent<SVGElement>) {
        event.preventDefault();
    }

    private handleMouseDown(event: React.MouseEvent<SVGElement>) {
        const square = event.currentTarget.getAttribute("data-name");
        if (event.button === 0) {
            // left click -> move
            // if no piece -> nothing to do

        } else if (event.button === 2) {
            // right click -> arrow
        }
        console.log("down");
        return;
    }

    private handleMouseUp(event: React.MouseEvent<SVGElement>) {
        // clear any in progress drags

        return;
    }

    private handleMouseMove(event: React.MouseEvent<SVGElement>) {
        console.log("move");
        return;
    }
}
