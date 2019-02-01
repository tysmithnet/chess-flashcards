import * as React from "react";
import { connect } from "react-redux";
import { Move as IMove, Opening as IOpening} from "../../chess-api";
import { Board } from "../../common/board";
import { IBaseProps, IRootState } from "../../root";

export interface IProps extends IBaseProps {
    openings: IOpening[];
}

export interface IState {
    fen: string;
    legalMoves: IMove[];
}

export class DiscoverOpenings extends React.Component<IProps> {
    constructor(props: IProps) {
        super(props);
    }

    public render() {
        return <Board />;
    }
}

function mapStateToProps(state: IRootState): IProps {
    let val: IOpening[] = [];
    if (state.openings) {
        val = state.openings.openings;
    }
    return {
        openings: val,
    };
}

export const connectedComponent = connect(mapStateToProps)(DiscoverOpenings);
