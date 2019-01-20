export declare const reducer: import("redux").Reducer<{
    app: import("src/client/app/app.domain").IRootState;
    auth: import("src/client/auth/auth.domain").IRootState;
}, import("redux").AnyAction>;
export interface IAction {
    type: string;
}
