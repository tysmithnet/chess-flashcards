export declare const reducer: import("redux").Reducer<{
    app: import("../app").IRootState;
    auth: import("../auth").IRootState;
    openings: import("../openings").IRootState;
    moves: import("../moves").IRootState;
    games: import("../games").IRootState;
}, import("redux").AnyAction>;
export interface IAction {
    type: string;
}
