import { combineReducers } from "redux";
import { reducer as app } from "../app";
import { reducer as auth } from "../auth";
import { reducer as openings } from "../openings";
import { reducer as openingsDiscover } from "../openings/discover";

export const reducer = combineReducers({
    app,
    auth,
    openings,
    openingsDiscover,
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
