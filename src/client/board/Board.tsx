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

export interface IProps {
    position: string[]; // ["R", "N", "B", "Q" ...] starting from A1, A2, .. H8, null represents empty
    legalMoves: Move[];
}

export interface IState {
    selectedPiece: SVGElement;
    x: number;
    y: number;
}

export class Board extends React.Component<IProps, IState> {
    constructor(props: IProps) {
        super(props);
        this.handleMouseDown = this.handleMouseDown.bind(this);
        this.handleMouseMove = this.handleMouseMove.bind(this);
    }

    public render() {
        const rects = [];
        const pieces = [];
        for (let rank = 0; rank < 8; rank++) {
            for (let file = 0; file < 8; file++) {
                const color = (rank + file) % 2 === 0 ? "#214887" : "#6aa0f7";
                const rect = <rect width={64} height={64} x={file * 64} y={512 - (64 * (rank + 1))} fill={color} />;
                rects.push(rect);
            }
        }
        for (let i = 0; i < (this.props.position || []).length; i++) {
            const pieceLetter = this.props.position[i];
            if (pieceLetter == null) {
                continue;
            }
            const row = Math.floor(i / 8);
            const col = i % 8;
            const isWhite = pieceLetter === pieceLetter.toUpperCase();
            const fill = isWhite ? "white" : "black";
            const stroke = isWhite ? "black" : "white";
            switch (pieceLetter.toLowerCase()) {
                case "p":
                    pieces.push(<Pawn onMouseDown={this.handleMouseDown} onMouseMove={this.handleMouseMove} x={col * 64} y={512 - (64 * (row + 1))} fillColor={fill} strokeColor={stroke} />);
                    break;
                case "n":
                    pieces.push(<Knight x={col * 64} y={512 - (64 * (row + 1))} fillColor={fill} strokeColor={stroke} />);
                    break;
                case "b":
                    pieces.push(<Bishop x={col * 64} y={512 - (64 * (row + 1))} fillColor={fill} strokeColor={stroke} />);
                    break;
                case "r":
                    pieces.push(<Rook x={col * 64} y={512 - (64 * (row + 1))} fillColor={fill} strokeColor={stroke} />);
                    break;
                case "q":
                    pieces.push(<Queen x={col * 64} y={512 - (64 * (row + 1))} fillColor={fill} strokeColor={stroke} />);
                    break;
                case "k":
                    pieces.push(<King x={col * 64} y={512 - (64 * (row + 1))} fillColor={fill} strokeColor={stroke} />);
                    const b = <button>something</button>;
                    break;
            }
        }
        return (
            <div className="container">
                <svg className="board" viewBox="0 0 512 512">
                    {rects}
                    {pieces}
                </svg>
            </div>
        );
    }

    private handleMouseDown(event: React.MouseEvent<SVGElement>) {
        this.setState({
            ...this.state,
            selectedPiece: event.currentTarget,
        });
    }

    private handleMouseMove(event: React.MouseEvent<SVGElement>) {
        console.dir(`${event.screenX}, ${event.screenY}, ${event.shiftKey}`);
    }
}
