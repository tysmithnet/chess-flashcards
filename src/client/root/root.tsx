import { createMuiTheme, CssBaseline, MuiThemeProvider } from "@material-ui/core";
import { install, ThemeProvider } from "@material-ui/styles";
import * as React from "react";
import * as ReactDOM from "react-dom";
import { AppContainer } from "react-hot-loader";
import { Provider } from "react-redux";
import App from "../app/App";
import { rootSaga } from "./root.saga";
import { configureStore, sagaMiddleware } from "./root.store";

// install();

const theme = createMuiTheme({ typography: { useNextVariants: true } });
const store = configureStore({
    app: null,
    auth: null,
    playlists: null,
    openings: null,
});

/**
 * Render a component and connect the root store to it
 *
 * @param {JSX.Element} component
 */
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

// Start the "background processing"
sagaMiddleware.run(rootSaga);

// Render the application
render(<App />);
