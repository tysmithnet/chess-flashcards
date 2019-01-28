import connexion
import os
from pathlib import Path
from swagger_server import encoder
from flask import abort, request
from flask_cors import CORS

app = connexion.App(__name__, specification_dir='./swagger/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'chess-flashcards'})
application = app.app
CORS(application)
