import {Move as IMove, Opening as IOpening, OpeningVariant as IOpeningVariant} from "../../chess-api";
import { IBaseProps } from "../../root";

export interface IProps extends IBaseProps {
    matchingVariants: IOpeningVariant[];
    fen: string;
    legalMoves: IMove[];
}

export interface IRootState {
    fen: string;
    legalMoves: IMove[];
    discoveredOpenings: IOpening[];
}
