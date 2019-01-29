/// <reference path="./custom.d.ts" />
// tslint:disable
/**
 * chess-flashcards
 * This is an API for chess games, openings, and moves
 *
 * OpenAPI spec version: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */


import * as url from "url";
import * as portableFetch from "portable-fetch";
import { Configuration } from "./configuration";

const BASE_PATH = "https://localhost:5000/api/v1".replace(/\/+$/, "");

/**
 *
 * @export
 */
export const COLLECTION_FORMATS = {
    csv: ",",
    ssv: " ",
    tsv: "\t",
    pipes: "|",
};

/**
 *
 * @export
 * @interface FetchAPI
 */
export interface FetchAPI {
    (url: string, init?: any): Promise<Response>;
}

/**
 *  
 * @export
 * @interface FetchArgs
 */
export interface FetchArgs {
    url: string;
    options: any;
}

/**
 * 
 * @export
 * @class BaseAPI
 */
export class BaseAPI {
    protected configuration: Configuration;

    constructor(configuration?: Configuration, protected basePath: string = BASE_PATH, protected fetch: FetchAPI = portableFetch) {
        if (configuration) {
            this.configuration = configuration;
            this.basePath = configuration.basePath || this.basePath;
        }
    }
};

/**
 * 
 * @export
 * @class RequiredError
 * @extends {Error}
 */
export class RequiredError extends Error {
    name: "RequiredError"
    constructor(public field: string, msg?: string) {
        super(msg);
    }
}

/**
 * Represents a single move that a player can make during a turn
 * @export
 * @interface Move
 */
export interface Move {
    /**
     * The piece being moved, white pieces are indicated by uppercase
     * @type {string}
     * @memberof Move
     */
    piece: string;
    /**
     * The square that the piece was on at the start of the move
     * @type {string}
     * @memberof Move
     */
    src: string;
    /**
     * The square that the piece is on at the end of the move
     * @type {string}
     * @memberof Move
     */
    dst: string;
    /**
     * True if the move results in check, false otherwise
     * @type {boolean}
     * @memberof Move
     */
    isCheck?: boolean;
    /**
     * True if the move results in checkmate, false otherwise
     * @type {boolean}
     * @memberof Move
     */
    isMate?: boolean;
    /**
     * True if the move results in stalemate, false otherwise
     * @type {boolean}
     * @memberof Move
     */
    isStalemate?: boolean;
    /**
     * True if the move was an en pessant capture
     * @type {boolean}
     * @memberof Move
     */
    isEnpessant?: boolean;
    /**
     * True if the move is a castle
     * @type {boolean}
     * @memberof Move
     */
    isCastle?: boolean;
    /**
     * The piece that was captured if one was captured
     * @type {string}
     * @memberof Move
     */
    capturedPiece?: string;
}

/**
 * An ECO chess opening
 * @export
 * @interface Opening
 */
export interface Opening {
    /**
     * The human friendly name for the opening
     * @type {string}
     * @memberof Opening
     */
    name: string;
    /**
     * The ECO id for the opening, e.g. E04
     * @type {string}
     * @memberof Opening
     */
    id: string;
    /**
     * The mainline moves that identify this opening
     * @type {Array&lt;Move&gt;}
     * @memberof Opening
     */
    moves: Array<Move>;
    /**
     * Variants of the opening if any exist
     * @type {Array&lt;OpeningVariant&gt;}
     * @memberof Opening
     */
    variants?: Array<OpeningVariant>;
}

/**
 * A named variation of an ECO opening
 * @export
 * @interface OpeningVariant
 */
export interface OpeningVariant {
    /**
     * The human friendly name for the variant
     * @type {string}
     * @memberof OpeningVariant
     */
    name?: string;
    /**
     * The moves that identify this variant
     * @type {Array&lt;Move&gt;}
     * @memberof OpeningVariant
     */
    moves?: Array<Move>;
}


/**
 * DefaultApi - fetch parameter creator
 * @export
 */
export const DefaultApiFetchParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary Get moves for the given position
         * @param {string} fen FEN of the position to find moves for
         * @param {Array&lt;string&gt;} [flags] Restrict the moves to certain types
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        movesGet(fen: string, flags?: Array<string>, options: any = {}): FetchArgs {
            // verify required parameter 'fen' is not null or undefined
            if (fen === null || fen === undefined) {
                throw new RequiredError('fen','Required parameter fen was null or undefined when calling movesGet.');
            }
            const localVarPath = `/moves`;
            const localVarUrlObj = url.parse(localVarPath, true);
            const localVarRequestOptions = Object.assign({ method: 'GET' }, options);
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            if (fen !== undefined) {
                localVarQueryParameter['fen'] = fen;
            }

            if (flags) {
                localVarQueryParameter['flags'] = flags.join(COLLECTION_FORMATS["csv"]);
            }

            localVarUrlObj.query = Object.assign({}, localVarUrlObj.query, localVarQueryParameter, options.query);
            // fix override query string Detail: https://stackoverflow.com/a/7517673/1077943
            delete localVarUrlObj.search;
            localVarRequestOptions.headers = Object.assign({}, localVarHeaderParameter, options.headers);

            return {
                url: url.format(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary Get all ECO openings
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        openingsGet(options: any = {}): FetchArgs {
            const localVarPath = `/openings`;
            const localVarUrlObj = url.parse(localVarPath, true);
            const localVarRequestOptions = Object.assign({ method: 'GET' }, options);
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            localVarUrlObj.query = Object.assign({}, localVarUrlObj.query, localVarQueryParameter, options.query);
            // fix override query string Detail: https://stackoverflow.com/a/7517673/1077943
            delete localVarUrlObj.search;
            localVarRequestOptions.headers = Object.assign({}, localVarHeaderParameter, options.headers);

            return {
                url: url.format(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary Get an opening and its variants by id
         * @param {string} id ECO id e.g. C42
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        openingsIdGet(id: string, options: any = {}): FetchArgs {
            // verify required parameter 'id' is not null or undefined
            if (id === null || id === undefined) {
                throw new RequiredError('id','Required parameter id was null or undefined when calling openingsIdGet.');
            }
            const localVarPath = `/openings/{id}`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            const localVarUrlObj = url.parse(localVarPath, true);
            const localVarRequestOptions = Object.assign({ method: 'GET' }, options);
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            localVarUrlObj.query = Object.assign({}, localVarUrlObj.query, localVarQueryParameter, options.query);
            // fix override query string Detail: https://stackoverflow.com/a/7517673/1077943
            delete localVarUrlObj.search;
            localVarRequestOptions.headers = Object.assign({}, localVarHeaderParameter, options.headers);

            return {
                url: url.format(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary Fuzzy search for openings
         * @param {string} term Search term to use in search
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        openingsSearchGet(term: string, options: any = {}): FetchArgs {
            // verify required parameter 'term' is not null or undefined
            if (term === null || term === undefined) {
                throw new RequiredError('term','Required parameter term was null or undefined when calling openingsSearchGet.');
            }
            const localVarPath = `/openings/search`;
            const localVarUrlObj = url.parse(localVarPath, true);
            const localVarRequestOptions = Object.assign({ method: 'GET' }, options);
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            if (term !== undefined) {
                localVarQueryParameter['term'] = term;
            }

            localVarUrlObj.query = Object.assign({}, localVarUrlObj.query, localVarQueryParameter, options.query);
            // fix override query string Detail: https://stackoverflow.com/a/7517673/1077943
            delete localVarUrlObj.search;
            localVarRequestOptions.headers = Object.assign({}, localVarHeaderParameter, options.headers);

            return {
                url: url.format(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * DefaultApi - functional programming interface
 * @export
 */
export const DefaultApiFp = function(configuration?: Configuration) {
    return {
        /**
         * 
         * @summary Get moves for the given position
         * @param {string} fen FEN of the position to find moves for
         * @param {Array&lt;string&gt;} [flags] Restrict the moves to certain types
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        movesGet(fen: string, flags?: Array<string>, options?: any): (fetch?: FetchAPI, basePath?: string) => Promise<Array<Move>> {
            const localVarFetchArgs = DefaultApiFetchParamCreator(configuration).movesGet(fen, flags, options);
            return (fetch: FetchAPI = portableFetch, basePath: string = BASE_PATH) => {
                return fetch(basePath + localVarFetchArgs.url, localVarFetchArgs.options).then((response) => {
                    if (response.status >= 200 && response.status < 300) {
                        return response.json();
                    } else {
                        throw response;
                    }
                });
            };
        },
        /**
         * 
         * @summary Get all ECO openings
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        openingsGet(options?: any): (fetch?: FetchAPI, basePath?: string) => Promise<Array<Opening>> {
            const localVarFetchArgs = DefaultApiFetchParamCreator(configuration).openingsGet(options);
            return (fetch: FetchAPI = portableFetch, basePath: string = BASE_PATH) => {
                return fetch(basePath + localVarFetchArgs.url, localVarFetchArgs.options).then((response) => {
                    if (response.status >= 200 && response.status < 300) {
                        return response.json();
                    } else {
                        throw response;
                    }
                });
            };
        },
        /**
         * 
         * @summary Get an opening and its variants by id
         * @param {string} id ECO id e.g. C42
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        openingsIdGet(id: string, options?: any): (fetch?: FetchAPI, basePath?: string) => Promise<Array<Opening>> {
            const localVarFetchArgs = DefaultApiFetchParamCreator(configuration).openingsIdGet(id, options);
            return (fetch: FetchAPI = portableFetch, basePath: string = BASE_PATH) => {
                return fetch(basePath + localVarFetchArgs.url, localVarFetchArgs.options).then((response) => {
                    if (response.status >= 200 && response.status < 300) {
                        return response.json();
                    } else {
                        throw response;
                    }
                });
            };
        },
        /**
         * 
         * @summary Fuzzy search for openings
         * @param {string} term Search term to use in search
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        openingsSearchGet(term: string, options?: any): (fetch?: FetchAPI, basePath?: string) => Promise<Array<Opening>> {
            const localVarFetchArgs = DefaultApiFetchParamCreator(configuration).openingsSearchGet(term, options);
            return (fetch: FetchAPI = portableFetch, basePath: string = BASE_PATH) => {
                return fetch(basePath + localVarFetchArgs.url, localVarFetchArgs.options).then((response) => {
                    if (response.status >= 200 && response.status < 300) {
                        return response.json();
                    } else {
                        throw response;
                    }
                });
            };
        },
    }
};

/**
 * DefaultApi - factory interface
 * @export
 */
export const DefaultApiFactory = function (configuration?: Configuration, fetch?: FetchAPI, basePath?: string) {
    return {
        /**
         * 
         * @summary Get moves for the given position
         * @param {string} fen FEN of the position to find moves for
         * @param {Array&lt;string&gt;} [flags] Restrict the moves to certain types
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        movesGet(fen: string, flags?: Array<string>, options?: any) {
            return DefaultApiFp(configuration).movesGet(fen, flags, options)(fetch, basePath);
        },
        /**
         * 
         * @summary Get all ECO openings
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        openingsGet(options?: any) {
            return DefaultApiFp(configuration).openingsGet(options)(fetch, basePath);
        },
        /**
         * 
         * @summary Get an opening and its variants by id
         * @param {string} id ECO id e.g. C42
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        openingsIdGet(id: string, options?: any) {
            return DefaultApiFp(configuration).openingsIdGet(id, options)(fetch, basePath);
        },
        /**
         * 
         * @summary Fuzzy search for openings
         * @param {string} term Search term to use in search
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        openingsSearchGet(term: string, options?: any) {
            return DefaultApiFp(configuration).openingsSearchGet(term, options)(fetch, basePath);
        },
    };
};

/**
 * DefaultApi - object-oriented interface
 * @export
 * @class DefaultApi
 * @extends {BaseAPI}
 */
export class DefaultApi extends BaseAPI {
    /**
     * 
     * @summary Get moves for the given position
     * @param {} fen FEN of the position to find moves for
     * @param {} [flags] Restrict the moves to certain types
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof DefaultApi
     */
    public movesGet(fen: string, flags?: Array<string>, options?: any) {
        return DefaultApiFp(this.configuration).movesGet(fen, flags, options)(this.fetch, this.basePath);
    }

    /**
     * 
     * @summary Get all ECO openings
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof DefaultApi
     */
    public openingsGet(options?: any) {
        return DefaultApiFp(this.configuration).openingsGet(options)(this.fetch, this.basePath);
    }

    /**
     * 
     * @summary Get an opening and its variants by id
     * @param {} id ECO id e.g. C42
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof DefaultApi
     */
    public openingsIdGet(id: string, options?: any) {
        return DefaultApiFp(this.configuration).openingsIdGet(id, options)(this.fetch, this.basePath);
    }

    /**
     * 
     * @summary Fuzzy search for openings
     * @param {} term Search term to use in search
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof DefaultApi
     */
    public openingsSearchGet(term: string, options?: any) {
        return DefaultApiFp(this.configuration).openingsSearchGet(term, options)(this.fetch, this.basePath);
    }

}

