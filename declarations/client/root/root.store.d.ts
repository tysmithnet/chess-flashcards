import { IRootState } from ".";
export interface IAction {
    type: string;
}
export declare function getHistory(): import("history").History;
export declare const reducer: import("redux").Reducer<{
    app: import("../app").IRootState;
    auth: import("../auth").IRootState;
    games: import("../games").IRootState;
    home: import("../home").IRootState;
    openings: import("../openings").IRootState;
    playlists: {
        masterList: any;
        viewer: any;
    };
    router: import("connected-react-router").RouterState;
}, import("redux").AnyAction>;
export declare const sagaMiddleware: import("redux-saga").SagaMiddleware<{}>;
export declare function configureStore(state: IRootState): import("redux").Store<{
    app: import("../app").IRootState;
    auth: import("../auth").IRootState;
    games: import("../games").IRootState;
    home: import("../home").IRootState;
    openings: import("../openings").IRootState;
    playlists: {
        masterList: any;
        viewer: any;
    };
    router: import("connected-react-router").RouterState;
}, import("redux").AnyAction> & {
    dispatch: {};
};
