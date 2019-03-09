import chess
import chess.pgn
import re
import os
import app.models as m
from app import db


class MoveVisitor(chess.pgn.BaseVisitor):
    def __init__(self):
        self.moves = []

    def visit_move(self, board, move):
        self.moves.append(move)


def create_move(uci):
    src = chess.SQUARE_NAMES[uci.from_square]
    dst = chess.SQUARE_NAMES[uci.to_square]
    return {
        "src": src,
        "dst": dst
    }


abs_path = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(abs_path, "openings.pgn")
pgn = open(file_path)

session = db.session()

openings = []


def create_position_if_necessary(board):
    pieces = board.board_fen()
    is_white = board.turn
    half_move = board.halfmove_clock
    full_move = board.fullmove_number
    white_kingside = bool(board.castling_rights & chess.BB_H1)
    white_queenside = bool(board.castling_rights & chess.BB_A1)
    black_kingside = bool(board.castling_rights & chess.BB_H8)
    black_queenside = bool(board.castling_rights & chess.BB_A8)
    is_check = board.is_check()
    is_checkmate = board.is_checkmate()
    is_stalemate = board.is_stalemate()
    en_passant = board.ep_square
    position_id = None
    with db.engine.connect() as con:
        if en_passant:
            res = con.execute("select id from position where pieces='{}' and turn={} and white_can_castle_kingside={} and white_can_castle_queenside={} and black_can_castle_kingside={} and black_can_castle_queenside={} and en_passant_square={} and fullmove_number={} and halfmove_clock={}".format(pieces, int(is_white), int(white_kingside), int(white_queenside), int(black_kingside), int(black_queenside), en_passant, full_move, half_move))
        else:
            res = con.execute("select id from position where pieces='{}' and turn={} and white_can_castle_kingside={} and white_can_castle_queenside={} and black_can_castle_kingside={} and black_can_castle_queenside={} and en_passant_square is null and fullmove_number={} and halfmove_clock={}".format(pieces, int(is_white), int(white_kingside), int(white_queenside), int(black_kingside), int(black_queenside), full_move, half_move))
        position_id = res.fetchone()
    if position_id:
        return m.Position.query.get(position_id[0])
    
    position = m.Position(
        pieces=pieces, turn=is_white,
        white_can_castle_kingside=white_kingside,
        white_can_castle_queenside=white_queenside,
        black_can_castle_kingside=black_kingside,
        black_can_castle_queenside=black_queenside,
        en_passant_square=en_passant, is_check=is_check,
        is_checkmate=is_checkmate, is_stalemate=is_stalemate)
    session.add(position)
    session.commit()
    return position


def create_opening_if_necessary(eco, name, slug):
    opening = session.query(m.Opening).filter(
        m.Opening.slug == slug
    )
    opening = opening.one_or_none()
    if not opening:
        opening = m.Opening(eco=eco, name=name, slug=slug)
        session.add(opening)
        session.commit()
    return opening


def create_game_name(game, game_num):
    headers = game.headers
    name = str(game_num)
    if "White" in headers:
        name += " " + headers["White"]
    else:
        name += " NN"
    name += " v "
    if "Black" in headers:
        name += " " + headers["Black"]
    else:
        name += " NN"
    if "Event" in headers:
        name += " " + headers["Event"]
    if "Date" in headers:
        name += " " + headers["Date"]
    if "Result" in headers:
        name += " " + headers["Result"]
    return name


# populate openings
while True:
    game = chess.pgn.read_game(pgn)
    if not game:
        break
    # create opening
    eco = game.headers["Site"]
    name = game.headers["White"]
    variant_name = game.headers["Black"]
    if variant_name != "?":
        name += " - {}".format(variant_name)
    name = name.strip()
    name = re.sub(r"\s+", " ", name)
    slug = "{} - {}".format(eco, name)
    slug = re.sub(r"[^0-9a-zA-Z$_.+!*-]", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    print(slug)
    opening = create_opening_if_necessary(eco, name, slug)

    # create moves
    board = chess.Board()
    starting_pos = create_position_if_necessary(board)
    first_opening_position = m.OpeningPosition(
        opening=opening, position=starting_pos)
    session.add(first_opening_position)
    session.commit()
    visitor = MoveVisitor()
    game.accept(visitor)
    moves = visitor.moves
    ending_pos = None
    move_num = 1
    for move in moves:
        board.push(move)
        ending_pos = create_position_if_necessary(board)
        opening_position = m.OpeningPosition(
            opening=opening, position=ending_pos)
        session.add(opening_position)
        session.commit()
        starting_pos = ending_pos
        move_num += 1

# populate games
cwd = os.path.abspath(os.path.dirname(__file__))
game_dir = os.path.join(cwd, "games")
game_filenames = os.listdir(game_dir)
game_num = 0
for game_file in game_filenames:
    pgn = open(os.path.join(game_dir, game_file))
    player_count = 0
    while True:
        game = chess.pgn.read_game(pgn)
        game_num += 1
        if not game or player_count > 400:
            break
        player_count += 1
        board = chess.Board()
        starting_pos = create_position_if_necessary(board)
        visitor = MoveVisitor()
        game.accept(visitor)
        moves = visitor.moves
        name = create_game_name(game, game_num)
        slug = re.sub(r"[^0-9a-zA-Z$_.+!*-]", "-", name)
        slug = re.sub(r"-+", "-", slug)
        print(slug)
        db_game = m.Game(name=name, slug=slug)
        for key in game.headers:
            value = game.headers[key]
            h = m.GameHeader(key=key, value=value)
            db_game.headers.append(h)
        session.add(db_game)
        session.commit()
        first_game_position = m.GamePosition(
            game=db_game, position=starting_pos)
        session.add(first_game_position)
        session.commit()
        ending_pos = None
        move_num = 1
        for move in moves:
            board.push(move)
            ending_pos = create_position_if_necessary(board)
            game_pos = m.GamePosition(game=db_game, position=ending_pos)
            session.add(game_pos)
            session.commit()
            starting_pos = ending_pos
            move_num += 1
