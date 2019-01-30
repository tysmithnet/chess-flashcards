import * as React from "react";
import { connect } from "react-redux";
import { match, Route, RouteComponentProps } from "react-router";
import { Link } from "react-router-dom";
import {OpeningMeta as IOpeningMeta} from "../../chess-api";
import { IBaseProps, IRootState } from "../../root";
import "./learn.styles";
import {connectedComponent as LearnVariant} from "./LearnVariant";

export interface IProps extends IBaseProps {
    match?: match<any>;
    openings: IOpeningMeta[];
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
        const variants = opening.variantNames;
        const items = variants.map(v => {
            return <li key={v}><Link  to={`/openings/learn/${id}/${v}`}>{v}</Link></li>;
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
       openings: state.openings.openingMetaData,
    };
}

export const connectedComponent = connect(mapStateToProps)(LearnOpening);
