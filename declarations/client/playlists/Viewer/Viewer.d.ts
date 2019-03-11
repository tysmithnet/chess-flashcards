import * as React from "react";
import { IBaseProps, IGame, IOpening, IPlaylist, IPosition, IRoutedProps, PlaylistType } from "../../root";
interface IProps extends IBaseProps {
    playlistType: PlaylistType;
    playlistId: number;
    playlist: IPlaylist;
    opening: IOpening;
    game: IGame;
    position: IPosition;
}
export declare class Viewer extends React.Component<IProps> {
    constructor(props: IProps);
    render(): JSX.Element;
    componentDidMount(): void;
}
export declare const connectedComponent: import("react-redux").ConnectedComponentClass<typeof Viewer, Pick<IProps, never> & IRoutedProps>;
export {};
