import { Color } from "csstype";
import * as React from "react";
import { Move } from "../chess-api";
import { Bishop, IProps as IPieceProps, King, Knight, Pawn, Queen, Rook } from "./Pieces";

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
    origX: number;
    origY: number;
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
    selectedPieceIndex: number;
}

export class Board extends React.Component<IProps, IState> {
    private squares: JSX.Element[];
    private boardRef: React.RefObject<SVGSVGElement>;
    constructor(props: IProps) {
        super(props);
        this.boardRef = React.createRef();
        this.handleMouseDown = this.handleMouseDown.bind(this);
        this.handleMouseUp = this.handleMouseUp.bind(this);
        this.handleMouseMove = this.handleMouseMove.bind(this);
        this.handleContextMenu = this.handleContextMenu.bind(this);
        this.squares = this.createSquares();
        this.initializeState(props);
    }

    public render() {
        const pieces = this.createPieces();
        return (
            <svg ref={this.boardRef} className="board" viewBox="0 0 512 512">
                {this.squares}
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

    private createPieces(): JSX.Element[] {
        const pieces = [];
        for (const cur of this.state.pieceState) {
            const isBlack = cur.pieceLetter.toLowerCase() === cur.pieceLetter;
            const fill = isBlack ? "#2d2d2d" : "white";
            const stroke = "black";
            const props: IPieceProps = {
                dataSrc: cur.square,
                fillColor: fill,
                onMouseDown: this.handleMouseDown,
                onMouseMove: this.handleMouseMove,
                strokeColor: stroke,
                x: cur.x,
                y: cur.y,
            };
            let piece = null;
            switch (cur.pieceLetter.toLowerCase()) {
                case "p":
                    piece = <Pawn key={cur.square} {...props}/>;
                    break;
                case "n":
                    piece = <Knight key={cur.square} {...props}/>;
                    break;
                case "b":
                    piece = <Bishop key={cur.square} {...props}/>;
                    break;
                case "r":
                    piece = <Rook key={cur.square} {...props}/>;
                    break;
                case "q":
                    piece = <Queen key={cur.square} {...props}/>;
                    break;
                case "k":
                    piece = <King key={cur.square} {...props}/>;
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
            const x = col * 64;
            const y = 512 - (64 * (row + 1));

            pieceState.push({
                pieceLetter,
                square: loc.s,
                origX: x,
                origY: y,
                x,
                y,
            });
        }
        this.state = {
            pieceState,
            selectedPieceIndex: null,
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
        const square = event.currentTarget.getAttribute("data-src");
        if (event.button === 0) {
            // left click -> move
            // if no piece -> nothing to do
            let i = null;
            for (i = 0; i < this.state.pieceState.length; i++) {
                if (this.state.pieceState[i].square === square) {
                    break;
                }
            }
            this.setState({
                ...this.state,
                selectedPieceIndex: i,
            });
        } else if (event.button === 2) {
            // right click -> arrow
        }
        return;
    }

    private handleMouseUp(event: React.MouseEvent<SVGElement>) {

        return;
    }

    private handleMouseMove(event: React.MouseEvent<SVGElement>) {
        if (this.state.selectedPieceIndex != null) {
            const newArray = [...this.state.pieceState];
            const copy = {...newArray[this.state.selectedPieceIndex]};
            const adjustedCoords = this.convertPageCoordinatesToBoardRelative(event.pageX, event.pageY);
            copy.x = adjustedCoords[0];
            copy.y = adjustedCoords[1];
            newArray[this.state.selectedPieceIndex] = copy;
            this.setState({
                ...this.state,
                pieceState: newArray,
            });
        }
        return;
    }

    private convertPageCoordinatesToBoardRelative(x: number, y: number): number[] {
        const boundingRect = this.boardRef.current.getBoundingClientRect();
        return [x - boundingRect.left, y - boundingRect.top];
    }
}
