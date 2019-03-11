export interface IRootState {
    user: IUser;
}
export interface IPermission {
    id: string;
    name: string;
    description?: string;
}
export interface IUser {
    id: string;
    username: string;
    permissions: IPermission[];
}
