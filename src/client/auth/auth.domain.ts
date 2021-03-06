/**
 * Root state for the auth domain
 *
 * @export
 * @interface IRootState
 */
export interface IRootState {
    /**
     * User currently logged in
     *
     * @type {IUser}
     * @memberof IRootState
     */
    user: IUser;
}

/**
 * Represents the ability to do something
 *
 * @export
 * @interface IPermission
 */
export interface IPermission {
    /**
     * Unique id for the permission
     *
     * @type {string}
     * @memberof IPermission
     */
    id: string;

    /**
     * User friendly name for the permission
     *
     * @type {string}
     * @memberof IPermission
     */
    name: string;

    /**
     * Short description for the permission
     *
     * @type {string}
     * @memberof IPermission
     */
    description?: string;
}

/**
 * Represents a user account
 *
 * @export
 * @interface IUser
 */
export interface IUser {
    /**
     * Id of the account
     *
     * @type {string}
     * @memberof IUser
     */
    id: string;

    /**
     * Name of the account owner
     *
     * @type {string}
     * @memberof IUser
     */
    username: string;

    /**
     * Permissions associated with the account
     *
     * @type {IPermission[]}
     * @memberof IUser
     */
    permissions: IPermission[];
}
