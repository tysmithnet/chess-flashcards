import * as React from "react";
import { connect } from "react-redux";
import { match, Route, RouteComponentProps } from "react-router";
import { Link } from "react-router-dom";
import {Opening as IOpening} from "../../chess-api";
import { IBaseProps, IRootState } from "../../root";
import "./learn.styles";
import { connectedComponent as LearnOpening } from "./LearnOpening";

export interface IProps extends IBaseProps {
    match?: match<any>;
    history?: any;
    openings: IOpening[];
}

export class LearnOpenings extends React.Component<IProps> {

    constructor(props: IProps) {
        super(props);
    }

    public render() {
        const links = (this.props.openings || []).map(o => {
            return <li key={o.id}><Link to={`/openings/learn/${o.id}`}>{o.id} - {o.name}</Link></li>;
        });
        return (
            <div>
                <ul className={"id-list"}>
                    {links}
                </ul>
                <Route path={"/openings/learn/:id"} component={LearnOpening}/>
            </div>
        );
    }
}

function mapStateToProps(state: IRootState): IProps {
    return {
       openings: state.openings.openings,
    };
}

export const connectedComponent = connect(mapStateToProps)(LearnOpenings);
