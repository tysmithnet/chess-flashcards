from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

user_roles = db.Table(
    "user_role",
    db.Column("user_id", db.Integer, db.ForeignKey(
        "user.id"), primary_key=True),
    db.Column("role_id", db.Integer, db.ForeignKey(
        "role.id"), primary_key=True),
)

open_moves = db.Table(
    "opening_move",
    db.Column("opening_id", db.Integer, db.ForeignKey(
        "opening.id"), primary_key=True),
    db.Column("move_id", db.Integer, db.ForeignKey(
        "move.id"), primary_key=True),
    db.Column("order", db.Integer)
)

game_moves = db.Table(
    "game_move",
    db.Column("game_id", db.Integer, db.ForeignKey(
        "game.id"), primary_key=True),
    db.Column("move_id", db.Integer, db.ForeignKey(
        "move.id"), primary_key=True),
    db.Column("order", db.Integer)
)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    roles = db.relationship(
        "Role", secondary=user_roles, back_populates="users")

    def __repr__(self):
        return "<User {}>".format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    users = db.relationship(
        "User", secondary=user_roles, back_populates="roles")


class Game(db.Model):
    __tablename__ = "game"
    id = db.Column(db.Integer, primary_key=True)
    moves = db.relationship(
        "Move", secondary=user_roles, back_populates="games",
        order_by=game_moves.order)


class Move(db.Model):
    __tablename__ = "move"
    id = db.Column(db.Integer, primary_key=True)
    start_pos_id = db.Column(db.Integer, db.ForeignKey(
        "position.id", ondelete="CASCADE"))
    start_pos = db.relationship("Position")
    end_pos_id = db.Column(db.Integer, db.ForeignKey(
        "position.id", ondelete="CASCADE"))
    end_pos = db.relationship("Position")
    src = db.Column(db.Integer, nullable=False)
    dst = db.Column(db.Integer, nullable=False)
    games = db.relationship(
        "Game", secondary=game_moves, back_populates="moves", order_by=Game.id)
    openings = db.relationship(
        "Opening", secondary=open_moves, back_populates="moves",
        order_by=open_moves.order)


class Position(db.Model):
    __tablename__ = "position"
    id = db.Column(db.Integer, primary_key=True)
    pieces = db.Column(db.String(64), nullable=False)
    turn = db.Column(db.Boolean, nullable=False)
    white_can_castle_queenside = db.Column(db.Boolean, nullable=False)
    white_can_castle_kingside = db.Column(db.Boolean, nullable=False)
    black_can_castle_queenside = db.Column(db.Boolean, nullable=False)
    black_can_castle_kingside = db.Column(db.Boolean, nullable=False)
    en_passant_square = db.Column(db.Integer)
    halfmove_clock = db.Column(db.Integer, nullable=False)
    fullmove_number = db.Column(db.Integer, nullable=False)
    is_check = db.Column(db.Boolean, default=False)
    is_checkmate = db.Column(db.Boolean, default=False)
    is_stalemate = db.Column(db.Boolean, default=False)
    is_check = db.Column(db.Boolean, default=False)


class Opening(db.Model):
    __tablename__ = "opening"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(3), primary_key=True)
    moves = db.relationship("Move", secondary=open_moves,
                            back_populates="openings",
                            order_by=open_moves.order)
