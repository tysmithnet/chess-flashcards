import { combineReducers } from "redux";
import { reducer as app } from "../app";
import { reducer as auth } from "../auth";
import { reducer as common } from "../openings";
import { reducer as discover } from "../openings/discover";

export const reducer = combineReducers({
    app,
    auth,
    openings: combineReducers({
        common,
        discover,
    }),
});

/**
 * Base interface for actions
 *
 * @export
 * @interface IAction
 */
export interface IAction {
    /**
     * Identifying type name for the action
     *
     * @type {string}
     * @memberof IAction
     */
    type: string;
}
