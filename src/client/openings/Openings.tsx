import * as _ from "lodash";
import * as React from "react";
import { connect } from "react-redux";
import { Board, EMPTY_BOARD, STARTING_POSITION } from "../board/Board";
import { Opening, OpeningVariant } from "../chess-api";
import {IBaseProps, IRootState} from "../root";
import { loadOpeningsRequestFactory } from "./openings.action";
import "./openings.styles";

export interface IProps extends IBaseProps {
    openings: Opening[];
}

export interface IState {
    searchText: string;
    selectedOpenings: ISelectedOpening[];
    showDialog: boolean;
    current: ISelectedOpening;
}

export interface ISelectedOpening {
    eco: string;
    variant: OpeningVariant;
}

export class Openings extends React.Component<IProps, IState> {
    constructor(props: IProps) {
        super(props);
        this.state = {
            searchText: "",
            selectedOpenings: [],
            showDialog: false,
            current: null,
        };
        this.handleSearchTextChange = this.handleSearchTextChange.bind(this);
        this.handleVariantSelected = this.handleVariantSelected.bind(this);
        this.showDialog = this.showDialog.bind(this);
    }

    public render() {
        if (!this.props.openings) {
            return <h3>Loading...</h3>;
        }
        const rows = this.props.openings.map((o, oi) => {
            const eco = o.id;
            const filtered = o.variants.filter(v => {
                return o.id.toLowerCase().indexOf(this.state.searchText.toLowerCase()) > -1
                    || v.name.toLowerCase().indexOf(this.state.searchText.toLowerCase()) > -1;
            });
            return filtered.map((v, vi) => {
                return (
                    <tr key={`${eco} - ${v.name} - ${vi}`}>
                        <td><input type="checkbox" data-eco={eco} data-name={v.name} onChange={this.handleVariantSelected}/></td>
                        <td>{eco}</td>
                        <td>{v.name}</td>
                    </tr>
                );
            });
        });
        const flattened = _.flatten(rows);
        let dialog = null;
        if (this.state.showDialog) {
            dialog = (
                <div className="selection-dialog">
                    <input value={this.state.searchText} onChange={this.handleSearchTextChange}/>
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
            );
        }
        let currentTitle = "Select openings";
        if (this.state.current) {
            currentTitle = `${this.state.current.eco} - ${this.state.current.variant.name}`;
        }
        return (
            <div className="openings">
                <h1 className="title" onClick={this.showDialog}>{currentTitle}</h1>
                <div className="board-area">
                    <Board position={EMPTY_BOARD} legalMoves={[]} />
                </div>
                {dialog}
            </div>
        );
    }

    public componentDidMount() {
        this.props.dispatch(loadOpeningsRequestFactory());
    }

    public showDialog() {
        this.setState({
            ...this.state,
            showDialog: true,
        });
    }

    private handleVariantSelected(event: React.ChangeEvent<HTMLInputElement>) {
        const eco = event.currentTarget.getAttribute("data-eco");
        const name = event.currentTarget.getAttribute("data-name");
        const opening = this.props.openings.find(o => o.id === eco);
        const variant = opening.variants.find(v => v.name === name);
        const isChecked = event.currentTarget.checked;
        if (!isChecked) {
            const newList = _.remove(this.state.selectedOpenings, s => s.variant === variant);
            this.setState({
                ...this.state,
                selectedOpenings: newList,
            });
        } else {
            const newList = [...this.state.selectedOpenings];
            newList.push({
                eco,
                variant,
            });
            this.setState({
                ...this.state,
                selectedOpenings: newList,
            });
        }
    }

    private handleSearchTextChange(event: React.ChangeEvent<HTMLInputElement>) {
        const text = event.currentTarget.value;
        this.setState({
            ...this.state,
            searchText: text,
        });
    }
}

function mapStateToProps(state: IRootState): IProps {
    return {
        openings: state.openings.openings,
    };
}

export const connectedComponent = connect(mapStateToProps)(Openings);
