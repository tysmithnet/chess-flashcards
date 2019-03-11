import { IOpening, IOpeningMeta } from "../root";

export interface IRootState {
    meta: IOpeningMeta[];
    openings: IOpening[];
}
