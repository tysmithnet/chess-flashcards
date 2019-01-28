import * as React from "react";
import { connect } from "react-redux";
import { bindActionCreators } from "redux";
import {Board} from "../common/board";
import { IState } from "../menu/menu.domain";
import { IRootState } from "../root";
import { getAllOpeningsRequestFactory } from "./openings.actions";
import {IProps} from "./openings.domain";
import "./openings.styles";
export class Openings extends React.Component<IProps, IState> {

    constructor(props: IProps) {
        super(props);
    }

    public render() {
        const options = (this.props.openings || []).map(x => {
            return <option key={x.id} value={x.id}>{x.name}</option>;
        });
        return (
            <div>
                <div className="board">
                    <Board />
                </div>
                <div>
                    <select>
                        {options}
                    </select>
                </div>
            </div>
        );
    }

    public componentDidMount() {
        getAllOpeningsRequestFactory();
    }
}

function mapDispatchToProps(dispatch: any) {
    return bindActionCreators({getAllOpeningsRequestFactory}, dispatch);
}

function mapStateToProps(state: IRootState): IProps {
    return {
        openings: (state.openings.openings) || [],
    };
}

export const connectedComponent = connect(mapStateToProps)(Openings);
