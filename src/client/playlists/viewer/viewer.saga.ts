import axios from "axios";
import { camelKeys } from "change-object-case";
import { random } from "lodash";
import { all, put, select, takeLatest } from "redux-saga/effects";
import { IPlaylist, IRootState, PlaylistType } from "../../root";
import {
    ACTION_TYPES,
    ILoadNextItemRequest,
    ILoadNextPositionRequest,
    ILoadPlaylistRequest,
    loadNextItemFailureFactory,
    loadNextItemRequestFactory,
    loadNextItemSuccessFactory,
    loadNextPositionFailureFactory,
    loadNextPositionSuccessFactory,
    loadPlaylistFailureFactory,
    loadPlaylistSuccessFactory} from "./viewer.actions";

function* loadPlaylist(action: ILoadPlaylistRequest) {
    try {
        if (action.playlistType === PlaylistType.opening) {
            const res = yield axios.get(`/api/playlist/opening/${action.id}`);
            const data = yield res.data;
            const converted = camelKeys(data) as IPlaylist;
            yield put(loadPlaylistSuccessFactory(converted));
            return;
        } else if (action.playlistType === PlaylistType.game) {
            const res = yield axios.get(`/api/playlist/game/${action.id}`);
            const data = yield res.data;
            const converted = camelKeys(data) as IPlaylist;
            yield put(loadPlaylistSuccessFactory(converted));
            return;
        } else {
            yield put(loadPlaylistFailureFactory(`Unexpected playlist type: ${action.playlistType}`));
        }
    } catch (err) {
        yield put(loadPlaylistFailureFactory(err));
    }
}

function* loadNextItem(action: ILoadNextItemRequest) {
    try {
        const state: IRootState = yield select();
        const index = random(0, state.playlists.viewer.playlist.ids.length - 1);
        const id = state.playlists.viewer.playlist.ids[index];
        if (state.playlists.viewer.playlist.type === PlaylistType.opening) {
            const res = yield axios.get(`/api/opening/${id}`);
            const data = yield res.data;
            const converted = camelKeys(data);
            yield put(loadNextItemSuccessFactory(converted, null));
        } else if (state.playlists.viewer.playlist.type === PlaylistType.game) {
            const res = yield axios.get(`/api/game/${id}`);
            const data = yield res.data;
            const converted = camelKeys(data);
            yield put(loadNextItemSuccessFactory(null, converted));
        } else {
            yield put(loadNextItemFailureFactory(`Unexpected playlist type: ${state.playlists.viewer.playlist.type}`));
        }
    } catch (err) {
        yield put(loadNextItemFailureFactory(err));
    }
}

function* loadNextPosition(action: ILoadNextPositionRequest) {
    try {
        const state: IRootState = yield select();
        if (state.playlists.viewer.playlist.type === PlaylistType.opening) {
            const index = state.playlists.viewer.opening.positions.indexOf(state.playlists.viewer.position);
            if (index + 1 >= state.playlists.viewer.opening.positions.length) {
                yield put(loadNextItemRequestFactory());
                return;
            }
            const nextPosition = state.playlists.viewer.opening.positions[index + 1];
            yield put(loadNextPositionSuccessFactory(nextPosition));
        } else if (state.playlists.viewer.playlist.type === PlaylistType.game) {
            const index = state.playlists.viewer.game.positions.indexOf(state.playlists.viewer.position);
            if (index + 1 >= state.playlists.viewer.game.positions.length) {
                yield put(loadNextItemRequestFactory());
                return;
            }
            const nextPosition = state.playlists.viewer.game.positions[index + 1];
            yield put(loadNextPositionSuccessFactory(nextPosition));
        } else {
            yield put(loadNextPositionFailureFactory(`Unexpected playlist type: ${state.playlists.viewer.playlist.type}`));
        }
    } catch (err) {
        yield put(loadNextPositionFailureFactory(err));
    }
}

function* loadPlaylistSaga() {
    yield takeLatest(ACTION_TYPES.LOAD_PLAYLIST.REQUEST, loadPlaylist);
}

function* loadNextPositionSaga() {
    yield takeLatest(ACTION_TYPES.LOAD_NEXT_POSITION.REQUEST, loadNextPosition);
}

function* loadNextItemSaga() {
    yield takeLatest(ACTION_TYPES.LOAD_NEXT_ITEM.REQUEST, loadNextItem);
}

export function* rootSaga() {
    yield all([loadPlaylistSaga(), loadNextItemSaga(), loadNextPositionSaga()]);
}
