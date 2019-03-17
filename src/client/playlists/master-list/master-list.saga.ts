import axios from "axios";
import cleanDeep from "clean-deep";
import { push } from "connected-react-router";
import { all, put, takeLatest } from "redux-saga/effects";
import { PlaylistType } from "../../root";
import { resetRequestFactory } from "../viewer";
import {
    ACTION_TYPES,
    createPlaylistFailureFactory,
    createPlaylistSuccessFactory,
    deletePlaylistsFailureFactory,
    deletePlaylistsSuccessFactory,
    getPlaylistFailureFactory,
    getPlaylistRequestFactory,
    getPlaylistSuccessFactory,
    ICreatePlaylistRequest,
    IDeletePlaylistsRequest,
    IGetPlaylistRequest,
    IUpdatePlaylistRequest,
    IViewPlaylistRequest,
    updatePlaylistFailureFactory,
    viewPlaylistFailureFactory} from "./master-list.actions";

function* getPlaylist(action: IGetPlaylistRequest) {
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

function* viewPlaylist(action: IViewPlaylistRequest) {
    try {
        yield put(resetRequestFactory());
        yield put(push(`/playlists/${action.playlist.type}/${action.playlist.id}`));
    } catch (err) {
        yield put(viewPlaylistFailureFactory(err));
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
        yield put(getPlaylistRequestFactory());
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

function* deletePlaylists(action: IDeletePlaylistsRequest) {
    try {
        const games = action.playlists.filter(p => p.type === PlaylistType.game).map(p => p.id);
        const openings = action.playlists.filter(p => p.type === PlaylistType.opening).map(p => p.id);
        const reqs = [];
        if (games.length) {
            const req = axios.delete("/api/playlist/game", {
                data: {
                    ids: games,
                },
            });
            reqs.push(req);
        }
        if (openings.length) {
            const req = axios.delete("/api/playlist/opening", {
                data: {
                    ids: openings,
                },
            });
            reqs.push(req);
        }
        yield all(reqs);
        yield put(deletePlaylistsSuccessFactory());
        yield put(getPlaylistRequestFactory());
    } catch (err) {
        yield put(deletePlaylistsFailureFactory(err));
    }
}

function* getPlaylistSaga() {
    yield takeLatest(ACTION_TYPES.GET_PLAYLIST.REQUEST, getPlaylist);
}

function* viewPlaylistSaga() {
    yield takeLatest(ACTION_TYPES.VIEW_PLAYLIST.REQUEST, viewPlaylist);
}

function* createPlaylistSaga() {
    yield takeLatest(ACTION_TYPES.CREATE_PLAYLIST.REQUEST, createPlaylist);
}

function* updatePlaylistSaga() {
    yield takeLatest(ACTION_TYPES.UPDATE_PLAYLIST.REQUEST, updatePlaylist);
}

function* deletePlaylistsSaga() {
    yield takeLatest(ACTION_TYPES.DELETE_PLAYLISTS.REQUEST, deletePlaylists);
}

export function* rootSaga() {
    yield all([getPlaylistSaga(), viewPlaylistSaga(), createPlaylistSaga(), updatePlaylistSaga(), deletePlaylistsSaga()]);
}
