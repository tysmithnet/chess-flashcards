import * as React from "react";
import { connect } from "react-redux";
import { match, Route, RouteComponentProps } from "react-router";
import { Link } from "react-router-dom";
import {Opening as IOpening} from "../../chess-api";
import { IBaseProps, IRootState } from "../../root";
import {OpeningBoard} from "../opening-board/OpeningBoard";

export interface IProps extends IBaseProps {
    match?: match<any>;
    openings: IOpening[];
}

export class LearnVariant extends React.Component<IProps> {
    constructor(props: IProps) {
        super(props);
    }
    public render() {
        const id = this.props.match.params.id;
        const name = this.props.match.params.name;
        if (!this.props.openings) {
            return <h1>{name}</h1>;
        }
        const opening = this.props.openings.filter(o => o.id === id)[0];
        const variant = opening.variants.filter(v => v.name === name)[0];
        return (
            <div>
                <h1>{name}</h1>
                <OpeningBoard moves={variant.moves} />
            </div>
        )
    }
}

function mapStateToProps(state: IRootState): IProps {
    return {
       openings: state.openings.openings,
    };
}

export const connectedComponent = connect(mapStateToProps)(LearnVariant);
