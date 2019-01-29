import {match, RouteComponentProps} from "react-router";
import {Opening as IOpening} from "../chess-api/api";
import { IBaseProps } from "../root";

export interface IParams {
    id: string;
}

export interface IProps extends IBaseProps {
    openings: IOpening[];
    match?: match<any>;
}

export interface IRootState {
    openings: IOpening[];
}
