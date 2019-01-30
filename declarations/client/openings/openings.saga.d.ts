export declare function getAllOpeningsSaga(): IterableIterator<import("redux-saga/effects").ForkEffect>;
export declare function getOpeningDetail(id: string): IterableIterator<import("redux-saga/effects").PutEffect<import("src/client/openings/openings.actions").IGetAllOpeningsSuccess> | import("axios").AxiosPromise<any> | import("redux-saga/effects").PutEffect<import("src/client/openings/openings.actions").IGetAllOpeningsFailure>>;
export declare function getOpeningDetailSaga(): IterableIterator<import("redux-saga/effects").ForkEffect>;
export declare function rootSaga(): IterableIterator<import("redux-saga/effects").GenericAllEffect<IterableIterator<import("redux-saga/effects").ForkEffect>>>;
