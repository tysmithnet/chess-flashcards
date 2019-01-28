import {Opening as IOpening} from "../chess-api/api";
import { IBaseProps } from "../root";

export interface IProps extends IBaseProps {
    openings: IOpening[];
}

export interface IRootState {
    openings: IOpening[];
}
