import * as React from "react";
import { connect } from "react-redux";
import { IBaseProps, IMove, IRootState } from "../root";

export interface IMoveCollection {
    position: string[];
    checks: IMove[];
    captures: IMove[];
    legalMoves: IMove[];
    checkmates: IMove[];
    stalemates: IMove[];
}

export interface IProps extends IBaseProps {
    position: string[];
}

export interface IState {

}

export class Moves extends React.Component<IBaseProps, IState> {
    public render() {
        return <h1>THREATS!</h1>;
    }
}

function mapStateToProps(state: IRootState): IProps {
    return {
        position: null,
    };
}

export const connectedComponent = connect(mapStateToProps)(Moves);
