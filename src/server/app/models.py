from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class UserRole(db.Model):
    __tablename__ = "user_role"
    user_id = db.Column(db.Integer, db.ForeignKey(
        "user.id", ondelete="CASCADE"), primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey(
        "user.id", ondelete="CASCADE"), primary_key=True)

    def __repr__(self):
        return "UserRole(user_id={}, role_id={})".format(self.user_id,
                                                         self.role_id)


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    roles = db.relationship(
        "Role", secondary=UserRole, back_populates="users")

    def __repr__(self):
        return "User(id={}, username=\"{}\")".format(self.id, self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    users = db.relationship(
        "User", secondary=UserRole, back_populates="roles")

    def __repr__(self):
        return "Role(id={}, name=\"{}\")".format(self.id, self.name)


class OpeningMove(db.Model):
    __tablename__ = "opening_move"
    opening_id = db.Column(db.Integer, db.ForeignKey(
        "opening.id", ondelete="CASCADE"), primary_key=True)
    move_id = db.Column(db.Integer, db.ForeignKey(
        "move.id", ondelete="CASCADE"), primary_key=True)
    order = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "OpeningMove(opening_id={}, move_id={}, order={})".format(
            self.opening_id, self.move_id, self.order)


class GameMove(db.Model):
    __tablename__ = "game_move"
    game_id = db.Column(db.Integer, db.ForeignKey(
        "game.id", ondelete="CASCADE"), primary_key=True)
    move_id = db.Column(db.Integer, db.ForeignKey(
        "move.id", ondelete="CASCADE"), primary_key=True)
    order = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "GameMove(game_id={}, move_id={}, order={})".format(
            self.game_id, self.move_id, self.order
        )


class Game(db.Model):
    __tablename__ = "game"
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(256), nullable=False, unique=True)
    moves = db.relationship(
        "Move", secondary="GameMove", back_populates="games",
        order_by=GameMove.order)
    headers = db.relationship("GameHeader")

    def __repr__(self):
        return "Game(id={})".format


class GameHeader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey(
        "game.id", ondelete="CASCADE"))
    key = db.Column(db.String(64), nullable=False)
    value = db.Column(db.String(64), nullable=False)


class Move(db.Model):
    __tablename__ = "move"
    id = db.Column(db.Integer, primary_key=True)
    start_pos_id = db.Column(db.Integer, db.ForeignKey(
        "position.id", ondelete="CASCADE"), nullable=False)
    end_pos_id = db.Column(db.Integer, db.ForeignKey(
        "position.id", ondelete="CASCADE"), nullable=False)
    src = db.Column(db.Integer, nullable=False)
    dst = db.Column(db.Integer, nullable=False)
    start_pos = db.relationship("Position")
    end_pos = db.relationship("Position")
    games = db.relationship(
        "Game", secondary=GameMove, back_populates="moves", order_by=Game.id)
    openings = db.relationship(
        "Opening", secondary=GameMove, back_populates="moves",
        order_by=Game.id)

    def __repr__(self):
        return "Move(id={}, start_pos_id={}, end_pos_id={}, src={}, dst={})" \
            .format(self.id, self.start_pos_id, self.end_pos_id, self.src,
                    self.dst)


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
    is_check = db.Column(db.Boolean, default=False, nullable=False)
    is_checkmate = db.Column(db.Boolean, default=False, nullable=False)
    is_stalemate = db.Column(db.Boolean, default=False, nullable=False)
    is_check = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return "Position(id={}, pieces=\"{}\", turn={})".format(
            self.id, self.pieces, self.turn)


class Opening(db.Model):
    __tablename__ = "opening"
    id = db.Column(db.Integer, primary_key=True)
    eco = db.Column(db.String(3), primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    slug = db.Column(db.String(256), nullable=False, unique=True)
    moves = db.relationship("Move", secondary=OpeningMove,
                            back_populates="openings",
                            order_by=OpeningMove.order)

    def __repr__(self):
        return "Opening(id={}, eco=\"{}\", name=\"{}\")".format(
            self.id, self.eco, self.name
            )
