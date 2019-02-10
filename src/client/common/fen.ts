const fenRegex = new RegExp("([pnbrqk1-8]+\/){7}([pnbrqk1-8]+)", "i");

export function fenToArray(fen: string) {
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
