import { IOpening } from "../root";

export interface IRootState {
    openings: IOpening[];
}

export interface IPreset {
    name: string;
    get: (openings: IOpening[]) => string[];
}
