from app import session_scope
from app.models import User
from functools import wraps
from flask import abort, session


def requires_login():
    def wrapper(f):
        @wraps(f)
        def decorator(*args, **kwargs):
            if "user_id" not in session:
                return abort(401)
            return f(*args, **kwargs)
        return decorator
    return wrapper


def requires_roles(*roles):
    def wrapper(f):
        @wraps(f)
        def decorator(*args, **kwargs):
            if "user_id" not in session:
                return abort(401)
            with session_scope() as sess:
                user_id = session["user_id"]
                user = sess.query(User).filter(
                    User.id == user_id).one_or_none()
                if user is None:
                    return abort(401)

                user_roles = list(map(lambda r: r.name, user.roles))
                missing_roles = [r for r in roles if r not in user_roles]
                if missing_roles:
                    return abort(401)
            return f(*args, **kwargs)
        return decorator
    return wrapper
