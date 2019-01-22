import { Color } from "csstype";
import * as React from "react";
import { IPieceLocation, Location, Piece, Side } from "../../../shared/chess";
import { Bishop, King, Knight, Pawn, Queen, Rook } from "./Pieces";

export interface IProps {
    darkSquareColor: Color;
    lightSquareColor: Color;
    darkPieceColor: Color;
    lightPieceColor: Color;
    pieceLocations: IPieceLocation[];
}

function convertLocationToOffsets(toConvert: Location): number[] {
    const result: number[] = [];
    const x = toConvert.charCodeAt(0) - 97;
    const y = parseInt(toConvert.charAt(1), 10) - 1;
    result.push(x * 64);
    result.push(512 - (64 * (y + 1)));
    return result;
}

export const Board = (props: IProps) => {
    const rects: JSX.Element[] = [];
    const pieces: JSX.Element[] = [];
    for (let rank = 0; rank < 8; rank++) {
        for (let file = 0; file < 8; file++) {
            const color = (rank + file) % 2 === 0 ? props.darkSquareColor : props.lightSquareColor;
            const rect = <rect width={64} height={64} x={file * 64} y={512 - (64 * (rank + 1))} fill={color} />;
            rects.push(rect);
        }
    }
    if (props.pieceLocations) {
        for (const loc of props.pieceLocations) {
            const offsets = convertLocationToOffsets(loc.location);
            const x = offsets[0];
            const y = offsets[1];
            const fillColor = loc.side === Side.White ? props.lightPieceColor : props.darkPieceColor;
            const strokeColor = loc.side === Side.White ? props.darkPieceColor : props.lightPieceColor;
            switch (loc.piece) {
                case Piece.Pawn:
                    pieces.push(<Pawn fillColor={fillColor} strokeColor={strokeColor} x={x} y={y} />);
                    break;
                case Piece.Knight:
                    pieces.push(<Knight fillColor={fillColor} strokeColor={strokeColor} x={x} y={y} />);
                    break;
                case Piece.Bishop:
                    pieces.push(<Bishop fillColor={fillColor} strokeColor={strokeColor} x={x} y={y} />);
                    break;
                case Piece.Rook:
                    pieces.push(<Rook fillColor={fillColor} strokeColor={strokeColor} x={x} y={y} />);
                    break;
                case Piece.Queen:
                    pieces.push(<Queen fillColor={fillColor} strokeColor={strokeColor} x={x} y={y} />);
                    break;
                case Piece.King:
                    pieces.push(<King fillColor={fillColor} strokeColor={strokeColor} x={x} y={y} />);
                    break;
            }
        }
    }

    return (
        <svg className="board" viewBox="0 0 512 512">
            {rects}
            {pieces}
        </svg>
    );
};
