export declare function getHistory(): import("history").History;
export declare const sagaMiddleware: import("redux-saga").SagaMiddleware<{}>;
export declare const store: import("redux").Store<{
    app: import("../app").IRootState;
    auth: import("../auth").IRootState;
    openings: import("../openings").IRootState;
    moves: import("../moves").IRootState;
    games: import("../games").IRootState;
}, import("redux").AnyAction> & {
    dispatch: {};
};
