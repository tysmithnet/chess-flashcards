import * as React from "react";
import { connect } from "react-redux";
import { IBaseProps, IRootState } from "../root";

export class Openings extends React.Component<IBaseProps> {

    constructor(props: IBaseProps) {
        super(props);
    }

    public render() {
        return (
            <div>openings</div>
        );
    }
}

/**
 * Mapping function for the root state
 *
 * @param {IRootState} state
 * @returns {IBaseProps}
 */
function mapStateToProps(state: IRootState): IBaseProps {
    return {};
}

export const connectedComponent = connect(mapStateToProps)(Openings);
