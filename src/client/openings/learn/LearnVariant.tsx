import * as React from "react";
import { connect } from "react-redux";
import { match, Route, RouteComponentProps } from "react-router";
import { Link } from "react-router-dom";
import {Opening as IOpening} from "../../chess-api";
import { IBaseProps, IRootState } from "../../root";

export interface IProps extends IBaseProps {
    match?: match<any>;
    openings: IOpening[];
}

export class LearnVariant extends React.Component<IProps> {
    constructor(props: IProps) {
        super(props);
    }
    public render() {
        return <h1>hi {this.props.match.params.id} - {this.props.match.params.name}</h1>;
    }
}

function mapStateToProps(state: IRootState): IProps {
    return {
       openings: state.openings.openings,
    };
}

export const connectedComponent = connect(mapStateToProps)(LearnVariant);
