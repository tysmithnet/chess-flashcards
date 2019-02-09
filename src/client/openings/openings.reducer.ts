import { IAction } from "../root";
import { IRootState } from "./openings.domain";

export function reducer(state: IRootState, action: IAction): IRootState {
    switch (action.type) {
    }
    return { ...state };
}
