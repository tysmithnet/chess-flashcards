import * as React from "react";
import { connect } from "react-redux";
import { Link, Route, Switch } from "react-router-dom";
import { bindActionCreators } from "redux";
import {OpeningMeta as IOpeningMeta} from "../chess-api";
import {Board} from "../common/board";
import { IState } from "../menu/menu.domain";
import { IRootState } from "../root";
import {connectedComponent as Learn} from "./learn";
import { getAllOpeningsRequestFactory } from "./openings.actions";
import {IProps} from "./openings.domain";
import "./openings.styles";

export class Openings extends React.Component<IProps> {

    constructor(props: IProps) {
        super(props);
    }

    public render() {
        return (
            <div>
                <Link to={"/openings/learn"}>Learn</Link>
                <Route path={"/openings/learn"} component={Learn} />
            </div>
        );
    }

    public componentDidMount() {
        this.props.dispatch(getAllOpeningsRequestFactory());
    }
}

function mapStateToProps(state: IRootState): IProps {
    let val: IOpeningMeta[] = [];
    if (state.openings) {
        val = state.openings.openingMetaData;
    }
    return {
       openingMetaData: val,

    };
}

export const connectedComponent = connect(mapStateToProps)(Openings);
