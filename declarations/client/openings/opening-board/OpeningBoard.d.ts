import * as React from "react";
import { Move as IMove } from "../../chess-api";
export interface IProps {
    moves: IMove[];
}
export declare const OpeningBoard: React.SFC<IProps>;
