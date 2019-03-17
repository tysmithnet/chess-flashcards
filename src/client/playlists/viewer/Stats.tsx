import { Card, CardContent, Typography } from "@material-ui/core";
import * as React from "react";
import { connect } from "react-redux";
import { IBaseProps, IGame, IOpening, IRootState } from "../../root";

interface IProps extends IBaseProps {
    opening: IOpening;
    game: IGame;
    attempts: number;
    successes: number;
}

export class Stats extends React.Component<IProps> {
    constructor(props: IProps) {
        super(props);
    }

    public render() {
        if (this.props.opening) {
            return this.renderOpening();
        }
        if (this.props.game) {
            return this.renderGame();
        }
        return null;
    }

    public renderGame(): React.ReactNode {
        const white = this.props.game.headers.get("White") || "??";
        const black = this.props.game.headers.get("Black") || "??";
        const name = `${white} vs. ${black}`;
        return (
            <Card>
                <CardContent>
                <Typography component="h5" variant="h5">
                    {name}
                </Typography>
                </CardContent>
            </Card>
        );
    }

    public renderOpening(): React.ReactNode {
        const eco = this.props.opening.eco;
        const name = this.props.opening.name;
        const header = `${eco} - ${name}`;
        const statsLine = `${this.props.successes}/${this.props.attempts}`;
        return (
            <Card>
                <CardContent>
                    <Typography component="h5" variant="h5">
                        {header}
                    </Typography>
                    <Typography variant="subtitle1" color="textSecondary">
                        {statsLine}
                    </Typography>
                </CardContent>
            </Card>
        );
    }
}

function mapStateToProps(state: IRootState): IProps {
    return {
        opening: state.playlists.viewer.opening,
        game: state.playlists.viewer.game,
        attempts: state.playlists.viewer.attempts || 0,
        successes: state.playlists.viewer.successes || 0,
    };
}

export const connectedComponent = connect(mapStateToProps)(Stats);
