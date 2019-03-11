import * as React from "react";
import { IBaseProps, IPlaylist, PlaylistType } from "../root";
interface IProps extends IBaseProps {
    playlist?: IPlaylist;
    type?: PlaylistType;
    id?: number;
}
interface IState {
}
export declare class Viewer extends React.Component<IProps, IState> {
    render(): JSX.Element;
}
export declare const connectedComponent: import("react-redux").ConnectedComponentClass<typeof Viewer, Pick<IProps, never> & IProps>;
export {};
