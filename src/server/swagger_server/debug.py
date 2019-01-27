import connexion
import os
from pathlib import Path
from swagger_server import encoder
from flask import abort, request

def error_handler(error):
    d = os.path.dirname(__file__)
    path = Path(d + "/../../../dist/client/")
    dist = path.resolve()
    if request.path == "/":
        index = Path(str(dist) + "/index.html").resolve()
        with open(index, "r") as f:
            lines = "\n".join(f.readlines())
            return lines
    possible = Path(str(dist) + request.path).resolve()
    if possible.is_file():
        with open(str(possible), "r") as f:
            lines = "\n".join(f.readlines())
            return lines
    abort(404)

app = connexion.App(__name__, specification_dir='./swagger/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'chess-flashcards'})
app.add_error_handler(404, error_handler)
application = app.app
