import os
import sys
import chess
import chess.pgn
import hashlib
import sqlite3
import datetime
import peewee as pw
from models import *
from py_linq import Enumerable

def create_position_model(board, is_capture=False, is_castle=False, is_enpassant=False):
    position = Position.create(fen=board.fen()
    , move_num=board.fullmove_number
    , is_check=board.is_check()
    , is_checkmate=board.is_checkmate()
    , is_enpassant=is_enpassant
    , is_insufficient_material=board.is_insufficient_material()
    , is_stalemate=board.is_stalemate()
    , is_whites_move=board.turn)
    return position

def create_move_model(start_position, end_position, piece, src, dst):
    return Move(start_position=start_position, end_position=end_position, piece=piece, move_src=src, move_dst=dst)

eargs = Enumerable(sys.argv)
exporter = chess.pgn.StringExporter(headers=True, variations=True, comments=True)
i = 0
with open("./src/server/games/Fischer.pgn", "r") as pgn:
    while i < 1000:
        i += 1
        game = chess.pgn.read_game(pgn)
        if not game:
            print("Finished processing {}".format(pgn.name))
            break
        board = game.board()
        game_raw = game.accept(exporter).encode("utf-8")
        game_model = Game.get_or_none(Game.hash == hashlib.md5(game_raw).hexdigest())
        if game_model:
            continue
        game_model = Game.create(hash=hashlib.md5(game_raw).hexdigest())
        game_model.save()
        for header in game.headers:
            header_model = GameHeader.create(game=game_model, key=header, value=game.headers[header])
            header_model.save()

        for move in game.mainline_moves():
            before_fen = board.fen()
            before_position = Position.get_or_none(Position.fen == before_fen)
            piece = str(board.piece_at(move.from_square))
            if not before_position:
                print("Can't find before position! {}".format(before_fen))
                break
            is_capture = board.is_capture(move)
            is_castling = board.is_castling(move)
            is_enpassant = board.is_en_passant(move)
            board.push(move)
            after_fen = board.fen()
            after_position = Position.get_or_none(Position.fen == after_fen)
            if not after_position:
                after_position = create_position_model(board, is_capture=is_capture, is_castle=is_castling, is_enpassant=is_enpassant)
                after_position.save()

            existing_move = Move.get_or_none((Move.start_position == before_position) & (Move.end_position == after_position))
            if not existing_move:                
                existing_move = Move.create(start_position=before_position, end_position=after_position, piece=piece, move_src=move.from_square, move_dst=move.to_square)
                existing_move.save()

            existing_game_move = GameMove.get_or_none((GameMove.game == game_model) & (GameMove.move == existing_move))
            if not existing_game_move:
                existing_game_move = GameMove.create(game=game_model, move=existing_move)
                existing_game_move.save()
        game_model.save()

   
            