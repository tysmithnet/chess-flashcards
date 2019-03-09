# flake8: noqa
import os
import sys
from flask import Flask, send_from_directory
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_migrate import Migrate
from contextlib import contextmanager

try:
    UI_DIR = os.environ["UI_DIR"]
except:
    sys.exit("UI_DIR environment variable not set")

app = Flask(__name__)
app.secret_key = "!%NDAKDadddadXAN_!*(#%!##%!#!DDADA"
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = db.session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

from app import models, auth
from app.resources import *

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    parts = [p for p in path.split("/") if p != ""]
    if len(parts) and parts[0] == "api":
        return abort(404)
    possible_path = os.path.join(UI_DIR, path)
    if os.path.exists(possible_path) and not os.path.isdir(possible_path):
        return send_from_directory(UI_DIR, path)
    return send_from_directory(UI_DIR, "index.html")