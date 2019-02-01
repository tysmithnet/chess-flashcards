import {Chessground} from "chessground";
import {Api as IChessground} from "chessground/api";
import {Config as IConfig} from "chessground/config";
import {Key, Piece} from "chessground/types";
import * as React from "react";
import {Move as IMove} from "../../chess-api";
import { IBaseProps } from "../../root";
import "./3d.css";
import "./board.css";
import "./theme.css";

export interface IProps extends IConfig, IBaseProps {
    moves?: IMove[];
    onMove?: (src: Key, dst: Key, capturedPiece?: Piece) => void;
}

export class Board extends React.Component<IProps> {
    private ref: React.RefObject<HTMLDivElement>;
    private ground: IChessground;
    constructor(props: IBaseProps) {
        super(props);
        this.ref = React.createRef();
    }

    public render() {
        // todo: allow for alternate themes
        return (
            <div className="blue merida">
                <div ref={this.ref} />
            </div>
        );
    }

    public componentDidMount() {
        this.ground = Chessground(this.ref.current, this.props);
    }

    public componentWillUnmount() {
        this.ground.destroy();
    }

    public componentWillReceiveProps(nextProps: IProps) {
        const newProps = {...nextProps};
        if (nextProps.onMove) {
            newProps.events = {...(nextProps.events || {}), move: nextProps.onMove};
        }
        if (nextProps.moves) {
            newProps.movable = {...(nextProps.movable || {}), dests: this.convertMovesToDests(nextProps.moves)};
        }
        this.ground.set(newProps);
    }

    private convertMovesToDests(moves: IMove[]): {[key: string]: Key[]} {
        const res: {[key: string]: Key[]} = {};
        for (const move of moves) {
            if (!res[move.src]) {
                res[move.src] = [];
            }
            res[move.src].push(move.dst as Key);
        }
        return res;
    }
}
