import { Admin } from "../admin";
import { Permissions } from "../auth";
import { connectedComponent as Home } from "../home";
import { connectedComponent as Openings} from "../openings";
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
        exact: false,
        path: "/admin",
        permissions: [Permissions.get("ADMIN")],
    },
    {
        component: Openings,
        display: "Openings",
        exact: false,
        path: "/openings",
        permissions: [],
    },
];
