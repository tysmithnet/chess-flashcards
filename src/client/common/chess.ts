const fenRegex = new RegExp("([pnbrqk1-8]+\/){7}([pnbrqk1-8]+)", "i");

export function fenToArray(fen: string): string[] {
    if (!fenRegex.test(fen)) {
        throw new Error("fen is not valid");
    }
    const relevantPart = fenRegex.exec(fen)[0];
    const board = relevantPart.split("/").reverse().join("");

    const res = new Array(64);
    let b = 0;
    for (let i = 0; i < board.length; i++) {
        const char = board.charAt(i);
        if (/[1-8]/.test(char)) {
            const converted = parseInt(char, 10);
            for (let j = b; j < b + converted; j++) {
                res[j] = null;
            }
            b += converted;
            continue;
        }
        res[b] = char;
        b++;
    }
    return res;
}

export function arrayToFen(board: string[]): string {
    if (!board || board.length !== 64) {
        throw new Error("Board must have exactly 64 elements");
    }
    let fen = "";
    for (let row = 0; row < 8; row++) {
        let nullCount = 0;
        let line = "";
        for (let col = 0; col < 8; col++) {
            const index = row * 8 + col;
            const letter = board[index];
            if (!letter) {
                nullCount++;
                continue;
            }
            if (nullCount) {
                line += `${nullCount}`;
                nullCount = 0;
            }
            line += letter;
        }
        if (nullCount) {
            line += `${nullCount}`;
        }
        fen = `${line}/${fen}`;
    }
    fen = fen.substr(0, fen.length - 1);
    return fen;
}
