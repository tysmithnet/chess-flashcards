import { combineReducers } from "redux";
import { reducer as app } from "../app";
import { reducer as auth } from "../auth";
import { reducer as games } from "../games";
import { reducer as moves } from "../moves";
import { reducer as openings } from "../openings";

export const reducer = combineReducers({
    app,
    auth,
    openings,
    moves,
    games,
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
