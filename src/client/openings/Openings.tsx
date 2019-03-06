import * as React from "react";
import { connect } from "react-redux";
import { IBaseProps, IOpening, IRootState } from "../root";
import { getOpeningMetaRequestFactory } from "./openings.actions";

export interface IProps extends IBaseProps {
    openings: IOpening[];
}

export class Openings extends React.Component<IProps> {
    constructor(props: IProps) {
        super(props);
    }

    public render() {
        return <h1>hi</h1>;
    }

    public componentDidMount() {
        this.props.dispatch(getOpeningMetaRequestFactory());
    }
}

function mapStateToProps(state: IRootState): IProps {
    return {
        openings: null,
    };
}

export const connectedComponent = connect(mapStateToProps)(Openings);
