import * as React from "react";
import { connect } from "react-redux";
import { match, Route, RouteComponentProps } from "react-router";
import { Link } from "react-router-dom";
import {Opening as IOpening} from "../../chess-api";
import { IBaseProps, IRootState } from "../../root";
import "./learn.styles";
import {connectedComponent as LearnVariant} from "./LearnVariant";

export interface IProps extends IBaseProps {
    match?: match<any>;
    openings: IOpening[];
}

export class LearnOpening extends React.Component<IProps> {
    constructor(props: IProps) {
        super(props);
    }
    public render() {
        const id = this.props.match.params.id;
        if (this.props.openings == null) {
            return <h1>{this.props.match.params.id}</h1>;
        }
        const opening = (this.props.openings || []).filter(o => o.id === id)[0];
        const variants = opening.variants;
        const items = variants.map(v => {
            return <li key={v.name}><Link  to={`/openings/learn/${id}/${v.name}`}>{v.name}</Link></li>;
        });
        return (
            <div>
                <h1>{this.props.match.params.id}</h1>
                <ul>
                    {items}
                </ul>
                <Route path={`/openings/learn/:id/:name`} component={LearnVariant} />
            </div>
        );
    }
}

function mapStateToProps(state: IRootState): IProps {
    return {
       openings: state.openings.openings,
    };
}

export const connectedComponent = connect(mapStateToProps)(LearnOpening);
