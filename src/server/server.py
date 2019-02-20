import chess
import chess.pgn
import os
import random
import sqlite3
from py_linq import Enumerable
from models import *
from flask import Flask, jsonify, send_from_directory, request
from openings import OPENINGS

from_main = False

app = Flask(__name__)

@app.route("/api/openings", methods=["GET"])
def openings():
    return jsonify(OPENINGS)

@app.route("/api/moves", methods=["POST"])
def moves():
    game_moves = list(request.get_json()["moves"])
    board = chess.Board()
    ret = []
    for move in game_moves:
        src = move["src"]
        dst = move["dst"]
        board.push_uci("{}{}".format(src, dst))
    for move in board.generate_legal_moves():
        ret.append({
            "src": chess.square_name(move.from_square),
            "dst": chess.square_name(move.to_square)
        })
    return jsonify(ret)

@app.route("/api/random-move-challenge", methods=["GET"])
def random_move_challenge():
    # get random game id
    with sqlite3.connect("./games.db") as conn:
        curs = conn.cursor()
        game = None
        i = 0
        while not game:
            curs.execute("select id from game order by random() limit 1;")
            id = curs.fetchone()[0]
            game = Game.get_by_id(id)
            num_moves = len(game.moves)
            if num_moves < 5:
                break
        random_move_index = random.randint(5, len(game.moves))
        opportunity_board = chess.Board()
        threat_board = chess.Board()
        game_moves = Enumerable(game.moves).order_by(lambda x: x.order).to_list()
        for i in range(random_move_index + 1):
            game_move = game_moves[i]
            src = chess.SQUARE_NAMES[game_move.move.move_src]
            dst = chess.SQUARE_NAMES[game_move.move.move_dst]
            move = chess.Move.from_uci("{}{}".format(src, dst))
            opportunity_board.push(move)
            threat_board.push(move)
        opportunities = []
        # opportunities
        for move in opportunity_board.legal_moves:
            copy = chess.Board(fen=opportunity_board.fen())
            is_capture = copy.is_capture(move)
            promotion = str(move.promotion) if move.promotion else None
            is_castle = opportunity_board.is_castling(move)
            is_enpassant = opportunity_board.is_en_passant(move)
            print("BEFORE: {}".format(copy.fen()))
            copy.push(move)
            print("AFTER : {}".format(copy.fen()))
            is_check = opportunity_board.is_check()
            is_checkmate = opportunity_board.is_checkmate()
            is_stalemate = opportunity_board.is_stalemate()
            is_insufficient_material = opportunity_board.is_insufficient_material()
            if is_capture or is_check or is_checkmate:
                opportunities.append({
                    "src": chess.SQUARE_NAMES[move.from_square],
                    "dst": chess.SQUARE_NAMES[move.to_square],
                    "is_capture": is_capture,
                    "promotion": promotion,
                    "is_check": is_check,
                    "is_checkmate": is_checkmate,
                    "is_stalemate": is_stalemate,
                    "is_castle": is_castle,
                    "is_enpassant": is_enpassant,
                    "is_insufficient_material": is_insufficient_material,
                    "is_whites_move": opportunity_board.turn
                })

        
        # threats
        threats = []
        threat_board.turn = not threat_board.turn
        for move in threat_board.legal_moves:
            copy = chess.Board(fen=threat_board.fen())
            is_capture = copy.is_capture(move)
            promotion = str(move.promotion) if move.promotion else None
            is_castle = threat_board.is_castling(move)
            is_enpassant = threat_board.is_en_passant(move)
            copy.push(move)
            is_check = threat_board.is_check()
            is_checkmate = threat_board.is_checkmate()
            is_stalemate = threat_board.is_stalemate()
            is_insufficient_material = threat_board.is_insufficient_material()
            if is_capture or is_check or is_checkmate:
                threats.append({
                    "src": chess.SQUARE_NAMES[move.from_square],
                    "dst": chess.SQUARE_NAMES[move.to_square],
                    "is_capture": is_capture,
                    "promotion": promotion,
                    "is_check": is_check,
                    "is_checkmate": is_checkmate,
                    "is_stalemate": is_stalemate,
                    "is_castle": is_castle,
                    "is_enpassant": is_enpassant,
                    "is_insufficient_material": is_insufficient_material,
                    "is_whites_move": threat_board.turn
                })

        return jsonify({
            "fen": opportunity_board.fen(),
            "is_whites_move": opportunity_board.turn,
            "opportunities": opportunities,
            "threats": threats,
        })


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    global from_main
    base = "../../dist/client"
    if path == "" or path == "/":
        path = "index.html"
    if from_main:
        base = "client"
    base = os.path.abspath(base)
    if os.path.exists(os.path.join(base, path)):
        return send_from_directory(base, path)
    else:
        return send_from_directory(base, "index.html")

if __name__ == "__main__":
    from_main = True
    app.run(port=8080)