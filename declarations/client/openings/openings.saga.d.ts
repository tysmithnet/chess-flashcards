export declare function getAllOpeningsSaga(): IterableIterator<import("redux-saga/effects").ForkEffect>;
export declare function getOpeningDetail(id: string): IterableIterator<import("redux-saga/effects").PutEffect<import("src/client/openings/openings.actions").IGetAllOpeningsSuccess> | import("redux-saga/effects").PutEffect<import("src/client/openings/openings.actions").IGetAllOpeningsFailure> | import("axios").AxiosPromise<any>>;
export declare function getOpeningDetailSaga(): IterableIterator<import("redux-saga/effects").ForkEffect>;
export declare function rootSaga(): IterableIterator<import("redux-saga/effects").GenericAllEffect<IterableIterator<import("redux-saga/effects").ForkEffect>>>;
