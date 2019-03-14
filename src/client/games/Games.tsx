import * as React from "react";
import { connect } from "react-redux";
import { getOpeningMetaRequestFactory } from "../openings";
import { IBaseProps, IGameMeta, IRootState } from "../root";

export interface IProps extends IBaseProps {
    meta: IGameMeta[];
}

export class Games extends React.Component<IProps> {
    constructor(props: IProps) {
        super(props);
    }

    public render() {
        return <h1>GAMES!</h1>;
    }

    public componentDidMount() {
        this.props.dispatch(getOpeningMetaRequestFactory());
    }
}

function mapStateToProps(state: IRootState): IProps {
    return {
        meta: state.games.meta,
    };
}

export const connectedComponent = connect(mapStateToProps)(Games);
