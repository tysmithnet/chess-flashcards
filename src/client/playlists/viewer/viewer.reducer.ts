import { IRootState } from ".";
import { IAction } from "../../root";

export function reducer(state: IRootState, action: IAction): IRootState {
    return {
        ...state,
    };
}
