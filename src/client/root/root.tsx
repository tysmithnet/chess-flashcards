import { createMuiTheme, MuiThemeProvider } from "@material-ui/core";
import { install } from "@material-ui/styles";
import * as React from "react";
import * as ReactDOM from "react-dom";
import { AppContainer } from "react-hot-loader";
import { Provider } from "react-redux";
import App from "../app/App";
import { rootSaga } from "./root.saga";
import { sagaMiddleware, store } from "./root.store";

install();

const theme = createMuiTheme();

/**
 * Render a component and connect the root store to it
 *
 * @param {JSX.Element} component
 */
function render(component: JSX.Element) {
    ReactDOM.render(
        <MuiThemeProvider theme={theme}>
            <AppContainer>
                <Provider store={store}>{component}</Provider>
            </AppContainer>
        </MuiThemeProvider>,
        document.getElementById("root"),
    );
}

// Start the "background processing"
sagaMiddleware.run(rootSaga);

// Render the application
render(<App />);
