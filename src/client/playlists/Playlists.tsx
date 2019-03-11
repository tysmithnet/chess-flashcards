import * as React from "react";
import { connect } from "react-redux";
import { Route, Switch } from "react-router";
import { IBaseProps, IRootState } from "../root";
import { connectedComponent as MasterList } from "./master-list";
import { connectedComponent as Viewer } from "./Viewer";

interface IProps extends IBaseProps {

}

class Playlists extends React.Component<IProps> {
    constructor(props: IProps) {
        super(props);
    }

    public render() {
        return (
            <Switch>
                <Route path={"/playlists/:type/:id"} component={Viewer}/>
                <Route component={MasterList} />
            </Switch>
        );
    }
}

function mapStateToProps(state: IRootState, ownProps: any): IProps {
    return { };
}

export const connectedComponent = connect(mapStateToProps)(Playlists);
