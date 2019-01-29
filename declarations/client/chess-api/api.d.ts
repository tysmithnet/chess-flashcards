/// <reference path="../../../src/client/chess-api/custom.d.ts" />
import { Configuration } from "./configuration";
export declare const COLLECTION_FORMATS: {
    csv: string;
    ssv: string;
    tsv: string;
    pipes: string;
};
export interface FetchAPI {
    (url: string, init?: any): Promise<Response>;
}
export interface FetchArgs {
    url: string;
    options: any;
}
export declare class BaseAPI {
    protected basePath: string;
    protected fetch: FetchAPI;
    protected configuration: Configuration;
    constructor(configuration?: Configuration, basePath?: string, fetch?: FetchAPI);
}
export declare class RequiredError extends Error {
    field: string;
    name: "RequiredError";
    constructor(field: string, msg?: string);
}
export interface ApiResponse {
    code?: number;
    type?: string;
    message?: string;
}
export interface Move {
    piece: string;
    src: string;
    dst: string;
    isCheck?: boolean;
    isMate?: boolean;
    isStalemate?: boolean;
    isEnpessant?: boolean;
    isCastle?: boolean;
    capturedPiece?: string;
}
export interface Opening {
    name: string;
    id: string;
    moves: Array<Move>;
}
export declare const DefaultApiFetchParamCreator: (configuration?: Configuration) => {
    movesGet(fen: string, flags?: string[], options?: any): FetchArgs;
    openingsGet(options?: any): FetchArgs;
    openingsIdGet(id: string, options?: any): FetchArgs;
    openingsSearchGet(term: string, options?: any): FetchArgs;
};
export declare const DefaultApiFp: (configuration?: Configuration) => {
    movesGet(fen: string, flags?: string[], options?: any): (fetch?: FetchAPI, basePath?: string) => Promise<Move[]>;
    openingsGet(options?: any): (fetch?: FetchAPI, basePath?: string) => Promise<Opening[]>;
    openingsIdGet(id: string, options?: any): (fetch?: FetchAPI, basePath?: string) => Promise<Opening[]>;
    openingsSearchGet(term: string, options?: any): (fetch?: FetchAPI, basePath?: string) => Promise<Opening[]>;
};
export declare const DefaultApiFactory: (configuration?: Configuration, fetch?: FetchAPI, basePath?: string) => {
    movesGet(fen: string, flags?: string[], options?: any): Promise<Move[]>;
    openingsGet(options?: any): Promise<Opening[]>;
    openingsIdGet(id: string, options?: any): Promise<Opening[]>;
    openingsSearchGet(term: string, options?: any): Promise<Opening[]>;
};
export declare class DefaultApi extends BaseAPI {
    movesGet(fen: string, flags?: Array<string>, options?: any): Promise<Move[]>;
    openingsGet(options?: any): Promise<Opening[]>;
    openingsIdGet(id: string, options?: any): Promise<Opening[]>;
    openingsSearchGet(term: string, options?: any): Promise<Opening[]>;
}