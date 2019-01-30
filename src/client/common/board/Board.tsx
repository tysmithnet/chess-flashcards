import {Chessground} from "chessground";
import {Api as IChessground} from "chessground/api";
import {Config as IConfig} from "chessground/config";
import * as React from "react";
import { IBaseProps } from "../../root";
import "./3d.css";
import "./board.css";
import "./theme.css";

export interface IProps extends IConfig, IBaseProps { }

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
        this.ground.set(nextProps);
    }
}
