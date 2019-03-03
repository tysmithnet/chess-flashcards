from app import app, db
from app.models import User, Role, Game, Position


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "User": User,
        "Game": Game,
        "Role": Role,
        "Position": Position
    }
