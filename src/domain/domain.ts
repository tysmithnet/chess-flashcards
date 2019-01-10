export enum Location {
    a1 = "a1",
    a2 = "a2",
    a3 = "a3",
    a4 = "a4",
    a5 = "a5",
    a6 = "a6",
    a7 = "a7",
    a8 = "a8",
    b1 = "b1",
    b2 = "b2",
    b3 = "b3",
    b4 = "b4",
    b5 = "b5",
    b6 = "b6",
    b7 = "b7",
    b8 = "b8",
    c1 = "c1",
    c2 = "c2",
    c3 = "c3",
    c4 = "c4",
    c5 = "c5",
    c6 = "c6",
    c7 = "c7",
    c8 = "c8",
    d1 = "d1",
    d2 = "d2",
    d3 = "d3",
    d4 = "d4",
    d5 = "d5",
    d6 = "d6",
    d7 = "d7",
    d8 = "d8",
    e1 = "e1",
    e2 = "e2",
    e3 = "e3",
    e4 = "e4",
    e5 = "e5",
    e6 = "e6",
    e7 = "e7",
    e8 = "e8",
    f1 = "f1",
    f2 = "f2",
    f3 = "f3",
    f4 = "f4",
    f5 = "f5",
    f6 = "f6",
    f7 = "f7",
    f8 = "f8",
    g1 = "g1",
    g2 = "g2",
    g3 = "g3",
    g4 = "g4",
    g5 = "g5",
    g6 = "g6",
    g7 = "g7",
    g8 = "g8",
}

export class Move {
    public from: PiecePosition;
    public to: PiecePosition;
}

export class Pgn {
    public event: string;
    public site: string;
    public date: Date;
    public round: string;
    public white: string;
    public black: string;
    public result: string;
}

export enum Piece {
    pawn = "P",
    knight = "N",
    bishop = "B",
    rook = "R",
    queen = "Q",
    king = "K",
}
export class PiecePosition {
    public piece: Piece;
    public location: Location;
}
export enum Side {
    white = "White",
    black = "Black",
}
export class Turn {
    public number: number;
}

export class Position {
    public piecePositions: PiecePosition[];
    public inCheck: Side;
}
