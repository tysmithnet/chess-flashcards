import * as _ from "lodash";
import * as React from "react";
import { connect } from "react-redux";
import { Board, EMPTY_BOARD, STARTING_POSITION } from "../board/Board";
import { Opening, OpeningVariant } from "../chess-api";
import { IBaseProps, IRootState } from "../root";
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
        this.showDialog = this.showDialog.bind(this);
        this.hideDialog = this.hideDialog.bind(this);
    }

    public render() {
        if (!this.props.openings) {
            return <h3>Loading...</h3>;
        }
        let dialog = null;
        if (this.state.showDialog) {
            dialog = this.createDialog();
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
        document.addEventListener("keydown", this.hideDialog);
    }

    public componentWillUnmount() {
        document.removeEventListener("keydown", this.hideDialog);
    }

    private createDialog() {
        const rows = this.props.openings.map((o, oi) => {
            const eco = o.id;
            const filtered = o.variants.filter(v => {
                return o.id.toLowerCase().indexOf(this.state.searchText.toLowerCase()) > -1
                    || v.name.toLowerCase().indexOf(this.state.searchText.toLowerCase()) > -1;
            });
            return filtered.map((v, vi) => {
                return (
                    <tr key={`${eco} - ${v.name} - ${vi}`}>
                        <td><input type="checkbox" data-eco={eco} data-name={v.name} /></td>
                        <td>{eco}</td>
                        <td>{v.name}</td>
                    </tr>
                );
            });
        });
        const flattened = _.flatten(rows);
        return (
            <div className="selection-dialog">
                <input className="search-bar" value={this.state.searchText} onChange={this.handleSearchTextChange} />
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

    private showDialog() {
        this.setState({
            ...this.state,
            showDialog: true,
        });
    }

    private hideDialog(event: KeyboardEvent) {
        if (event.keyCode !== 27) {
            return;
        }

        const selectedInputs = (event.currentTarget as any).querySelectorAll(".openings .selection-dialog table input:checked");
        const newSelected: ISelectedOpening[] = [];
        for (const input of selectedInputs as HTMLInputElement[]) {
            const eco = input.getAttribute("data-eco");
            const name = input.getAttribute("data-name");
            const opening = this.props.openings.find(o => o.id === eco);
            const variant = opening.variants.find(v => v.name === name);
            newSelected.push({
                eco,
                variant,
            });
        }

        let current = null;
        if (newSelected.length) {
            const ran = Math.floor(Math.random() * newSelected.length);
            current = newSelected[ran];
        }

        this.setState({
            ...this.state,
            showDialog: false,
            selectedOpenings: newSelected,
            current,
        });
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
