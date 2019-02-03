import axios from "axios";
import { camelArray, camelKeys } from "change-object-case";
import { all, call, put, takeLatest } from "redux-saga/effects";
import { Configuration, DefaultApi, DefaultApiFactory, Move as IMove, Opening as IOpening } from "../../chess-api";
import { STARTING_FEN } from "../../common/board";
import { getOpeningDetailSuccessFactory } from "../openings.actions";
import { ACTION_TYPES, IMakeMovesRequest, IMatchOpeningsRequest, makeMovesFailureFactory, makeMovesSuccessFactory, matchOpeningsFailureFactory, matchOpeningsRequestFactory, matchOpeningsSuccessFactory } from "./discover.actions";

const api = DefaultApiFactory();

function* makeMoves(fen: string, moves: IMove[]) {
    try {
        const nextFen = yield call(api.fenPost, {
            fen,
            moves,
        });
        const nextMoves = yield call(api.movesGet, nextFen);
        yield all([put(makeMovesSuccessFactory(nextFen, nextMoves)), put(matchOpeningsRequestFactory(nextFen))]);
    } catch (err) {
        yield put(makeMovesFailureFactory(err));
    }
}

function* makeMovesSaga() {
    yield takeLatest(ACTION_TYPES.MAKE_MOVES_REQUEST, (action: IMakeMovesRequest) => {
        return makeMoves(action.fen, action.moves);
    });
}

function* matchOpenings(fen: string) {
    try {
        if (fen === STARTING_FEN) {
            yield put(matchOpeningsSuccessFactory([]));
        } else {
            const openings = yield call(api.openingsMatchGet, fen);
            yield put(matchOpeningsSuccessFactory(openings));
            for (const opening of openings) {
                yield put(getOpeningDetailSuccessFactory(opening));
            }
        }
    } catch (err) {
        yield put(matchOpeningsFailureFactory(err));
    }
}

function* matchOpeningsSaga() {
    yield takeLatest(ACTION_TYPES.MATCH_OPENINGS_REQUEST, (action: IMatchOpeningsRequest) => {
        return matchOpenings(action.fen);
    });
}

export function* rootSaga() {
    yield all([makeMovesSaga(), matchOpeningsSaga()]);
}
