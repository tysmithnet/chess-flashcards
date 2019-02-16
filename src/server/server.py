import os
from flask import Flask, send_from_directory

from_main = False

app = Flask(__name__)

print("global")

@app.route("/api")
def api():
    return "/API!!"

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    global from_main
    base = "../../dist/client"
    if path == "" or path == "/":
        path = "index.html"
    if from_main:
        base = "client"
    base = os.path.abspath(base)
    if os.path.exists(os.path.join(base, path)):
        return send_from_directory(base, path)
    return "404"

if __name__ == "__main__":
    from_main = True
    app.run(port=8080)