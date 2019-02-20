import uuid
import sqlite3
import peewee as pw

sqlite_db = sqlite3.connect("c:\\projects\\chess-flashcards\\src\\server\\games.db")
sqlite_db.close()
db = pw.SqliteDatabase("c:\\projects\\chess-flashcards\\src\\server\\games.db")

class BaseModel(pw.Model):
    class Meta:
        database = db

class Game(BaseModel):
    id = pw.UUIDField(primary_key=True, default=uuid.uuid4)
    hash = pw.TextField(null=False)

Game.add_index(Game.hash, unique=True)

class GameHeader(BaseModel):
    game = pw.ForeignKeyField(Game, backref="headers")
    key = pw.TextField()
    value = pw.TextField()

class Position(BaseModel):
    id = pw.UUIDField(primary_key=True, default=uuid.uuid4)
    fen = pw.TextField(null=False)
    move_num = pw.IntegerField(null=False)
    is_whites_move = pw.BooleanField(default=True)
    is_capture = pw.BooleanField(default=False)
    is_check = pw.BooleanField(default=False)
    is_checkmate = pw.BooleanField(default=False)
    is_stalemate = pw.BooleanField(default=False)
    is_castle = pw.BooleanField(default=False)
    is_enpassant = pw.BooleanField(default=False)
    is_insufficient_material = pw.BooleanField(default=False)

Position.add_index(Position.fen, unique=True)

class Move(BaseModel):
    id = pw.UUIDField(primary_key=True, default=uuid.uuid4)
    start_position = pw.ForeignKeyField(Position, backref="moves_after")
    end_position = pw.ForeignKeyField(Position, backref="moves_before")
    piece = pw.CharField(null=False)
    move_src = pw.IntegerField(null=False)
    move_dst = pw.IntegerField(null=False)
    promotion = pw.CharField(null=True)

Move.add_index(Move.start_position, Move.end_position, unique=True)

class GameMove(BaseModel):
    id = pw.UUIDField(primary_key=True, default=uuid.uuid4)
    game = pw.ForeignKeyField(Game, backref="moves")
    move = pw.ForeignKeyField(Move, backref="games")

GameMove.add_index(GameMove.game, GameMove.move, unique=True)

db.connect()
db.create_tables([Game, GameHeader, Position, Move, GameMove])


if not Position.get_or_none(Position.fen == r"rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):
    start = Position.create(fen=r"rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", is_whites_move=True, move_num=1)

