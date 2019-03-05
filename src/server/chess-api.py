from app import app, db
import app.models as m


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "User": m.User,
        "Game": m.Game,
        "Role": m.Role,
        "Position": m.Position,
        "GamePlaylist": m.GamePlaylist,
        "OpeningPlaylist": m.OpeningPlaylist,
    }
