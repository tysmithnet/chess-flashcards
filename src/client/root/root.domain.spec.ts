import {applyMove} from "./root.domain";

test("applyMove should handle basic king moves", () => {
    // arrange
    const beforePosition =   ["R", "N", "B", "Q", "K", "B", "N", "R", "P", "P", "P", "P", null, null, "P", "P", null, null, null, null, null, null, null, null, null, null, null, null, "P", "p", null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, "p", "p", "p", "p", null, "p", "p", "p", "r", "n", "b", "q", "k", "b", "n", "r"];
    const expectedPosition = ["R", "N", "B", "Q", null, "B", "N", "R", "P", "P", "P", "P", null, "K", "P", "P", null, null, null, null, null, null, null, null, null, null, null, null, "P", "p", null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, "p", "p", "p", "p", null, "p", "p", "p", "r", "n", "b", "q", "k", "b", "n", "r"];

    // act
    const actual = applyMove(beforePosition, {src: "e1", dst: "f2"});

    // assert
    expect(actual).toEqual(expectedPosition);
});
