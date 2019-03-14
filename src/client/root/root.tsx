import { createMuiTheme, CssBaseline, MuiThemeProvider } from "@material-ui/core";
import { ThemeProvider } from "@material-ui/styles";
import * as React from "react";
import * as ReactDOM from "react-dom";
import { AppContainer } from "react-hot-loader";
import { Provider } from "react-redux";
import App from "../app/App";
import { rootSaga } from "./root.saga";
import { configureStore, sagaMiddleware } from "./root.store";

const theme = createMuiTheme({ typography: { useNextVariants: true } });
const store = configureStore({
    app: null,
    auth: null,
    games: null,
    playlists: {
        masterList: null,
        viewer: null,
    },
    openings: null,
    router: null,
});

function render(component: JSX.Element) {
    ReactDOM.render(
        <CssBaseline>
            <AppContainer>
                <ThemeProvider theme={theme}>
                    <Provider store={store}>
                        {component}
                    </Provider>
                </ThemeProvider>
            </AppContainer>
        </CssBaseline>,
        document.getElementById("root"),
    );
}

sagaMiddleware.run(rootSaga);
render(<App />);
