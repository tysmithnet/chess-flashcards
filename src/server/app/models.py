from app import db
from werkzeug.security import generate_password_hash, check_password_hash
import chess


class UserRole(db.Model):
    __tablename__ = "user_role"
    user_id = db.Column(db.Integer, db.ForeignKey(
        "user.id", ondelete="CASCADE"), primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey(
        "role.id", ondelete="CASCADE"), primary_key=True)
    user = db.relationship("User", back_populates="roles")
    role = db.relationship("Role", back_populates="users")

    def __repr__(self):
        return "UserRole(user_id={}, role_id={})".format(self.user_id,
                                                         self.role_id)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(
        db.String(64), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    roles = db.relationship("UserRole", back_populates="user")

    def __repr__(self):
        return "User(id={}, username=\"{}\")".format(self.id, self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    users = db.relationship("UserRole", back_populates="role")

    def __repr__(self):
        return "Role(id={}, name=\"{}\")".format(self.id, self.name)


class Position(db.Model):
    __tablename__ = "position"
    id = db.Column(db.Integer, primary_key=True)
    pieces = db.Column(db.String(128), nullable=False)
    turn = db.Column(db.Boolean, nullable=False)
    white_can_castle_queenside = db.Column(db.Boolean, nullable=False)
    white_can_castle_kingside = db.Column(db.Boolean, nullable=False)
    black_can_castle_queenside = db.Column(db.Boolean, nullable=False)
    black_can_castle_kingside = db.Column(db.Boolean, nullable=False)
    en_passant_square = db.Column(db.Integer)
    halfmove_clock = db.Column(db.Integer, nullable=False)
    fullmove_number = db.Column(db.Integer, nullable=False)
    is_check = db.Column(db.Boolean, default=False, nullable=False)
    is_checkmate = db.Column(db.Boolean, default=False, nullable=False)
    is_stalemate = db.Column(db.Boolean, default=False, nullable=False)
    games = db.relationship("GamePosition", back_populates="position")
    openings = db.relationship("OpeningPosition", back_populates="position")

    __table_args__ = (
        db.UniqueConstraint(
            "pieces", "turn", "white_can_castle_queenside",
            "white_can_castle_kingside", "black_can_castle_queenside",
            "black_can_castle_kingside", "en_passant_square",
            "halfmove_clock", "fullmove_number"),
    )

    def fen(self):
        color = "w" if self.turn else "b"
        castling = ""
        if self.white_can_castle_kingside:
            castling += "K"
        if self.white_can_castle_queenside:
            castling += "Q"
        if self.black_can_castle_kingside:
            castling += "k"
        if self.black_can_castle_queenside:
            castling += "q"
        if castling == "":
            castling = "-"
        ep_square = chess.SQUARE_NAMES[self.en_passant_square] \
            if self.en_passant_square is not None else "-"
        return "{} {} {} {} {} {}".format(
            self.pieces, color, castling, ep_square,
            self.halfmove_clock, self.fullmove_number)

    def __repr__(self):
        return "Position(id={}, pieces=\"{}\", turn={})".format(
            self.id, self.pieces, self.turn)


class OpeningPosition(db.Model):
    __tablename__ = "opening_position"
    opening_id = db.Column(db.Integer, db.ForeignKey(
        "opening.id", ondelete="CASCADE"), primary_key=True)
    position_id = db.Column(db.Integer, db.ForeignKey(
        "position.id", ondelete="CASCADE"), primary_key=True)
    opening = db.relationship("Opening", back_populates="positions")
    position = db.relationship("Position", back_populates="openings")


class GamePosition(db.Model):
    __tablename__ = "game_position"
    game_id = db.Column(db.Integer, db.ForeignKey(
        "game.id", ondelete="CASCADE"), primary_key=True)
    position_id = db.Column(db.Integer, db.ForeignKey(
        "position.id", ondelete="CASCADE"), primary_key=True)
    game = db.relationship("Game", back_populates="positions")
    position = db.relationship("Position", back_populates="games")


class Game(db.Model):
    __tablename__ = "game"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    slug = db.Column(db.String(256), nullable=False, unique=True)
    positions = db.relationship(
        "GamePosition", back_populates="game",
        order_by=Position.fullmove_number)
    headers = db.relationship("GameHeader")

    def __repr__(self):
        return "Game(id={})".format


class GameHeader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey(
        "game.id", ondelete="CASCADE"))
    key = db.Column(db.String(64), nullable=False)
    value = db.Column(db.String(64), nullable=False)


class Opening(db.Model):
    __tablename__ = "opening"
    id = db.Column(db.Integer, primary_key=True)
    eco = db.Column(db.String(3), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    slug = db.Column(db.String(256), nullable=False, unique=True)
    positions = db.relationship(
        "OpeningPosition", back_populates="opening",
        order_by=Position.fullmove_number)

    def __repr__(self):
        return "Opening(id={}, eco=\"{}\", name=\"{}\")".format(
            self.id, self.eco, self.name
        )
