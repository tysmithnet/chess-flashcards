# flake8: noqa
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from contextlib import contextmanager

app = Flask(__name__)
app.secret_key = "!%NDAKDadddadXAN_!*(#%!##%!#!DDADA"
app.config.from_object(Config)
db = SQLAlchemy(app)

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

@app.route("/")
@auth.requires_login()
def hello_world():
    return "hello"