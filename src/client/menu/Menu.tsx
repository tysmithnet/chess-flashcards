import * as React from "react";
import { Link } from "react-router-dom";
import { IBaseProps } from "../root";
import "./menu.styles";
/**
 * Props for Menu
 */
export interface IProps extends IBaseProps {
    /**
     * Links to display
     */
    links: Link[];
}

export class Menu extends React.Component<IProps> {
    constructor(props: IProps) {
        super(props);
    }

    public render() {
        const items = this.props.links.map(l => {
            return (
                <div key={l.props.href} className="menu-item">
                    {l}
                </div>
            );
        });
        return (
            <div className="menu">
                {items}
            </div>
        );
    }
}
