# flake8: noqa
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from contextlib import contextmanager

app = Flask(__name__)
app.secret_key = "!%NDAKDadddadXAN_!*(#%!##%!#!DDADA"
app.config.from_object(Config)
db = SQLAlchemy(app)
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
from resources.game import GameResource
