import { IAction } from "../../root";
import { IMakeMovesSuccess } from "./discover.actions";
import { IRootState } from "./discover.domain";
export declare function handleMakeMovesSuccess(state: IRootState, action: IMakeMovesSuccess): IRootState;
export declare function reducer(state: IRootState, action: IAction): IRootState;
