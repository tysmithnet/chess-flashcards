import { boardToAscii, createArrayRep, getDefaultPosition, isWhitePiece, Location, locationToZeroBasedIndices, Piece, zeroBasedIndicesToLocation } from "./chess";

test("sanity", () => {
    expect(1).toBeTruthy();
});

test("locationToZeroBasedIndices", () => {
    expect(locationToZeroBasedIndices(Location.A1)).toEqual([0, 0]);
    expect(locationToZeroBasedIndices(Location.A2)).toEqual([1, 0]);
    expect(locationToZeroBasedIndices(Location.A3)).toEqual([2, 0]);
    expect(locationToZeroBasedIndices(Location.B1)).toEqual([0, 1]);
    expect(locationToZeroBasedIndices(Location.B2)).toEqual([1, 1]);
    expect(locationToZeroBasedIndices(Location.C4)).toEqual([3, 2]);
    expect(locationToZeroBasedIndices(Location.H8)).toEqual([7, 7]);
});

test("zeroBasedIndicesToLocation", () => {
    expect(() => zeroBasedIndicesToLocation(-1, 0)).toThrowError();
    expect(() => zeroBasedIndicesToLocation(-1, 0)).toThrowError();
    expect(() => zeroBasedIndicesToLocation(8, 0)).toThrowError();
    expect(() => zeroBasedIndicesToLocation(0, 8)).toThrowError();
    expect(zeroBasedIndicesToLocation(0, 0)).toEqual(Location.A1);
    expect(zeroBasedIndicesToLocation(1, 0)).toEqual(Location.A2);
    expect(zeroBasedIndicesToLocation(0, 1)).toEqual(Location.B1);
    expect(zeroBasedIndicesToLocation(3, 2)).toEqual(Location.C4);
    expect(zeroBasedIndicesToLocation(7, 7)).toEqual(Location.H8);
});

test("isWhitePiece", () => {
    expect(isWhitePiece(Piece.WhitePawn)).toBeTruthy();
    expect(isWhitePiece(Piece.WhiteKnight)).toBeTruthy();
    expect(isWhitePiece(Piece.WhiteBishop)).toBeTruthy();
    expect(isWhitePiece(Piece.WhiteRook)).toBeTruthy();
    expect(isWhitePiece(Piece.WhiteQueen)).toBeTruthy();
    expect(isWhitePiece(Piece.WhiteKing)).toBeTruthy();
    expect(isWhitePiece(Piece.BlackPawn)).toBeFalsy();
    expect(isWhitePiece(Piece.BlackKnight)).toBeFalsy();
    expect(isWhitePiece(Piece.BlackBishop)).toBeFalsy();
    expect(isWhitePiece(Piece.BlackRook)).toBeFalsy();
    expect(isWhitePiece(Piece.BlackQueen)).toBeFalsy();
    expect(isWhitePiece(Piece.BlackKing)).toBeFalsy();
});

test("createArrayRep", () => {
    const emptyExpected = [
        [null, null, null, null, null, null, null, null],
        [null, null, null, null, null, null, null, null],
        [null, null, null, null, null, null, null, null],
        [null, null, null, null, null, null, null, null],
        [null, null, null, null, null, null, null, null],
        [null, null, null, null, null, null, null, null],
        [null, null, null, null, null, null, null, null],
        [null, null, null, null, null, null, null, null],
    ];

    const singlePieceExpected = [
        [null, null, null, null, null, null, null, null],
        [null, null, null, null, null, null, null, null],
        [null, null, null, null, null, null, null, null],
        [null, null, "K", null, null, null, null, null],
        [null, null, null, null, null, null, null, null],
        [null, null, null, null, null, null, null, null],
        [null, null, null, null, null, null, null, null],
        [null, null, null, null, null, null, null, null],
    ];

    expect(createArrayRep([])).toEqual(emptyExpected);
    expect(createArrayRep([{
        location: Location.C4,
        piece: Piece.WhiteKing,
    }])).toEqual(singlePieceExpected);
    expect(() => {
        createArrayRep([{
            location: Location.C4,
            piece: Piece.WhiteKing,
        }, {
            location: Location.C4,
            piece: Piece.WhiteKing,
        }]);
    }).toThrow();
});

test("boardToAscii", () => {
    const expected = `  +------------------------+
8 | r  n  b  q  k  b  n  r |
7 | p  p  p  p  p  p  p  p |
6 | .  .  .  .  .  .  .  . |
5 | .  .  .  .  .  .  .  . |
4 | .  .  .  .  .  .  .  . |
3 | .  .  .  .  .  .  .  . |
2 | P  P  P  P  P  P  P  P |
1 | R  N  B  Q  K  B  N  R |
  +------------------------+
    a  b  c  d  e  f  g  h  `;
    const defaultPosition = getDefaultPosition();
    const actual = boardToAscii(defaultPosition.pieces);
    expect(actual).toEqual(expected);
});
