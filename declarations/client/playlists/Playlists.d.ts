import * as React from "react";
import { IBaseProps, IPlaylist } from "../root";
export interface IProps extends IBaseProps {
    gamePlaylistMeta: IPlaylist[];
    openingPlaylistMeta: IPlaylist[];
}
export declare class Playlists extends React.Component<IProps, {}> {
    constructor(props: IProps);
    render(): JSX.Element;
}
export declare const connectedComponent: import("react-redux").ConnectedComponentClass<typeof Playlists, Pick<IProps, never>>;
