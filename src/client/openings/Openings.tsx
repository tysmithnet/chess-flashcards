import * as React from "react";
import { connect } from "react-redux";
import { Opening } from "../chess-api";
import {IRootState} from "./openings.domain";

export interface IProps {
    openings: Opening[];
    selectedOpenings: Opening[];
}

export interface IState {
    searchTerm: string;
}

export class Openings extends React.Component<IProps> {
    public render() {
        return <h1>Openings Quiz</h1>;
    }
}

function mapStateToProps(state: IRootState): IProps {
    return {
        openings: state.openings,
        selectedOpenings: state.selectedOpenings,
    };
}

export const connectedComponent = connect(mapStateToProps)(Openings);
