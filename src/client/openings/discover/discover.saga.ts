import axios from "axios";
import {camelArray, camelKeys} from "change-object-case";
import { all, call, put, takeLatest } from "redux-saga/effects";
import {Configuration, DefaultApi, DefaultApiFactory, Move as IMove, Opening as IOpening, OpeningMeta as IOpeningMeta } from "../../chess-api";
import {ACTION_TYPES, IMakeMovesRequest, makeMovesFailureFactory, makeMovesSuccessFactory} from "./discover.actions";

const api = DefaultApiFactory();

function* makeMoves(fen: string, moves: IMove[]) {
    try {
        const nextFen = yield call(api.fenPost, {
            fen,
            moves,
        });
        const nextMoves = yield call(api.movesGet, nextFen);
        yield put(makeMovesSuccessFactory(nextFen, nextMoves));
    } catch (err) {
        yield put(makeMovesFailureFactory(err));
    }
}

function* makeMovesSaga() {
    yield takeLatest(ACTION_TYPES.MAKE_MOVES_REQUEST, (action: IMakeMovesRequest) => {
        return makeMoves(action.fen, action.moves);
    });
}

export function* rootSaga() {
    yield all([makeMovesSaga()]);
}
