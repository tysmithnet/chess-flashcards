import {Chessground} from "chessground";
import {Api as IChessground} from "chessground/api";
import * as React from "react";
import { connect } from "react-redux";
import {Board} from "../common/board";
import { IBaseProps, IRootState } from "../root";
import "./openings.styles";
export class Openings extends React.Component<IBaseProps> {
    constructor(props: IBaseProps) {
        super(props);
    }

    public render() {
        return (
            <div className="board">
                <Board />
            </div>
        );
    }
}

/**
 * Mapping function for the root state
 *
 * @param {IRootState} state
 * @returns {IBaseProps}
 */
function mapStateToProps(state: IRootState): IBaseProps {
    return {};
}

export const connectedComponent = connect(mapStateToProps)(Openings);
