import consoleStamp from "console-stamp";
import express from "express";
import proxy from "express-http-proxy";
import http from "http";
import morgan from "morgan";
import path from "path";
import webpack from "webpack";
import webpackHotMiddleware from "webpack-hot-middleware";
import clientWebpackConfig = require("../../config/webpack.config");

consoleStamp(console, "HH:MM:ss.l");

const clientRoot = path.resolve(__dirname, "../client");

const app = express();
app.use(express.static(clientRoot));
app.use(express.json());
app.use(express.urlencoded());
app.use(morgan("short"));
app.use("/proxy", proxy("http://localhost:5000/"));

(() => {
    // setup webpack middleware and hot module replacement
    const webpackConfig = clientWebpackConfig({ mode: "development" });
    const compiler = webpack(webpackConfig);

    app.use(webpackHotMiddleware(compiler, {
        logLevel: "warn",
        publicPath: webpackConfig.output.publicPath,
    }));

    app.use(require("webpack-hot-middleware")(compiler, {
        heartbeat: 10 * 1000,
        log: console.log,
        path: "/__webpack_hmr",
    }));
})();

app.post(/metrics/, (req, res) => {
    console.log(req.param("data"));
});

app.use((req, res, next) => {
    res.sendFile(path.resolve(__dirname, "../client/index.html"));
});

if (require.main === module) {
    const server = http.createServer(app);
    server.listen(process.env.PORT || 8080, () => {
        console.log("Listening on %j", server.address());
    });
}
