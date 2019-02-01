import { Key, Piece } from "chessground/types";
import * as React from "react";
import { connect } from "react-redux";
import { Move as IMove, Opening as IOpening } from "../../chess-api";
import { Board, STARTING_FEN } from "../../common/board";
import { IBaseProps, IRootState } from "../../root";
import { makeMovesRequestFactory } from "./discover.actions";
import { IProps } from "./discover.domain";

export class DiscoverOpenings extends React.Component<IProps> {
    constructor(props: IProps) {
        super(props);
        this.handleOnMove = this.handleOnMove.bind(this);
    }

    public render() {
        return <Board fen={this.props.fen} onMove={this.handleOnMove} />;
    }

    public componentDidMount() {
        this.props.dispatch(makeMovesRequestFactory(STARTING_FEN, []));
    }

    private handleOnMove(src: Key, dst: Key, capturedPiece?: Piece) {
        console.log(`MOVED ${src} -> ${dst}`);
    }
}

function mapStateToProps(state: IRootState): IProps {
    let val: IOpening[] = [];
    let fen = STARTING_FEN;
    let moves: IMove[] = [];
    if (state.openings) {
        val = state.openings.openings;
        if (state.openings.discover) {
            fen = state.openings.discover.fen;
            moves = state.openings.discover.legalMoves;
        }
    }
    return {
        openings: val,
        fen,
        legalMoves: moves,
    };
}

export const connectedComponent = connect(mapStateToProps)(DiscoverOpenings);
