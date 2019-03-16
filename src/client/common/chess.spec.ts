import { arrayToFen, fenToArray } from "./chess";

test("fenToArray should handle the starting position", () => {
    // arrange
    const fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR";

    // act
    const array = fenToArray(fen);

    // assert
    const file8 = ["r", "n", "b", "q", "k", "b", "n", "r"];
    const file7 = ["p", "p", "p", "p", "p", "p", "p", "p"];
    const file6 = [null, null, null, null, null, null, null, null];
    const file5 = [null, null, null, null, null, null, null, null];
    const file4 = [null, null, null, null, null, null, null, null];
    const file3 = [null, null, null, null, null, null, null, null];
    const file2 = ["P", "P", "P", "P", "P", "P", "P", "P"];
    const file1 = ["R", "N", "B", "Q", "K", "B", "N", "R"];
    const board = file1.concat(file2).concat(file3).concat(file4).concat(file5).concat(file6).concat(file7).concat(file8);
    expect(array).toEqual(board);
});

test("fenToArray should be correct after 1 e4", () => {
    // arrange
    const fen = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR";

    // act
    const array = fenToArray(fen);

    // assert
    const file8 = ["r", "n", "b", "q", "k", "b", "n", "r"];
    const file7 = ["p", "p", "p", "p", "p", "p", "p", "p"];
    const file6 = [null, null, null, null, null, null, null, null];
    const file5 = [null, null, null, null, null, null, null, null];
    const file4 = [null, null, null, null, "P", null, null, null];
    const file3 = [null, null, null, null, null, null, null, null];
    const file2 = ["P", "P", "P", "P", null, "P", "P", "P"];
    const file1 = ["R", "N", "B", "Q", "K", "B", "N", "R"];
    const board = file1.concat(file2).concat(file3).concat(file4).concat(file5).concat(file6).concat(file7).concat(file8);
    expect(array).toEqual(board);
});

test("arrayToFen should handle the starting position", () => {
    // arrange
    const fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR";

    // act
    const array = fenToArray(fen);

    // assert
    const file8 = ["r", "n", "b", "q", "k", "b", "n", "r"];
    const file7 = ["p", "p", "p", "p", "p", "p", "p", "p"];
    const file6 = [null, null, null, null, null, null, null, null];
    const file5 = [null, null, null, null, null, null, null, null];
    const file4 = [null, null, null, null, null, null, null, null];
    const file3 = [null, null, null, null, null, null, null, null];
    const file2 = ["P", "P", "P", "P", "P", "P", "P", "P"];
    const file1 = ["R", "N", "B", "Q", "K", "B", "N", "R"];
    const board = file1.concat(file2).concat(file3).concat(file4).concat(file5).concat(file6).concat(file7).concat(file8);
    expect(array).toEqual(board);
});

test("arrayToFen should be correct after 1 e4", () => {
    // arrange
    const file8 = ["r", "n", "b", "q", "k", "b", "n", "r"];
    const file7 = ["p", "p", "p", "p", "p", "p", "p", "p"];
    const file6 = [null, null, null, null, null, null, null, null];
    const file5 = [null, null, null, null, null, null, null, null];
    const file4 = [null, null, null, null, "P", null, null, null];
    const file3 = [null, null, null, null, null, null, null, null];
    const file2 = ["P", "P", "P", "P", null, "P", "P", "P"];
    const file1 = ["R", "N", "B", "Q", "K", "B", "N", "R"];
    const array = file1.concat(file2).concat(file3).concat(file4).concat(file5).concat(file6).concat(file7).concat(file8);

    // act
    const fen = arrayToFen(array);

    // assert
    expect(fen).toEqual("rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR");
});

test("fenToArray should be correct after 1 e4 c5 2. Nf3", () => {
    // arrange
    const fen = "rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R";

    // act
    const array = fenToArray(fen);

    // assert
    const file8 = ["r", "n", "b", "q", "k", "b", "n", "r"];
    const file7 = ["p", "p", null, "p", "p", "p", "p", "p"];
    const file6 = [null, null, null, null, null, null, null, null];
    const file5 = [null, null, "p", null, null, null, null, null];
    const file4 = [null, null, null, null, "P", null, null, null];
    const file3 = [null, null, null, null, null, "N", null, null];
    const file2 = ["P", "P", "P", "P", null, "P", "P", "P"];
    const file1 = ["R", "N", "B", "Q", "K", "B", null, "R"];
    const board = file1.concat(file2).concat(file3).concat(file4).concat(file5).concat(file6).concat(file7).concat(file8);
    expect(array).toEqual(board);
});

test("arrayToFen should be correct after 1 e4 c5 2. Nf3", () => {
    // arrange
    const file8 = ["r", "n", "b", "q", "k", "b", "n", "r"];
    const file7 = ["p", "p", null, "p", "p", "p", "p", "p"];
    const file6 = [null, null, null, null, null, null, null, null];
    const file5 = [null, null, "p", null, null, null, null, null];
    const file4 = [null, null, null, null, "P", null, null, null];
    const file3 = [null, null, null, null, null, "N", null, null];
    const file2 = ["P", "P", "P", "P", null, "P", "P", "P"];
    const file1 = ["R", "N", "B", "Q", "K", "B", null, "R"];
    const array = file1.concat(file2).concat(file3).concat(file4).concat(file5).concat(file6).concat(file7).concat(file8);

    // act
    const fen = arrayToFen(array);

    // assert
    expect(fen).toEqual("rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R");
});
