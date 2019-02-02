import {Move as IMove, Opening as IOpening} from "../../chess-api";
import { IBaseProps } from "../../root";

export interface IProps extends IBaseProps {
    openings: IOpening[];
    fen: string;
    legalMoves: IMove[];
}

export interface IRootState {
    fen: string;
    legalMoves: IMove[];
    discoveredOpenings: IOpening[];
}
