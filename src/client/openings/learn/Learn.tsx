import * as React from "react";
import { connect } from "react-redux";
import { match, RouteComponentProps } from "react-router";
import {Opening as IOpening} from "../../chess-api";
import { IBaseProps, IRootState } from "../../root";
export interface IProps extends IBaseProps {
    match?: match<any>;
    history?: any;
    openings: IOpening[];
}

export class Learn extends React.Component<IProps> {

    constructor(props: any) {
        super(props);
        this.handleOpeningSelected = this.handleOpeningSelected.bind(this);
    }

    public render() {
        const id = this.props.match.params.id || "Select an Id";
        const options = (this.props.openings || []).map(o => {
            if (id === o.id) {
                return <option key={o.id} value={o.id} selected={true}>{o.id} - {o.name}</option>;
            }
            return <option key={o.id} value={o.id}>{o.id} - {o.name}</option>;
        });
        return (
            <div>
                <h3>{id}</h3>
                <select onChange={this.handleOpeningSelected}>
                    {options}
                </select>
            </div>
        );
    }

    private handleOpeningSelected(event: React.ChangeEvent<HTMLSelectElement>) {
        const id = event.target.value;
        this.props.history.push(`/openings/learn/${id}`);
    }
}

function mapStateToProps(state: IRootState): IProps {
    return {
       openings: state.openings.openings,
    };
}

export const connectedComponent = connect(mapStateToProps)(Learn);
