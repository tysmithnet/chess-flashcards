import * as React from "react";
import { Link } from "react-router-dom";
import { IBaseProps } from "../root";
import "./menu.styles";
export interface IProps extends IBaseProps {
    links: Link[];
}
export declare class Menu extends React.Component<IProps> {
    constructor(props: IProps);
    render(): JSX.Element;
}
