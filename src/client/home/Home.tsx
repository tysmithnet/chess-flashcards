import { Paper, Typography } from "@material-ui/core";
import * as React from "react";
import { connect } from "react-redux";
import { IUser } from "../auth";
import { Board } from "../board/Board";
import { applyMove, IBaseProps, IRootState, STARTING_POSITION } from "../root/root.domain";

interface IProps extends IBaseProps {
    user: IUser;
}

export class Home extends React.Component<IProps> {
    constructor(props: IProps) {
        super(props);
    }

    public render() {
        if (!this.props.user) {
            return (
                <Typography align="center" variant="h3">
                    Please login to see stats
                </Typography>
            );
        }
        return (
            <h1>hi!</h1>
        );
    }
}

function mapStateToProps(state: IRootState): IProps {
    return {
        user: state.auth.user,
    };
}

export const connectedComponent = connect(mapStateToProps)(Home);
