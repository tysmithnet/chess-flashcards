export declare function getAllOpeningsSaga(): IterableIterator<import("@redux-saga/types").SimpleEffect<"FORK", import("redux-saga/effects").ForkEffectDescriptor>>;
export declare function rootSaga(): IterableIterator<import("@redux-saga/types").CombinatorEffect<"ALL", IterableIterator<import("@redux-saga/types").SimpleEffect<"FORK", import("redux-saga/effects").ForkEffectDescriptor>>>>;
