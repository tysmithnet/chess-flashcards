import * as React from "react";
import { IBaseProps, IGameMeta } from "../root";
export interface IProps extends IBaseProps {
    meta: IGameMeta[];
}
export declare class Games extends React.Component<IProps> {
    constructor(props: IProps);
    render(): JSX.Element;
    componentDidMount(): void;
}
export declare const connectedComponent: import("react-redux").ConnectedComponentClass<typeof Games, Pick<IProps, never>>;
