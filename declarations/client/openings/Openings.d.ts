import * as React from "react";
import { IBaseProps, IMove, IOpening } from "../root";
import "./openings.styles";
export interface IProps extends IBaseProps {
    openings: IOpening[];
}
export interface IState {
    openings: Map<string, IOpening>;
    searchText: string;
    selectedOpenings: Set<string>;
    showDialog: boolean;
    current: IOpening;
    moveNum: number;
    position: string[];
    legalMoves: IMove[];
    backStack: string[];
    isBlackPerspective: boolean;
    isBackOfCard: boolean;
}
export declare class Openings extends React.Component<IProps, IState> {
    constructor(props: IProps);
    componentDidUpdate(prevProps: IProps): void;
    render(): JSX.Element;
    componentDidMount(): void;
    componentWillUnmount(): void;
    private createRecognizeQuiz;
    private handleMouseWheelOverBoard;
    private createDemonstrateQuiz;
    private createPresets;
    private handlePresetSelected;
    private handleKeyUp;
    private flipMode;
    private flipBoard;
    private giveHint;
    private goNextOpening;
    private redoCurrentOpening;
    private goBackOpening;
    private handleMove;
    private createDialog;
    private showDialog;
    private handleVariantSelected;
    private hideDialog;
    private handleSearchTextChange;
}
export declare const connectedComponent: React.ComponentClass<Pick<IProps, never>, any> & {
    WrappedComponent: React.ComponentType<IProps>;
};
