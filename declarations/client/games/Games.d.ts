import * as React from "react";
import { IBaseProps } from "../root";
import { IFoundGame } from "./games.domain";
export interface IProps extends IBaseProps {
    searchResults: IFoundGame[];
}
export declare class Games extends React.Component<IProps, {}> {
    render(): JSX.Element;
    componentDidMount(): void;
}
export declare const connectedComponent: import("react-redux").ConnectedComponentClass<typeof Games, Pick<IProps, never>>;
