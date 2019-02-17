import * as Fuse from "fuse.js";
import { IOpening } from "../root";
export interface IPreset {
    title: string;
    getSelectedOpenings: (openings: IOpening[]) => string[];
}

export const PRESETS: IPreset[] = [
    {
        title: "Ruy Lopez",
        getSelectedOpenings: (openings: IOpening[]) => {
            const fuse = new Fuse(openings, {
                keys: ["variantName"],
                id: "id",
                threshold: 0.2,
            });
            return fuse.search("ruy lopez");
        },
    },
];
