import {match, RouteComponentProps} from "react-router";
import {Opening as IOpening, OpeningMeta as IOpeningMeta} from "../chess-api/api";
import { IBaseProps } from "../root";

export interface IParams {
    id: string;
}

export interface IProps extends IBaseProps {
    openingMetaData: IOpeningMeta[];
    match?: match<any>;
}

export interface IRootState {
    openingMetaData: IOpeningMeta[];
    openings: IOpening[];
}
