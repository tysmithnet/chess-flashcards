from app import api
from app.models import Game
from flask import abort
from flask_restful import Resource


def create_position_response(position):
    return {
        "pieces": position.pieces,
        "turn": position.turn,
        "white_can_castle_queenside": position.white_can_castle_queenside,
        "white_can_castle_kingside": position.white_can_castle_kingside,
        "black_can_castle_queenside": position.black_can_castle_queenside,
        "black_can_castle_kingside": position.black_can_castle_kingside,
        "en_passant_square": position.en_passant_square,
        "halfmove_clock": position.halfmove_clock,
        "fullmove_number": position.fullmove_number,
        "is_check": position.is_check,
        "is_checkmate": position.is_checkmate,
        "is_stalemate": position.is_stalemate,
    }


def create_game_response(game):
    return {
        "id": game.id,
        "slug": game.slug,
        "positions": list(map(create_position_response, game.positions))
    }


def create_opening_response(opening):
    return {
        "id": opening.id,
        "slug": opening.slug,
        "positions": list(map(create_position_response, opening.positions))
    }


class GameResource(Resource):
    def get(self, id):
        game = Game.query.filter_by(id=id).first_or_404()
        if not game:
            return abort(404)
        return create_game_response(game)


class OpeningResource(Resource):
    def get(self, id):
        opening = Game.query.filter_by(id=id).first_or_404()
        if not opening:
            return abort(404)
        return create_opening_response(opening)


api.add_resource(GameResource, "/game/<int:id>")
api.add_resource(GameResource, "/opening/<int:id>")
