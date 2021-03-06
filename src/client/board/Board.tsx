import cn from "classnames";
import { Color } from "csstype";
import * as _ from "lodash";
import * as React from "react";
import {convertSquare, IMove} from "../root";
import "./board.styles";
const BlackBishop = require("./images/bb.png");
const BlackKing = require("./images/bk.png");
const BlackKnight = require("./images/bn.png");
const BlackPawn = require("./images/bp.png");
const BlackQueen = require("./images/bq.png");
const BlackRook = require("./images/br.png");
const WhiteBishop = require("./images/wb.png");
const WhiteKing = require("./images/wk.png");
const WhiteKnight = require("./images/wn.png");
const WhitePawn = require("./images/wp.png");
const WhiteQueen = require("./images/wq.png");
const WhiteRook = require("./images/wr.png");

interface IPieceState {
    pieceLetter: string;
    square: string;
}

export interface IArrow {
    src: string;
    dst: string;
    color: Color;
}

export interface ISelectedSquare {
    square: string;
    color: Color;
}

export interface IProps {
    position: string[]; // ["R", "N", "B", "Q" ...] starting from A1, A2, .. H8, null represents empty
    legalMoves: IMove[];
    freeMove?: boolean;
    isBlackPerspective?: boolean;
    onMove?: (src: string, dst: string) => void;
}

export interface IState {
    pieceState: IPieceState[];
    selectedPieceIndex: number;
    arrows: IArrow[];
    selectedSquares: ISelectedSquare[];
    rightMouseDownSquare: string;
}

export class Board extends React.Component<IProps, IState> {

    public static getDerivedStateFromProps(props: IProps, state: IState): IState {
        const pieceState: IPieceState[] = [];
        for (let i = 0; i < 64; i++) {
            const pieceLetter = props.position[i];
            if (pieceLetter == null) {
                continue;
            }
            const row = Math.floor(i / 8);
            const col = i % 8;
            const loc = convertSquare([row, col]);

            pieceState.push({
                pieceLetter,
                square: loc.s,
            });
        }

        return {
            pieceState,
            selectedSquares: [],
            arrows: [],
            rightMouseDownSquare: null,
            selectedPieceIndex: null,
        };
    }

    private boardRef: React.RefObject<SVGSVGElement>;
    constructor(props: IProps) {
        super(props);
        this.boardRef = React.createRef();
        this.handleMouseDown = this.handleMouseDown.bind(this);
        this.handleMouseUp = this.handleMouseUp.bind(this);
        this.handleMouseMove = this.handleMouseMove.bind(this);
        this.handleContextMenu = this.handleContextMenu.bind(this);
        this.handleDragOver = this.handleDragOver.bind(this);
        this.handleDragStart = this.handleDragStart.bind(this);
        this.handleDrop = this.handleDrop.bind(this);
        this.state = {
            arrows: [],
            pieceState: [],
            rightMouseDownSquare: null,
            selectedPieceIndex: null,
            selectedSquares: [],
        };
    }

    public render() {
        const squares = this.createSquares();
        return (
            <div className={cn("board-container", {"black-perspective": this.props.isBlackPerspective})}>
                <div className={"board"}>
                    {squares}
                </div>
                <div className="overlay" />
            </div>
        );
    }

    private createPieces(): JSX.Element[] {
        const pieces = [];
        for (const cur of this.state.pieceState) {
            const isBlack = cur.pieceLetter.toLowerCase() === cur.pieceLetter;
            let piece = null;
            let src = null;
            switch (cur.pieceLetter.toLowerCase()) {
                case "p":
                    src = isBlack ? BlackPawn : WhitePawn;
                    piece = <img className={"piece"} key={cur.square} data-src={cur.square} src={src} draggable={true} onDragStart={this.handleDragStart} />;
                    break;
                case "n":
                    src = isBlack ? BlackKnight : WhiteKnight;
                    piece = <img className={"piece"} key={cur.square} data-src={cur.square} src={src} draggable={true} onDragStart={this.handleDragStart} />;
                    break;
                case "b":
                    src = isBlack ? BlackBishop : WhiteBishop;
                    piece = <img className={"piece"} key={cur.square} data-src={cur.square} src={src} draggable={true} onDragStart={this.handleDragStart} />;
                    break;
                case "r":
                    src = isBlack ? BlackRook : WhiteRook;
                    piece = <img className={"piece"} key={cur.square} data-src={cur.square} src={src} draggable={true} onDragStart={this.handleDragStart} />;
                    break;
                case "q":
                    src = isBlack ? BlackQueen : WhiteQueen;
                    piece = <img className={"piece"} key={cur.square} data-src={cur.square} src={src} draggable={true} onDragStart={this.handleDragStart} />;
                    break;
                case "k":
                    src = isBlack ? BlackKing : WhiteKing;
                    piece = <img className={"piece"} key={cur.square} data-src={cur.square} src={src} draggable={true} onDragStart={this.handleDragStart} />;
                    break;
            }
            pieces.push(piece);
        }
        return pieces;
    }

    private createSquares(): JSX.Element[] {
        const pieces = this.createPieces();
        const rects: JSX.Element[] = [];
        for (let rank = 7; rank >= 0; rank--) {
            for (let file = 0; file < 8; file++) {
                const square = String.fromCharCode(97 + file) + (rank + 1);
                const isBlack = (rank + file) % 2 === 0;
                let rect = null;
                let style = null;
                const selectedSquares = this.state.selectedSquares.filter(s => s.square === square);
                if (selectedSquares.length) {
                    style = {
                        backgroundImage: `linear-gradient(red, green)`,
                    };
                }
                const pieceAtSquare = pieces.find(p => p.key === square);
                if (pieceAtSquare != null) {
                    rect = (
                        <div key={square} data-src={square} className={cn("square", { white: !isBlack, black: isBlack })} style={style} onDragOver={this.handleDragOver} onDrop={this.handleDrop} onMouseDown={this.handleMouseDown} onMouseUp={this.handleMouseUp} onContextMenu={this.handleContextMenu}>
                            {pieceAtSquare}
                        </div>
                    );
                } else {
                    rect = <div key={square} data-src={square} className={cn("square", { white: !isBlack, black: isBlack })} style={style}  onDragOver={this.handleDragOver} onDrop={this.handleDrop} onMouseDown={this.handleMouseDown} onMouseUp={this.handleMouseUp} onContextMenu={this.handleContextMenu}/>;
                }
                rects.push(rect);
            }
        }
        return rects;
    }

    private handleDrop(event: React.DragEvent<HTMLDivElement>) {
        const src = event.dataTransfer.getData("piece");
        const dst = event.currentTarget.getAttribute("data-src");
        this.movePiece(src, dst);
        return;
    }

    private movePiece(src: string, dst: string) {
        const newArray = [...this.state.pieceState];
        let i = 0;
        for (i = 0; i < newArray.length; i++) {
            if (newArray[i].square === src) {
                break;
            }
        }
        const copy = { ...newArray[i] };
        copy.square = dst;
        newArray[i] = copy;
        this.setState({
            pieceState: newArray,
            selectedPieceIndex: null,
        });
        if (this.props.onMove) {
            this.props.onMove(src, dst);
        }
        return;
    }

    private handleDragStart(event: React.DragEvent<HTMLImageElement>) {
        event.dataTransfer.setData("piece", event.currentTarget.getAttribute("data-src"));
        return;
    }

    private handleDragOver(event: React.DragEvent<HTMLDivElement>) {
        event.preventDefault();
        return;
    }

    private handleContextMenu(event: React.MouseEvent<HTMLDivElement>) {
        event.preventDefault();
        return;
    }

    private handleMouseDown(event: React.MouseEvent<HTMLDivElement>) {
        if (event.button === 2) {
            const square = event.currentTarget.getAttribute("data-src");
            event.preventDefault();
            this.setState({
                ...this.state,
                rightMouseDownSquare: square,
            });
        }
        return;
    }

    private handleMouseUp(event: React.MouseEvent<HTMLDivElement>) {
        if (event.button === 2) {
            const square = event.currentTarget.getAttribute("data-src");
            if (square === this.state.rightMouseDownSquare) {
                // highlight square
                const existing = this.state.selectedSquares.find(s => s.square === square && s.color === "red"); // todo: need to add modifier for other colors
                let copy = [...this.state.selectedSquares];
                if (existing) {
                    copy = _.remove(copy, s => s === existing);
                } else {
                    copy.push({
                        square,
                        color: "red",
                    });
                }
                this.setState({
                    ...this.state,
                    selectedSquares: copy,
                });
            }
        }
    }

    private handleMouseMove(event: React.MouseEvent<HTMLDivElement>) {
        return;
    }
}
