import {match, RouteComponentProps} from "react-router";
import {OpeningMeta as IOpeningMeta} from "../chess-api/api";
import { IBaseProps } from "../root";

export interface IParams {
    id: string;
}

export interface IProps extends IBaseProps {
    openings: IOpeningMeta[];
    match?: match<any>;
}

export interface IRootState {
    openings: IOpeningMeta[];
}
