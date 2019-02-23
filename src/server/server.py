import re
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
        while True:
            curs.execute("select id from game order by random() limit 1;")
            id = curs.fetchone()[0]
            game = Game.get_by_id(id)
            num_moves = len(game.moves)
            if num_moves < 5:
                continue
            random_move_index = random.randint(5, len(game.moves) - 1)
            opportunity_board = chess.Board()
            threat_board = chess.Board()
            game_moves = Enumerable(game.moves).order_by(lambda x: x.order).to_list()
            opportunity_board.turn = not opportunity_board.turn
            is_non_active_player_in_check = opportunity_board.is_check()
            opportunity_board.turn = not opportunity_board.turn
            if opportunity_board.is_check() or is_non_active_player_in_check:
                continue
            else:
                break

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
            is_castle = copy.is_castling(move)
            is_enpassant = copy.is_en_passant(move)
            copy.push(move)
            is_check = copy.is_check()
            is_checkmate = copy.is_checkmate()
            is_stalemate = copy.is_stalemate()
            is_insufficient_material = copy.is_insufficient_material()
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
                    "is_whites_move": copy.turn
                })

        
        # threats
        threats = []
        threat_board.turn = not threat_board.turn
        for move in threat_board.legal_moves:
            copy = chess.Board(fen=threat_board.fen())
            is_capture = copy.is_capture(move)
            promotion = str(move.promotion) if move.promotion else None
            is_castle = copy.is_castling(move)
            is_enpassant = copy.is_en_passant(move)
            copy.push(move)
            is_check = copy.is_check()
            is_checkmate = copy.is_checkmate()
            is_stalemate = copy.is_stalemate()
            is_insufficient_material = copy.is_insufficient_material()
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
                    "is_whites_move": copy.turn
                })

        return jsonify({
            "fen": opportunity_board.fen(),
            "is_whites_move": opportunity_board.turn,
            "opportunities": opportunities,
            "threats": threats,
        })

@app.route("/api/search/games")
def search_games():
    query = request.args.get("q")
    with sqlite3.connect("./games.db") as conn:
        curs = conn.cursor()
        curs.execute("select * from gameheader where game_id in (select distinct(game_id) from gameheader where value like ?)", ("%{}%".format(query),))
        rows = []
        while True:
            res = curs.fetchone()
            if not res:
                break
            rows.append(res)
        inflated = []
        for row in rows:
            inflated.append({
                "id": row[1],
                "key": row[2],
                "value": row[3]
            })
        groups = Enumerable(inflated).group_by(key=lambda x: x["id"], key_names=["id"]).to_list()
        results = []
        for group in groups:
            name_builder = {
                "event": "??",
                "white": "??",
                "black": "??",
                "result": "??",
                "eco": "??"
            }
            for row in group.data:
                if re.match(r"^\s*event\s*$", row["key"], re.I):
                    name_builder["event"] = row["value"]
                elif re.match(r"^\s*eco\s*$", row["key"], re.I):
                    name_builder["eco"] = row["value"]
                elif re.match(r"^\s*white\s*$", row["key"], re.I):
                    name_builder["white"] = row["value"]
                elif re.match(r"^\s*black\s*$", row["key"], re.I):
                    name_builder["black"] = row["value"]
                elif re.match(r"^\s*result\s*$", row["key"], re.I):
                    name_builder["result"] = row["value"]
                
            title = "{} v {} {} {} {}".format(name_builder["white"], name_builder["black"], name_builder["result"], name_builder["event"], name_builder["eco"])
            results.append({
                "id": group.key.id,
                "title": title,
            })
                
    return jsonify(results)


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