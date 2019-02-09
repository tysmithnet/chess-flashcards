import * as _ from "lodash";
import * as React from "react";
import { connect } from "react-redux";
import { Board } from "../board/Board";
import { Opening } from "../chess-api";
import {IBaseProps, IRootState} from "../root";
import { loadOpeningsRequestFactory } from "./openings.action";

export interface IProps extends IBaseProps {
    openings: Opening[];
    selectedOpenings: Opening[];
}

export interface IState {
    searchTerm: string;
}

export class Openings extends React.Component<IProps, IState> {
    constructor(props: IProps) {
        super(props);
        this.state = {
            searchTerm: null,
        };
    }

    public render() {
        if (!this.props.openings) {
            return <h3>Loading...</h3>;
        }
        const rows = this.props.openings.map((o, oi) => {
            const eco = o.id;
            return o.variants.map((v, vi) => {
                return (
                    <tr key={`${eco} - ${v.name} - ${vi}`}>
                        <td><input type="checkbox" /></td>
                        <td>{eco}</td>
                        <td>{v.name}</td>
                    </tr>
                );
            });
        });
        const flattened = _.flatten(rows);
        return (
            <div className="openings">
                <h1>Openings Quiz</h1>
                <div className="board-area">
                    board
                </div>
                <div className="selection-area">
                    <input value={this.state.searchTerm} />
                    <table>
                        <thead>
                            <tr>
                                <th />
                                <th>ECO</th>
                                <th>Name</th>
                            </tr>
                        </thead>
                        <tbody>
                            {flattened}
                        </tbody>
                    </table>
                </div>
            </div>
        );
    }

    public componentDidMount() {
        this.props.dispatch(loadOpeningsRequestFactory());
    }
}

function mapStateToProps(state: IRootState): IProps {
    return {
        openings: state.openings.openings,
        selectedOpenings: state.openings.selectedOpenings,
    };
}

export const connectedComponent = connect(mapStateToProps)(Openings);
