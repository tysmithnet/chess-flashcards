import * as React from "react";
import { connect } from "react-redux";
import { Board, STARTING_POSITION } from "../board/Board";
import { IBaseProps, IRootState } from "../root";
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
                    <Board darkSquareColor={"#b58863"} lightSquareColor={"#f0d9b5"} position={STARTING_POSITION} legalMoves={[]} />
                </div>
            </div>
        );
    }
}

function mapStateToProps(state: IRootState): IBaseProps {
    return {};
}

export const connectedComponent = connect(mapStateToProps)(Home);
