import { IPermission } from "../auth";
export interface IRootState {
    routes: IRoute[];
}
export interface IRoute {
    component: React.ComponentClass;
    display: string;
    exact: boolean;
    path: string;
    permissions: IPermission[];
}
