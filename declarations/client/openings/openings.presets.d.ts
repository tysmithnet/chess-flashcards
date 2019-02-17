import { IOpening } from "../root";
export interface IPreset {
    title: string;
    getSelectedOpenings: (openings: IOpening[]) => string[];
}
export declare const PRESETS: IPreset[];
