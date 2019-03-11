import { combineReducers } from "redux";
import { reducer as masterList } from "./master-list";
import { reducer as viewer } from "./viewer";

export const reducer = combineReducers({
    masterList,
    viewer,
});
