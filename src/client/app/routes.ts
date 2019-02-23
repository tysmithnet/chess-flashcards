import { Admin } from "../admin";
import { Permissions } from "../auth";
import { connectedComponent as Games } from "../games";
import { connectedComponent as Home } from "../home";
import { connectedComponent as Moves } from "../moves/Moves";
import { connectedComponent as Openings } from "../openings/Openings";

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
        permissions: [Permissions.get("ADMIN")],
    },
    {
        component: Openings,
        display: "Openings Flashcards",
        exact: true,
        path: "/openings",
        permissions: [],
    },
    {
        component: Moves,
        display: "Threats",
        exact: true,
        path: "/threats",
        permissions: [],
    },
    {
        component: Games,
        display: "Game Flashcards",
        exact: true,
        path: "/games",
        permissions: [],
    },
];
