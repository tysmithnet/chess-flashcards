export enum Piece {
    Pawn = "P",
    Knight = "N",
    Bishop = "B",
    Rook = "R",
    Queen = "Q",
    King = "K",
}

export enum Location {
    A1 = "a1",
    A2 = "a2",
    A3 = "a3",
    A4 = "a4",
    A5 = "a5",
    A6 = "a6",
    A7 = "a7",
    A8 = "a8",
    B1 = "b1",
    B2 = "b2",
    B3 = "b3",
    B4 = "b4",
    B5 = "b5",
    B6 = "b6",
    B7 = "b7",
    B8 = "b8",
    C1 = "c1",
    C2 = "c2",
    C3 = "c3",
    C4 = "c4",
    C5 = "c5",
    C6 = "c6",
    C7 = "c7",
    C8 = "c8",
    D1 = "d1",
    D2 = "d2",
    D3 = "d3",
    D4 = "d4",
    D5 = "d5",
    D6 = "d6",
    D7 = "d7",
    D8 = "d8",
    E1 = "e1",
    E2 = "e2",
    E3 = "e3",
    E4 = "e4",
    E5 = "e5",
    E6 = "e6",
    E7 = "e7",
    E8 = "e8",
    F1 = "f1",
    F2 = "f2",
    F3 = "f3",
    F4 = "f4",
    F5 = "f5",
    F6 = "f6",
    F7 = "f7",
    F8 = "f8",
    G1 = "g1",
    G2 = "g2",
    G3 = "g3",
    G4 = "g4",
    G5 = "g5",
    G6 = "g6",
    G7 = "g7",
    G8 = "g8",
    H1 = "h1",
    H2 = "h2",
    H3 = "h3",
    H4 = "h4",
    H5 = "h5",
    H6 = "h6",
    H7 = "h7",
    H8 = "h8",
}

export enum Side {
    White = "W",
    Black = "B",
}

export interface IPieceLocation {
    side: Side;
    piece: Piece;
    location: Location;
}

export interface IPosition {
    whoseTurn: Side;
    pieces: IPieceLocation[];
}

export const DEFAULT_POSITION: IPosition = {
    pieces: [
        // 1st Rank
        {
            location: Location.A1,
            piece: Piece.Rook,
            side: Side.White,
        },
        {
            location: Location.B1,
            piece: Piece.Knight,
            side: Side.White,
        },
        {
            location: Location.C1,
            piece: Piece.Bishop,
            side: Side.White,
        },
        {
            location: Location.D1,
            piece: Piece.Queen,
            side: Side.White,
        },
        {
            location: Location.E1,
            piece: Piece.King,
            side: Side.White,
        },
        {
            location: Location.F1,
            piece: Piece.Bishop,
            side: Side.White,
        },
        {
            location: Location.G1,
            piece: Piece.Knight,
            side: Side.White,
        },
        {
            location: Location.H1,
            piece: Piece.Rook,
            side: Side.White,
        },
        // 2nd Rank
        {
            location: Location.A2,
            piece: Piece.Pawn,
            side: Side.White,
        },
        {
            location: Location.B2,
            piece: Piece.Pawn,
            side: Side.White,
        },
        {
            location: Location.C2,
            piece: Piece.Pawn,
            side: Side.White,
        },
        {
            location: Location.D2,
            piece: Piece.Pawn,
            side: Side.White,
        },
        {
            location: Location.E2,
            piece: Piece.Pawn,
            side: Side.White,
        },
        {
            location: Location.F2,
            piece: Piece.Pawn,
            side: Side.White,
        },
        {
            location: Location.G2,
            piece: Piece.Pawn,
            side: Side.White,
        },
        {
            location: Location.H2,
            piece: Piece.Pawn,
            side: Side.White,
        },
        // 2nd Rank
        {
            location: Location.A7,
            piece: Piece.Pawn,
            side: Side.Black,
        },
        {
            location: Location.B7,
            piece: Piece.Pawn,
            side: Side.Black,
        },
        {
            location: Location.C7,
            piece: Piece.Pawn,
            side: Side.Black,
        },
        {
            location: Location.D7,
            piece: Piece.Pawn,
            side: Side.Black,
        },
        {
            location: Location.E7,
            piece: Piece.Pawn,
            side: Side.Black,
        },
        {
            location: Location.F7,
            piece: Piece.Pawn,
            side: Side.Black,
        },
        {
            location: Location.G7,
            piece: Piece.Pawn,
            side: Side.Black,
        },
        {
            location: Location.H7,
            piece: Piece.Pawn,
            side: Side.Black,
        },
        // 8th Rank
        {
            location: Location.A8,
            piece: Piece.Rook,
            side: Side.Black,
        },
        {
            location: Location.B8,
            piece: Piece.Knight,
            side: Side.Black,
        },
        {
            location: Location.C8,
            piece: Piece.Bishop,
            side: Side.Black,
        },
        {
            location: Location.D8,
            piece: Piece.Queen,
            side: Side.Black,
        },
        {
            location: Location.E8,
            piece: Piece.King,
            side: Side.Black,
        },
        {
            location: Location.F8,
            piece: Piece.Bishop,
            side: Side.Black,
        },
        {
            location: Location.G8,
            piece: Piece.Knight,
            side: Side.Black,
        },
        {
            location: Location.H8,
            piece: Piece.Rook,
            side: Side.Black,
        },
    ],
    whoseTurn: Side.White,
};

export interface IMove {
    whoMoved: Side;
    piece: Piece;
    from: Location;
    to: Location;
    isCastle?: boolean;
    capturedPiece?: IPieceLocation;
    isPromotion?: boolean;
    turnNum?: number;
    alternateLines?: IMove[][];
    causesCheck?: boolean;
    isMate?: boolean;
    isStalemate?: boolean;
    comments?: string[];
    timeTaken?: Date;
}

export enum MoveAnalysis {
    Blunder = "??",
    Mistake = "?",
    DubiousMove = "?!",
    InterestingMove = "!?",
    GoodMove = "!",
    BrilliantMove = "!!",
}
