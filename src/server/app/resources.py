from app import api
from app.models import Game, Opening, OpeningPlaylist
from flask import abort
from flask_restful import Resource


def create_position_response(position):
    return {
        "pieces": position.position.pieces,
        "turn": position.position.turn,
        "white_can_castle_queenside":
            position.position.white_can_castle_queenside,
        "white_can_castle_kingside":
            position.position.white_can_castle_kingside,
        "black_can_castle_queenside":
            position.position.black_can_castle_queenside,
        "black_can_castle_kingside":
            position.position.black_can_castle_kingside,
        "en_passant_square": position.position.en_passant_square,
        "halfmove_clock": position.position.halfmove_clock,
        "fullmove_number": position.position.fullmove_number,
        "is_check": position.position.is_check,
        "is_checkmate": position.position.is_checkmate,
        "is_stalemate": position.position.is_stalemate,
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


def create_playlist_meta_response(game_playlists, opening_playlists):
    return {
        "game_playlists": list(map(lambda x: {
            "id": x.id,
            "name": x.name,
            "num_items": len(x.games)
        })),
        "opening_playlists": list(map(lambda x: {
            "id": x.id,
            "name": x.name,
            "num_items": len(x.openings)
        }))
    }


class GameResource(Resource):
    def get(self, id):
        game = Game.query.filter_by(id=id).first_or_404()
        if not game:
            return abort(404)
        return create_game_response(game)


class OpeningResource(Resource):
    def get(self, id):
        opening = Opening.query.filter_by(id=id).first_or_404()
        if not opening:
            return abort(404)
        return create_opening_response(opening)


class PlaylistMetaResource(Resource):
    def get(self, user_id):
        pass


api.add_resource(GameResource, "/game/<int:id>")
api.add_resource(OpeningResource, "/opening/<int:id>")
api.add_resource(PlaylistMetaResource, "/playlist/meta/<int:user_id>")
