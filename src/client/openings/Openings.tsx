import * as React from "react";
import { connect } from "react-redux";
import { Link, Route, Switch } from "react-router-dom";
import { bindActionCreators } from "redux";
import {Opening as IOpening} from "../chess-api";
import {Board} from "../common/board";
import { IState } from "../menu/menu.domain";
import { IRootState } from "../root";
import { getAllOpeningsRequestFactory } from "./openings.actions";
import {IProps} from "./openings.domain";
import "./openings.styles";
export class Openings extends React.Component<IProps, IState> {

    constructor(props: IProps) {
        super(props);
    }

    public render() {
        const options = (this.props.openings || []).map(x => {
            return <option key={x.id} value={x.id}>{x.name}</option>;
        });
        return (
            <div>
                <ul>
                    <li><Link to={`/openings/A01`}>ad</Link></li>
                </ul>
                <Route path={`/openings/:ecoId`} component={HelloWorld} />
            </div>
        );
    }

    public componentDidMount() {
        this.props.dispatch(getAllOpeningsRequestFactory());
    }
}

export class HelloWorld extends React.Component<any> {
    public render() {
        return <h1>hi! {this.props.match.params.ecoId}</h1>;
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
