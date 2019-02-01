import { IAction } from "../root";
import { IRootState } from "./openings.domain";
export declare function openingsReducer(state: IRootState, action: IAction): IRootState;
export declare const reducer: import("redux").Reducer<{
    openingsReducer: IRootState;
    discoverReducer: import("src/client/root/root.domain").IRootState;
}, import("redux").AnyAction>;
