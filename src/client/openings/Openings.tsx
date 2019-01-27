import {Chessground} from "chessground";
import {Api as IChessground} from "chessground/api";
import * as React from "react";
import { connect } from "react-redux";
import { IBaseProps, IRootState } from "../root";
import "./openings.styles";
export class Openings extends React.Component<IBaseProps> {
    private ref: React.RefObject<HTMLDivElement>;
    private ground: IChessground;
    constructor(props: IBaseProps) {
        super(props);
        this.ref = React.createRef();
    }

    public render() {
        return (
            <div className="board" ref={this.ref} />
        );
    }

    public componentDidMount() {
        this.ground = Chessground(this.ref.current, {
            fen: "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
        });
    }

    public componentWillUnmount() {
        this.ground.destroy();
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
