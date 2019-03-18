import { Theme } from "@material-ui/core";
import * as React from "react";
import { IBaseProps, IGame, IOpening, IPlaylist, IPosition, IRoutedProps, PlaylistType } from "../../root";
interface IClasses {
    root: any;
    horizontalCenter: any;
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
    isLearnMovesMode: boolean;
    learnMovePositionIndex: number;
}
interface IState {
    isBlackPerspective: boolean;
}
export declare class Viewer extends React.Component<IProps, IState> {
    constructor(props: IProps);
    render(): JSX.Element;
    componentDidMount(): void;
    componentDidUpdate(prevProps: IProps, prevState: IState): void;
    private renderLearnMovesMode;
    private renderMakeMovesMode;
    private getButtons;
    private handleSkip;
    private handleLearnGoForward;
    private handleLearnGoBack;
    private handleFlipBoard;
    private handleChangeToLearnMovesMode;
    private handleChangeToMakeMovesMode;
    private ensureDataIsLoaded;
    private handleMove;
}
export declare const connectedComponent: import("react-redux").ConnectedComponentClass<React.ComponentType<Pick<IProps, "playlistType" | "playlistId" | "playlist" | "opening" | "game" | "position" | "isLearnMovesMode" | "learnMovePositionIndex" | "dispatch" | "createWorker"> & import("@material-ui/core").StyledComponentProps<"root" | "horizontalCenter" | "boardArea">>, Pick<Pick<IProps, "playlistType" | "playlistId" | "playlist" | "opening" | "game" | "position" | "isLearnMovesMode" | "learnMovePositionIndex" | "dispatch" | "createWorker"> & import("@material-ui/core").StyledComponentProps<"root" | "horizontalCenter" | "boardArea">, "innerRef"> & IRoutedProps>;
export {};
