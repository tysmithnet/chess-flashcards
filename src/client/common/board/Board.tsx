import { Color } from "csstype";
import * as React from "react";
import { Bishop, Knight, Pawn } from "./Pieces";

export interface IProps {
    darkcolor: Color;
    lightColor: Color;
}

export const Board = (props: IProps) => {
    const rects = [];
    const pawns = [];
    for (let rank = 0; rank < 8; rank++) {
        for (let file = 0; file < 8; file++) {
            const color = (rank + file) % 2 === 0 ? props.darkcolor : props.lightColor;
            const rect = <rect width={64} height={64} x={file * 64} y={512 - (64 * (rank + 1))} fill={color} />;
            rects.push(rect);
        }
    }
    return (
        <svg className="board" viewBox="0 0 512 512">
            {rects}
            <Bishop strokeColor="black" fillColor="white" />
        </svg>
    );
};
