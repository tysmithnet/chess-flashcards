import consoleStamp from "console-stamp";
import express from "express";
import http from "http";
import morgan from "morgan";
import path from "path";
import webpackHotMiddleware from "webpack-hot-middleware";

consoleStamp(console, "HH:MM:ss.l");

const app = express();
app.use(express.static("../dist"));
app.use(express.json());
app.use(express.urlencoded());
app.use(morgan("short"));

(() => {
    // setup webpack middleware and hot module replacement
    const webpack = require("webpack");
    const webpackConfig = require("../config/webpack.config.js")({mode: "development"});
    const compiler = webpack(webpackConfig);

    app.use(require("webpack-dev-middleware")(compiler, {
        logLevel: "warn",
        publicPath: webpackConfig.output.publicPath,
    }));

    app.use(require("webpack-hot-middleware")(compiler, {
        heartbeat: 10 * 1000,
        log: console.log,
        path: "/__webpack_hmr",
    }));
})();

app.post("/api/auth", (req, res) => {
    if(!req.body.id || !req.body.password) {
        res.status(400);
        res.end();
    }
    // IMPENTRABLE SECURITY
    if(req.body.id === "admin" && req.body.password === "password") {
        res.json({
            id: "1",
            name: "Admin",
            permissions: [
                "ADMIN",
            ]});
        res.status(200);
    }
    else {
        res.status(401);
    }
    res.end();
});

app.get(/admin/, (req, res) => {
    res.sendFile(path.resolve(__dirname, "../dist/index.html"));
});

app.post(/metrics/, (req, res) => {
    console.log(req.param("data"));
});

if (require.main === module) {
    const server = http.createServer(app);
    server.listen(process.env.PORT || 8080, () => {
        console.log("Listening on %j", server.address());
    });
}