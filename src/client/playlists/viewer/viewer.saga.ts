import axios from "axios";
import { camelKeys } from "change-object-case";
import * as _ from "lodash";
import { all, put, select, takeLatest } from "redux-saga/effects";
import { fenToArray } from "../../common/chess";
import { applyMove, IPlaylist, IPosition, IRootState, PlaylistType } from "../../root";
import {
    ACTION_TYPES,
    checkMoveFailureFactory,
    checkMoveSuccessFactory,
    getStatsFailureFactory,
    getStatsRequestFactory,
    getStatsSuccessFactory,
    ICheckMoveRequest,
    IGetStatsRequest,
    ILoadNextItemRequest,
    ILoadNextPositionRequest,
    ILoadPlaylistRequest,
    loadNextItemFailureFactory,
    loadNextItemRequestFactory,
    loadNextItemSuccessFactory,
    loadNextPositionFailureFactory,
    loadNextPositionRequestFactory,
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
        const index = _.random(0, state.playlists.viewer.playlist.ids.length - 1);
        const id = state.playlists.viewer.playlist.ids[index];
        if (state.playlists.viewer.playlist.type === PlaylistType.opening) {
            const dataRes = yield axios.get(`/api/opening/${id}`);
            const data = yield dataRes.data;
            const converted = camelKeys(data);
            yield put(getStatsRequestFactory(PlaylistType.opening, id));
            yield put(loadNextItemSuccessFactory(converted, null));
        } else if (state.playlists.viewer.playlist.type === PlaylistType.game) {
            const res = yield axios.get(`/api/game/${id}`);
            const data = yield res.data;
            const converted = camelKeys(data);
            yield put(getStatsRequestFactory(PlaylistType.game, id));
            yield put(loadNextItemSuccessFactory(null, converted));
        } else {
            yield put(loadNextItemFailureFactory(`Unexpected playlist type: ${state.playlists.viewer.playlist.type}`));
        }
    } catch (err) {
        yield put(loadNextItemFailureFactory(err));
    }
}

function getNextPosition(state: IRootState): IPosition {
    if (state.playlists.viewer.playlist.type === PlaylistType.opening) {
        const index = state.playlists.viewer.opening.positions.indexOf(state.playlists.viewer.position);
        if (index + 1 >= state.playlists.viewer.opening.positions.length) {
            return null;
        }
        const nextPosition = state.playlists.viewer.opening.positions[index + 1];
        return nextPosition;
    } else if (state.playlists.viewer.playlist.type === PlaylistType.game) {
        const index = state.playlists.viewer.game.positions.indexOf(state.playlists.viewer.position);
        if (index + 1 >= state.playlists.viewer.game.positions.length) {
            return null;
        }
        const nextPosition = state.playlists.viewer.game.positions[index + 1];
        return nextPosition;
    } else {
        throw new Error(`Unexpected playlist type: ${state.playlists.viewer.playlist.type}`);
    }
}

function* loadNextPosition(action: ILoadNextPositionRequest) {
    try {
        const state: IRootState = yield select();
        const nextPosition = getNextPosition(state);
        if (nextPosition == null) {
            yield put(loadNextItemRequestFactory());
        }
        yield put(loadNextPositionSuccessFactory(nextPosition));
    } catch (err) {
        yield put(loadNextPositionFailureFactory(err));
    }
}

function* checkMove(action: ICheckMoveRequest) {
    try {
        const state: IRootState = yield select();
        const viewerState = state.playlists.viewer;
        const nextPosition = getNextPosition(state);
        const type = viewerState.playlist.type;
        const id = viewerState.game ? viewerState.game.id : viewerState.opening.id;
        if (!nextPosition) {
            yield axios.post(`/api/stats/${type}/${id}`, {
                success: true,
            });
            yield put(loadNextItemRequestFactory());
        }
        const currentPosition = fenToArray(viewerState.position.pieces);
        const afterMove = applyMove(currentPosition, action.move);
        const correctNextPosition = fenToArray(nextPosition.pieces);
        const isCorrect = _.isEqual(afterMove, correctNextPosition);
        if (isCorrect) {
            yield put(checkMoveSuccessFactory(action.move, true));
            yield put(loadNextPositionRequestFactory());
        } else {
            yield axios.post(`/api/stats/${type}/${id}`, {
                success: false,
            });
            yield put(checkMoveSuccessFactory(action.move, false));
        }
    } catch (err) {
        yield put(checkMoveFailureFactory(err));
    }
}

function* getStats(action: IGetStatsRequest) {
    try {
        const res = yield axios.get(`/api/stats/${action.playlistType}/${action.id}`);
        const data = yield res.data;
        yield put(getStatsSuccessFactory(data.attempts, data.succeses));
    } catch (err) {
        yield put(getStatsFailureFactory(err));
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

function* checkMoveSaga() {
    yield takeLatest(ACTION_TYPES.CHECK_MOVE.REQUEST, checkMove);
}

function* getStatsSaga() {
    yield takeLatest(ACTION_TYPES.GET_STATS.REQUEST, getStats);
}

export function* rootSaga() {
    yield all([loadPlaylistSaga(), loadNextItemSaga(), loadNextPositionSaga(), checkMoveSaga(), getStatsSaga()]);
}
