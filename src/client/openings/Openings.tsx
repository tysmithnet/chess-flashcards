import * as React from "react";
import { connect } from "react-redux";
import { Link, Route, Switch } from "react-router-dom";
import { bindActionCreators } from "redux";
import { Opening as IOpening } from "../chess-api";
import { IRootState } from "../root";
import {connectedComponent as DiscoverOpenings } from "./discover";
import { connectedComponent as LearnOpenings } from "./learn";
import { getAllOpeningsRequestFactory } from "./openings.actions";
import { IProps } from "./openings.domain";
import "./openings.styles";

export class Openings extends React.Component<IProps> {

    constructor(props: IProps) {
        super(props);
    }

    public render() {
        return (
            <div className="openings">
                <div className="links">
                    <Link to={"/openings/learn"}>Learn</Link>
                    <Link to={"/openings/discover"}>Discover</Link>
                    <Link to={"/openings/quiz"}>Quiz</Link>
                </div>
                <Route path={"/openings/learn"} component={LearnOpenings} />
                <Route path={"/openings/discover"} component={DiscoverOpenings} />
            </div>
        );
    }

    public componentDidMount() {
        this.props.dispatch(getAllOpeningsRequestFactory());
    }
}

function mapStateToProps(state: IRootState): IProps {
    let val: IOpening[] = [];
    if (state.openings) {
        val = state.openings.openings;
    }
    return {
        openings: val,
    };
}

export const connectedComponent = connect(mapStateToProps)(Openings);
