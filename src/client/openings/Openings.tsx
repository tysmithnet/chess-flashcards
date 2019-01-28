import * as React from "react";
import { connect } from "react-redux";
import {Opening as IOpening} from "../chess-api/api";
import {Board} from "../common/board";
import { IBaseProps, IRootState } from "../root";
import "./openings.styles";

export class Openings extends React.Component<IBaseProps> {
    private openings: IOpening[] = [];

    constructor(props: IBaseProps) {
        super(props);
    }

    public render() {
        const options = this.openings.map(x => {
            return <option key={x.id} value={x.id}>{x.name}</option>;
        });
        return (
            <div>
                <div className="board">
                    <Board />
                </div>
                <div>
                    <select>
                        {options}
                    </select>
                </div>
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
