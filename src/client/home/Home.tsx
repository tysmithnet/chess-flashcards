import * as React from "react";
import { connect } from "react-redux";
import { Board } from "../board/Board";
import { IBaseProps, IRootState, STARTING_POSITION } from "../root";
import "./home.styles";

export class Home extends React.Component {
    public render() {
        return (
            <div className="home">
                <div className="jumbo">
                    <h1>Chess Quiz</h1>
                    <p>Practice your chess openings, and quiz yourself on best moves, checks, captures, and more!</p>
                </div>
                <div className="board">
                    <Board position={STARTING_POSITION} legalMoves={[]} />
                </div>
            </div>
        );
    }
}

function mapStateToProps(state: IRootState): IBaseProps {
    return {};
}

export const connectedComponent = connect(mapStateToProps)(Home);
