import { Theme } from "@material-ui/core";
import * as React from "react";
import { IBaseProps, IGame, IOpening, IPlaylist, IPosition, IRoutedProps, PlaylistType } from "../../root";
interface IClasses {
    boardArea: any;
}
interface IProps extends IBaseProps {
    playlistType: PlaylistType;
    playlistId: number;
    playlist: IPlaylist;
    opening: IOpening;
    game: IGame;
    position: IPosition;
    classes?: IClasses;
    theme?: Theme;
}
export declare class Viewer extends React.Component<IProps> {
    constructor(props: IProps);
    render(): JSX.Element;
    componentDidUpdate(prevProps: IProps): void;
}
export declare const connectedComponent: import("react-redux").ConnectedComponentClass<React.ComponentType<Pick<IProps, "playlistType" | "playlistId" | "playlist" | "opening" | "game" | "position" | "dispatch" | "createWorker"> & import("@material-ui/core").StyledComponentProps<"boardArea">>, Pick<Pick<IProps, "playlistType" | "playlistId" | "playlist" | "opening" | "game" | "position" | "dispatch" | "createWorker"> & import("@material-ui/core").StyledComponentProps<"boardArea">, "innerRef"> & IRoutedProps>;
export {};
