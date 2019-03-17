import * as React from "react";
import { IBaseProps, IGame, IOpening } from "../../root";
interface IProps extends IBaseProps {
    opening: IOpening;
    game: IGame;
    attempts: number;
    successes: number;
}
export declare class Stats extends React.Component<IProps> {
    constructor(props: IProps);
    render(): {};
    renderGame(): React.ReactNode;
    renderOpening(): React.ReactNode;
}
export declare const connectedComponent: import("react-redux").ConnectedComponentClass<typeof Stats, Pick<IProps, never>>;
export {};
