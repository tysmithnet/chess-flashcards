export enum Piece {
    WhitePawn = "P",
    WhiteKnight = "N",
    WhiteBishop = "B",
    WhiteRook = "R",
    WhiteQueen = "Q",
    WhiteKing = "K",
    BlackPawn = "p",
    BlackKnight = "n",
    BlackBishop = "b",
    BlackRook = "r",
    BlackQueen = "q",
    BlackKing = "k",
}

export function isWhitePiece(piece: Piece): boolean {
    return (piece as string).toUpperCase() === (piece as string);
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

export interface IPieceLocation {
    piece: Piece;
    location: Location;
}

export enum Side {
    White = "W",
    Black = "B",
}

export function getDefaultPosition(): IPosition {
    return {
        moveNum: 0,
        pieces: [
            // 1st rank
            {
                location: Location.A1,
                piece: Piece.WhiteRook,
            },
            {
                location: Location.B1,
                piece: Piece.WhiteKnight,
            },
            {
                location: Location.C1,
                piece: Piece.WhiteBishop,
            },
            {
                location: Location.D1,
                piece: Piece.WhiteQueen,
            },
            {
                location: Location.E1,
                piece: Piece.WhiteKing,
            },
            {
                location: Location.F1,
                piece: Piece.WhiteBishop,
            },
            {
                location: Location.G1,
                piece: Piece.WhiteKnight,
            },
            {
                location: Location.H1,
                piece: Piece.WhiteRook,
            },
            // 2nd rank
            {
                location: Location.A2,
                piece: Piece.WhitePawn,
            },
            {
                location: Location.B2,
                piece: Piece.WhitePawn,
            },
            {
                location: Location.C2,
                piece: Piece.WhitePawn,
            },
            {
                location: Location.D2,
                piece: Piece.WhitePawn,
            },
            {
                location: Location.E2,
                piece: Piece.WhitePawn,
            },
            {
                location: Location.F2,
                piece: Piece.WhitePawn,
            },
            {
                location: Location.G2,
                piece: Piece.WhitePawn,
            },
            {
                location: Location.H2,
                piece: Piece.WhitePawn,
            },
            // 7th rank
            {
                location: Location.A7,
                piece: Piece.BlackPawn,
            },
            {
                location: Location.B7,
                piece: Piece.BlackPawn,
            },
            {
                location: Location.C7,
                piece: Piece.BlackPawn,
            },
            {
                location: Location.D7,
                piece: Piece.BlackPawn,
            },
            {
                location: Location.E7,
                piece: Piece.BlackPawn,
            },
            {
                location: Location.F7,
                piece: Piece.BlackPawn,
            },
            {
                location: Location.G7,
                piece: Piece.BlackPawn,
            },
            {
                location: Location.H7,
                piece: Piece.BlackPawn,
            },
            // 8th rank
            {
                location: Location.A8,
                piece: Piece.BlackRook,
            },
            {
                location: Location.B8,
                piece: Piece.BlackKnight,
            },
            {
                location: Location.C8,
                piece: Piece.BlackBishop,
            },
            {
                location: Location.D8,
                piece: Piece.BlackQueen,
            },
            {
                location: Location.E8,
                piece: Piece.BlackKing,
            },
            {
                location: Location.F8,
                piece: Piece.BlackBishop,
            },
            {
                location: Location.G8,
                piece: Piece.BlackKnight,
            },
            {
                location: Location.H8,
                piece: Piece.BlackRook,
            },
        ],
        whoseTurn: Side.White,
    };
}

export interface IMove {
    moveNum: number;
    from: IPieceLocation;
    to: IPieceLocation;
}

export interface IPosition {
    moveNum: number;
    whoseTurn: Side;
    pieces: IPieceLocation[];
}

export enum MoveAnalysis {
    Blunder = "??",
    Mistake = "?",
    DubiousMove = "?!",
    InterestingMove = "!?",
    GoodMove = "!",
    BrilliantMove = "!!",
}

export function zeroBasedIndicesToLocation(row: number, col: number): Location {
    if (row < 0 || row > 7) {
        throw new Error(`row must be in the range 0..7 inclusive, but found ${row}`);
    }
    if (col < 0 || col > 7) {
        throw new Error(`col must be in the range 0..7 inclusive, but found ${col}`);
    }

    const rank = `${row + 1}`;
    const file = String.fromCharCode(col + 97);
    return `${file}${rank}` as Location;
}

export function locationToZeroBasedIndices(location: Location): number[] {
    const file = location.charCodeAt(0) - 97;
    const rank = parseInt(location.charAt(1), 10) - 1;
    return [rank, file];
}

export function createArrayRep(pieces: IPieceLocation[]): Piece[][] {
    const result: Piece[][] = [];
    for (let i = 0; i < 8; i++) {
        const row: Piece[] = [];
        for (let j = 0; j < 8; j++) {
            row.push(null);
        }
        result.push(row);
    }
    for (const piece of pieces) {
        const col = piece.location.charCodeAt(0) - 97;
        const row = parseInt(piece.location.charAt(1), 10) - 1;
        if (result[row][col] !== null) {
            throw new Error("Multiple pieces attempted to be set at ")
        }
        result[row][col] = piece.piece;
    }
    return result;
}
// -> '  +------------------------+
//     8 | .  r  .  .  .  k  r  . |
//     7 | p  b  p  B  B  p  .  p |
//     6 | .  b  .  .  .  P  .  . |
//     5 | .  .  .  .  .  .  .  . |
//     4 | .  .  .  .  .  .  .  . |
//     3 | .  .  P  .  .  q  .  . |
//     2 | P  .  .  .  .  P  P  P |
//     1 | .  .  .  R  .  .  K  . |
//       +------------------------+
//         a  b  c  d  e  f  g  h'
export function boardToAscii(pieces: IPieceLocation[]): string {
    const rep = createArrayRep(pieces);
    const lines: string[] = [
        "  +------------------------+",
        "8 | .  .  .  .  .  .  .  . |",
        "7 | .  .  .  .  .  .  .  . |",
        "6 | .  .  .  .  .  .  .  . |",
        "5 | .  .  .  .  .  .  .  . |",
        "4 | .  .  .  .  .  .  .  . |",
        "3 | .  .  .  .  .  .  .  . |",
        "2 | .  .  .  .  .  .  .  . |",
        "1 | .  .  .  .  .  .  .  . |",
        "  +------------------------+",
        "    a  b  c  d  e  f  g  h  ",
    ];
    for (const piece of pieces) {
        const rowCol = locationToZeroBasedIndices(piece.location);
        const row = 9 - (rowCol[0] + 1);
        const col = 4 + (3 * rowCol[1]);
        const newChar = piece.piece as string;
        lines[row] = lines[row].substr(0, col) + newChar + lines[row].substr(col + 1);
    }
    return lines.join("\n");
}
