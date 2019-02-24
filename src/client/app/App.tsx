import { AppBar, CssBaseline, Divider, Drawer, IconButton, List, ListItem, ListItemIcon, ListItemText, Toolbar, Typography } from "@material-ui/core";
import { createStyles, Theme, withStyles } from "@material-ui/core/styles";
import ChevronLeftIcon from "@material-ui/icons/ChevronLeft";
import ChevronRightIcon from "@material-ui/icons/ChevronRight";
import InboxIcon from "@material-ui/icons/Inbox";
import MailIcon from "@material-ui/icons/Mail";
import MenuIcon from "@material-ui/icons/Menu";
import classNames from "classnames";
import { ConnectedRouter } from "connected-react-router";
import * as React from "react";
import { hot } from "react-hot-loader";
import { observe } from "react-performance-observer";
import { connect } from "react-redux";
import { Route, Switch } from "react-router";
import { Link } from "react-router-dom";
import { IUser } from "../auth";
import { isTest } from "../globals";
import { getHistory, IBaseProps, IRootState } from "../root";
import { IRoute } from "./app.domain";
import { routes } from "./routes";
// register a metric tracking routine
if (!isTest) {
    observe(measurements => {
        for (const measurement of measurements) {
            if (measurement.entryType !== "measure") {
                continue;
            }
            // console.log(`${measurement.componentName} - ${measurement.duration}`);
            // todo: batch this
            // axios.post("/metrics", {
            //   data: `${measurement.componentName} - ${measurement.duration}`,
            // });
        }
    });
}

const drawerWidth = "240";

export interface IClasses {
    root: any;
    appBar: any;
    appBarShift: any;
    menuButton: any;
    hide: any;
    drawer: any;
    drawerPaper: any;
    drawerHeader: any;
    content: any;
    contentShift: any;
}

const styles = (theme: Theme) => createStyles({
    root: {
        display: "flex",
    },
    appBar: {
        transition: theme.transitions.create(["margin", "width"], {
            easing: theme.transitions.easing.sharp,
            duration: theme.transitions.duration.leavingScreen,
        }),
    },
    appBarShift: {
        width: `calc(100% - ${drawerWidth}px)`,
        marginLeft: drawerWidth,
        transition: theme.transitions.create(["margin", "width"], {
            easing: theme.transitions.easing.easeOut,
            duration: theme.transitions.duration.enteringScreen,
        }),
    },
    menuButton: {
        marginLeft: 12,
        marginRight: 20,
    },
    hide: {
        display: "none",
    },
    drawer: {
        width: drawerWidth,
        flexShrink: 0,
    },
    drawerPaper: {
        width: drawerWidth,
    },
    drawerHeader: {
        display: "flex",
        alignItems: "center",
        padding: "0 8px",
        ...theme.mixins.toolbar,
        justifyContent: "flex-end",
    },
    content: {
        flexGrow: 1,
        padding: theme.spacing.unit * 3,
        transition: theme.transitions.create("margin", {
            easing: theme.transitions.easing.sharp,
            duration: theme.transitions.duration.leavingScreen,
        }),
        marginLeft: -drawerWidth,
    },
    contentShift: {
        transition: theme.transitions.create("margin", {
            easing: theme.transitions.easing.easeOut,
            duration: theme.transitions.duration.enteringScreen,
        }),
        marginLeft: 0,
    },
});

export interface IState {
    open: boolean;
}
export interface IProps extends IBaseProps {
    /**
     * The currently logged in user
     *
     * @type {IUser}
     * @memberof IProps
     */
    user?: IUser;

    /**
     * Currently active routes
     *
     * @type {IRoute[]}
     * @memberof IProps
     */
    routes?: IRoute[];
    classes?: IClasses;
    theme?: Theme;
}

function fourOhFour() {
    return <h1 className="not-found">Not found!</h1>;
}
/**
 * The root of the application. It"s primary responsibility is providing
 * an environment in which more focused components can provide value.
 */
export class App extends React.Component<IProps, IState> {

    private classes: IClasses;
    private theme: Theme;

    constructor(props: IProps) {
        super(props);
        this.state = {
            open: false,
        };
        this.classes = props.classes;
        this.theme = props.theme;
        this.handleClose = this.handleClose.bind(this);
        this.handleOpen = this.handleOpen.bind(this);
    }

    public render() {
        const open = this.state.open;
        const toAdd = routes
            .map(r => {
                return {
                    link: (
                        <Link key={r.path} to={r.path}>
                            <ListItem button={true} key={r.path}>
                                <ListItemIcon><InboxIcon /></ListItemIcon>
                                <ListItemText primary={r.display}>{r.display}</ListItemText>
                            </ListItem>
                        </Link>
                    ),
                    route: (
                        <Route
                            key={r.path}
                            path={r.path}
                            component={r.component}
                            exact={r.exact}
                        />
                    ),
                };
            });
        return (
            <ConnectedRouter history={getHistory()}>
                <div className={this.classes.root}>
                    <CssBaseline />
                    <AppBar
                        position="fixed"
                        className={classNames(this.classes.appBar, {
                            [this.classes.appBarShift]: open,
                        })}
                    >
                        <Toolbar disableGutters={!open}>
                            <IconButton
                                color="inherit"
                                aria-label="Open drawer"
                                onClick={this.handleOpen}
                                className={classNames(this.classes.menuButton, open && this.classes.hide)}
                            >
                                <MenuIcon />
                            </IconButton>
                            <Typography variant="h6" color="inherit" noWrap={true}>
                                Persistent drawer
                                </Typography>
                        </Toolbar>
                    </AppBar>
                    <Drawer
                        className={this.classes.drawer}
                        variant="persistent"
                        anchor="left"
                        open={open}
                        classes={{
                            paper: this.classes.drawerPaper,
                        }}
                    >
                        <div className={this.classes.drawerHeader}>
                            <IconButton onClick={this.handleClose}>
                                {this.theme.direction === "ltr" ? <ChevronLeftIcon /> : <ChevronRightIcon />}
                            </IconButton>
                        </div>
                        <Divider />
                        <List>
                            {toAdd.map(x => x.link)}
                        </List>
                    </Drawer>
                    <main
                        className={classNames(this.classes.content, {
                            [this.classes.contentShift]: open,
                        })}
                    >
                        <div className={this.classes.drawerHeader} />
                        <Switch>
                            {toAdd.map(x => x.route)}
                            <Route render={fourOhFour} />
                        </Switch>
                    </main>
                </div>
            </ConnectedRouter >
        );
    }

    private handleOpen() {
        this.setState({
            open: true,
        });
    }

    private handleClose() {
        this.setState({
            open: false,
        });
    }
}

/**
 * Hook into changes in the state
 * @param state Current state of the application
 */
function mapStateToProps(state: IRootState): IProps {
    return {
        routes: state.app.routes,
    };
}

// Setup hot module reloading for the app
// This enables changes to files under development to be instantly reflected
// in the browser
const hotModule = hot(module)(App);
const styledComponent = withStyles(styles, { withTheme: true })(hotModule);
const connectedComponent = connect(mapStateToProps)(styledComponent);

export default connectedComponent;
