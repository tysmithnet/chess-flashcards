import axios from "axios";
import { all, takeLatest } from "redux-saga/effects";
import { ACTION_TYPES } from "./playlists.actions";

function* getPlaylistMeta() {
    return null;
}

export function* getPlaylistMetaSaga() {
    yield takeLatest(ACTION_TYPES.PLAYLIST_META.REQUEST, () => {
        return getPlaylistMeta();
    });
}

export function* rootSaga() {
    yield all([getPlaylistMetaSaga()]);
}
