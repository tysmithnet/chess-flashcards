import * as React from "react";
import { IBaseProps } from "../root";
interface IProps extends IBaseProps {
}
declare class Playlists extends React.Component<IProps> {
    constructor(props: IProps);
    render(): JSX.Element;
}
export declare const connectedComponent: import("react-redux").ConnectedComponentClass<typeof Playlists, Pick<IProps, never>>;
export {};
