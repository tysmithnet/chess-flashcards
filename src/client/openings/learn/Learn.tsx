import * as React from "react";
import { connect } from "react-redux";
import { match } from "react-router";
import {Opening as IOpening} from "../../chess-api";
import { IBaseProps, IRootState } from "../../root";
export interface IProps extends IBaseProps {
    match?: match<any>;
    openings: IOpening[];
}

export class Learn extends React.Component<IProps> {

    constructor(props: any) {
        super(props);
    }

    public render() {
        const options = (this.props.openings || []).map(o => {
            return <option key={o.id}>{o.id} - {o.name}</option>;
        });
        const id = this.props.match.params.id || "Select an Id";
        return (
            <div>
                <h3>{id}</h3>
                <select>
                    {options}
                </select>
            </div>
        );
    }
}

function mapStateToProps(state: IRootState): IProps {
    return {
       openings: state.openings.openings,
    };
}

export const connectedComponent = connect(mapStateToProps)(Learn);
