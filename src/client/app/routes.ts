import { Admin } from "../admin";
import { connectedComponent as Home } from "../home";
import { connectedComponent as Openings } from "../openings";
import { connectedComponent as Playlists } from "../playlists";
import { IRoute } from "./app.domain";
// Implementation note: I find it easier to debug applications when there is a
// central place for all statically defined routes.

/**
 * Navigatable areas of the application
 */
export const routes: IRoute[] = [
    {
        component: Home,
        display: "Home",
        exact: true,
        path: "/",
        permissions: [],
    },
    {
        component: Admin,
        display: "Admin",
        exact: true,
        path: "/admin",
        permissions: [],
    },
    {
        component: Playlists,
        display: "Playlists",
        exact: true,
        path: "/playlists",
        permissions: [],
    },
    {
        component: Openings,
        display: "Openings",
        exact: true,
        path: "/openings",
        permissions: [],
    },
];
