export declare function getAllOpeningsSaga(): IterableIterator<import("redux-saga/effects").ForkEffect>;
export declare function getOpeningDetail(id: string): IterableIterator<import("redux-saga/effects").CallEffect | import("redux-saga/effects").PutEffect<import("src/client/openings/openings.actions").IGetAllOpeningsFailure> | import("redux-saga/effects").PutEffect<import("src/client/openings/openings.actions").IGetOpeningDetailSuccess>>;
export declare function getOpeningDetailSaga(): IterableIterator<import("redux-saga/effects").ForkEffect>;
export declare function rootSaga(): IterableIterator<import("redux-saga/effects").GenericAllEffect<IterableIterator<import("redux-saga/effects").ForkEffect>>>;
