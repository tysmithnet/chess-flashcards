import * as React from "react";
import { connect } from "react-redux";
import { IBaseProps, IGame, IPlaylist, IPosition, IRootState } from "../../root";

interface IProps extends IBaseProps {
    playlist: IPlaylist;
    opening: IPlaylist;
    game: IGame;
    position: IPosition;
}

export class Viewer extends React.Component<IProps> {
    constructor(props: IProps) {
        super(props);
    }
}

function mapStateToProps(state: IRootState): IProps {
    return {
        playlist: null,
        game: null,
        opening: null,
        position: null,
    };
}

export const connectedComponent = connect(mapStateToProps)(Viewer);
