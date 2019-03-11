import axios from "axios";
import * as React from "react";
import { IBaseProps, IPlaylist } from "../../root";

interface IProps extends IBaseProps {
    playlist: IPlaylist;
}

interface IState {

}

export class Viewer extends React.Component<IProps, IState> {
    public render() {
        return <h1>hi</h1>;
    }
}
