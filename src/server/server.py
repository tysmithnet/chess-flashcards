import chess
import chess.pgn
import os
import random
import sqlite3
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

@app.route("/api/random_move_challenge", methods=["GET"])
def random_move_challenge():
    # get random game id
    conn = sqlite3.connect("./games.db")
    curs = conn.cursor()
    game = None
    while not game:
        curs.execute("select id from game order by random() limit 1;")
        id = curs.fetchone()[0]
        game = Game.get_by_id(id)
        num_moves = len(game.moves)
        if num_moves < 5:
            break
    random_move_index = random.randint(5, len(game.moves) + 1)
    board = chess.Board()
    for i in range(random_move_index + 1):
        game_move = game.moves[i]
        src = chess.SQUARE_NAMES[game_move.move.move_src]
        dst = chess.SQUARE_NAMES[game_move.move.move_dst]
        move = chess.Move.from_uci("{}{}".format(src, dst))
        board.push(move)
    return jsonify(str(board.fen()))


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