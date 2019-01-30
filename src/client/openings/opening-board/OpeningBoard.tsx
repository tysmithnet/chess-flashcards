import * as React from "react";
import {Move as IMove} from "../../chess-api";
import {Board} from "../../common/board";

export interface IProps {
    moves: IMove[];
}

const OpeningBoard: React.SFC<IProps> = (props) => {
    return <Board />;
};
