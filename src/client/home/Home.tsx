import * as React from "react";
import { connect } from "react-redux";
import { Board } from "../board/Board";
import { applyMove, IBaseProps, IRootState, STARTING_POSITION } from "../root/root.domain";
import "./home.styles";

export class Home extends React.Component {
    public render() {
        return (
            <h1>hello world</h1>
        );
    }
}

function mapStateToProps(state: IRootState): IBaseProps {
    return {};
}

export const connectedComponent = connect(mapStateToProps)(Home);
