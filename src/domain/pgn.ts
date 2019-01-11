import { Pgn } from "./domain";

export function parsePgn(contents: string): Pgn {
    const pgn = new Pgn();
    const lines = contents.split("\n");
    const numLines = lines.length;
    let curLineNum = 0;

    // process the header
    while (curLineNum < numLines && lines[curLineNum].startsWith("[")) {
        const curLine = lines[curLineNum].slice(1, -1);
        const indexOfFirstSpace = curLine.indexOf(" ");
        const tag = curLine.slice(0, indexOfFirstSpace);
        const value = curLine.slice(indexOfFirstSpace + 2, -1);
        switch (tag) {
            case "Event":
                pgn.event = value;
                break;
            case "Site":
                pgn.site = value;
                break;
            case "Date":
                pgn.date = new Date(value);
                break;
            case "Round":
                pgn.round = value;
                break;
            case "White":
                pgn.white = value;
                break;
            case "Black":
                pgn.black = value;
                break;
            case "Result":
                pgn.result = value;
                break;
            default:
                pgn.otherTags.set(tag, value);
        }
        curLineNum++;
    }
    return pgn;
}
