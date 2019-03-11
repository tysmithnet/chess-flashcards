import axios from "axios";
import cleanDeep from "clean-deep";
import { all, put, takeLatest } from "redux-saga/effects";
import { PlaylistType } from "../root";
import {
    ACTION_TYPES,
    createPlaylistFailureFactory,
    createPlaylistSuccessFactory,
    getPlaylistFailureFactory,
    getPlaylistRequestFactory,
    getPlaylistSuccessFactory,
    ICreatePlaylistRequest,
    IGetPlaylistRequest,
    IUpdatePlaylistRequest,
    updatePlaylistFailureFactory} from "./playlists.actions";

function* getPlaylistMeta(action: IGetPlaylistRequest) {
    try {
        let url = "/api/playlist";
        if (action.playlistType === "opening") {
            url = "/api/playlist/opening";
        }
        if (action.playlistType === "game") {
            url = "/api/playlist/game";
        }
        if (action.playlistType && action.id != null) {
            url = `${url}/${action.id}`;
        }
        const res = yield axios.get(url);
        const data = yield res.data;
        const games = [];
        const openings = [];
        if (action.playlistType && action.id != null) {
            if (action.playlistType === "opening") {
                openings.push(data);
            }
            if (action.playlistType === "game") {
                games.push(data);
            }
            yield put(getPlaylistSuccessFactory(games, openings));
        } else {
            yield put(getPlaylistSuccessFactory(data.game, data.opening));
        }
    } catch (err) {
        yield put(getPlaylistFailureFactory(err));
    }
}

function* createPlaylist(action: ICreatePlaylistRequest) {
    let url = "/api/playlist/opening";
    if (action.playlistType === PlaylistType.game) {
        url = "/api/playlist/game";
    }
    try {
        const res = yield axios.post(url, {
            name: action.name,
            ids: action.ids,
        });
        const data = yield res.data as any;
        yield put(createPlaylistSuccessFactory({
            id: data.id,
            type: action.playlistType,
            name: data.name,
            ids: data.ids,
        }));
    } catch (err) {
        yield put(createPlaylistFailureFactory());
    }
 }

function* updatePlaylist(action: IUpdatePlaylistRequest) {
    try {
        let url = null;
        switch (action.playlistType) {
            case PlaylistType.opening:
                url = `/api/playlist/opening/${action.id}`;
                break;
            case PlaylistType.game:
                url = `/api/playlist/game/${action.id}`;
                break;
        }
        const data = cleanDeep({
            name: action.name,
            ids: action.ids,
        }, {
            emptyArrays: false,
        });
        const res = yield axios.put(url, data);
        yield put(getPlaylistRequestFactory());
    } catch (err) {
        yield put(updatePlaylistFailureFactory(err));
    }
}

function* getPlaylistMetaSaga() {
    yield takeLatest(ACTION_TYPES.GET_PLAYLIST.REQUEST, getPlaylistMeta);
}

function* createPlaylistSaga() {
    yield takeLatest(ACTION_TYPES.CREATE_PLAYLIST.REQUEST, createPlaylist);
}

function* updatePlaylistSaga() {
    yield takeLatest(ACTION_TYPES.UPDATE_PLAYLIST.REQUEST, updatePlaylist);
}

export function* rootSaga() {
    yield all([getPlaylistMetaSaga(), createPlaylistSaga(), updatePlaylistSaga()]);
}
