import * as React from "react";
import { connect } from "react-redux";
import { match, Route, RouteComponentProps } from "react-router";
import { Link } from "react-router-dom";
import {OpeningMeta as IOpeningMeta} from "../../chess-api";
import { IBaseProps, IRootState } from "../../root";
import {OpeningBoard} from "../opening-board/OpeningBoard";

export interface IProps extends IBaseProps {
    match?: match<any>;
    openings: IOpeningMeta[];
}

export class LearnVariant extends React.Component<IProps> {
    constructor(props: IProps) {
        super(props);
    }
    public render() {
        return <h1>hi</h1>;
    }
}

function mapStateToProps(state: IRootState): IProps {
    return {
       openings: state.openings.openingMetaData,
    };
}

export const connectedComponent = connect(mapStateToProps)(LearnVariant);
