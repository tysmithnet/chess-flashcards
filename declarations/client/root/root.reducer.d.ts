export declare const reducer: import("redux").Reducer<{
    app: import("src/client/app/app.domain").IRootState;
    auth: import("src/client/auth/auth.domain").IRootState;
    openings: import("src/client/openings/openings.domain").IRootState;
    moves: import("src/client/moves/moves.domain").IRootState;
    games: import("src/client/games/games.domain").IRootState;
}, import("redux").AnyAction>;
export interface IAction {
    type: string;
}
