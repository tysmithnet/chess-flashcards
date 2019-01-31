import * as React from "react";
import { connect } from "react-redux";
import { match, Route, RouteComponentProps } from "react-router";
import { Link } from "react-router-dom";
import {Opening as IOpening, OpeningMeta as IOpeningMeta} from "../../chess-api";
import { IBaseProps, IRootState } from "../../root";
import {OpeningBoard} from "../opening-board/OpeningBoard";
import { getOpeningDetailRequestFactory } from "../openings.actions";

export interface IProps extends IBaseProps {
    match?: match<any>;
    openingMetaData: IOpeningMeta[];
    openings: IOpening[];
}

export class LearnVariant extends React.Component<IProps> {
    constructor(props: IProps) {
        super(props);
    }

    public render() {
        if (this.props.openings == null) {
            return <h1>loading..</h1>;
        }
        const opening = this.props.openings.find(o => o.id === this.props.match.params.id);
        if (opening == null) {
            this.props.dispatch(getOpeningDetailRequestFactory(this.props.match.params.id));
            return <h1>loading..</h1>;
        }
        return <h1>OK TO GO AHEAD</h1>;
    }
}

function mapStateToProps(state: IRootState): IProps {
    return {
        openings: state.openings.openings,
        openingMetaData: state.openings.openingMetaData,
    };
}

export const connectedComponent = connect(mapStateToProps)(LearnVariant);
