import { connectRouter, routerMiddleware } from "connected-react-router";
import { createBrowserHistory, createMemoryHistory } from "history";
import { applyMiddleware, combineReducers, compose, createStore } from "redux";
import loggerMiddleware from "redux-logger";
import createSagaMiddleware from "redux-saga";
import { IRootState } from ".";
import { reducer as app } from "../app";
import { reducer as auth } from "../auth";
import { reducer as games } from "../games";
import { reducer as moves } from "../moves";
import { reducer as openings } from "../openings";

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

// You cannot use browser history in jest tests or in storybook
const dynamic = global as any;
const history = dynamic.jasmine || dynamic.STORYBOOK_ENV
    ? createMemoryHistory()
    : createBrowserHistory();

export function getHistory() {
    return history;
}

export const reducer = combineReducers({
    app,
    auth,
    openings,
    moves,
    games,
    router: connectRouter(history),
});

/**
 * The saga middleware
 */
export const sagaMiddleware = createSagaMiddleware();

export function configureStore(state: IRootState) {
    return createStore(
        reducer,
        state,
        compose(
            applyMiddleware(
                routerMiddleware(history),
                loggerMiddleware,
                sagaMiddleware),
        ),
    );
}
