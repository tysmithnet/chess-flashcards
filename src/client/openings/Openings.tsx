import * as React from "react";
import { connect } from "react-redux";
import { DEFAULT_POSITION } from "../../shared/domain";
import {Board} from "../common/board/Board";
import { IBaseProps, IRootState } from "../root";
import "./openings.styles";
export class Openings extends React.Component<IBaseProps> {

    constructor(props: IBaseProps) {
        super(props);
    }

    public render() {
        return (
            <div className="board">
                <Board lightSquareColor={"#EFDAB5"} darkSquareColor={"#B68762"} lightPieceColor={"white"} darkPieceColor={"black"} pieceLocations={DEFAULT_POSITION.pieces} />
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
