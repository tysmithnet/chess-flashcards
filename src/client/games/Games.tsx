import * as React from "react";
import { connect } from "react-redux";
import { IBaseProps, IRootState } from "../root";
import { gameSearchRequestFactory } from "./games.action";
import { IFoundGame } from "./games.domain";

export interface IProps extends IBaseProps {
    searchResults: IFoundGame[];
}

export class Games extends React.Component<IProps, {}> {
    public render() {
        return <h1>hi!</h1>;
    }

    public componentDidMount() {
        this.props.dispatch(gameSearchRequestFactory(""));
    }
}

function mapStateToProps(state: IRootState): IProps {
    return {
        searchResults: state.games.searchResults,
    };
}

export const connectedComponent = connect(mapStateToProps)(Games);
