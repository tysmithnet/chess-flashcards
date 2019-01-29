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
        this.handleOpeningChanged = this.handleOpeningChanged.bind(this);
        this.handleVariantChanged = this.handleVariantChanged.bind(this);
    }

    public render() {
        const id = this.props.match.params.id || "Select an Id";
        const options = (this.props.openings || []).map(o => {
            if (id === o.id) {
                return <option key={o.id} value={o.id} selected={true}>{o.id} - {o.name}</option>;
            }
            return <option key={o.id} value={o.id}>{o.id} - {o.name}</option>;
        });
        let variantSelect = null;
        if (this.props.match.params.id) {
            const opening = this.props.openings.filter(o => {
                return o.id === this.props.match.params.id;
            })[0];
            if (opening.variants.length) {
                const variantOptions = opening.variants.map(v => {
                    return <option key={v.name} value={v.name}>{v.name}</option>;
                });
                variantSelect = (
                    <div>
                        <select onChange={this.handleVariantChanged}>
                            {variantOptions}
                        </select>
                    </div>
                );
            }
        }
        return (
            <div>
                <h3>{id}</h3>
                <div>
                    <select onChange={this.handleOpeningChanged}>
                        {options}
                    </select>
                </div>
                {variantSelect}
            </div>
        );
    }

    private handleVariantChanged(event: React.ChangeEvent<HTMLSelectElement>) {
        const id = event.target.value;
        this.props.history.push(`${this.props.match.url}/${id}`);
    }

    private handleOpeningChanged(event: React.ChangeEvent<HTMLSelectElement>) {
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
