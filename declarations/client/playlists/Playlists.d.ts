import * as React from "react";
import { IBaseProps } from "../root";
import { IPlaylistMeta } from "./playlists.domain";
export interface IProps extends IBaseProps {
    gamePlaylistMeta: IPlaylistMeta[];
    openingPlaylistMeta: IPlaylistMeta[];
}
export declare class Playlists extends React.Component<IProps, {}> {
    constructor(props: IProps);
    render(): JSX.Element;
}
export declare const connectedComponent: import("react-redux").ConnectedComponentClass<typeof Playlists, Pick<IProps, never>>;
