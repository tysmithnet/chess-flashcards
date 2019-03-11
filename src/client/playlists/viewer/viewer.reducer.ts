import { IAction } from "../../root";
import { IRootState } from "./viewer.domain";

export function reducer(state: IRootState, action: IAction): IRootState {
    switch (action.type) {
        case "sayhello":
            console.log("hi!");
            break;
    }
    return {
        ...state,
    };
}
