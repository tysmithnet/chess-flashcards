from app import api
from app.models import Game, Opening, User
from app.auth import requires_login
from flask import abort, request, session
from flask_restful import Resource
from webargs import fields
from webargs.flaskparser import parser


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


def create_opening_meta_response(opening):
    return {
        "id": opening.id,
        "eco": opening.eco,
        "name": opening.name,
        "slug": opening.slug,
        "num_moves": len(opening.positions) - 1,
    }


class GameResource(Resource):
    def get(self, id):
        game = Game.query.filter_by(id=id).first_or_404()
        if not game:
            return abort(404)
        return create_game_response(game)


class OpeningMetaResource(Resource):
    def get(self):
        openings = Opening.query.all()
        return list(map(create_opening_meta_response, openings))


class OpeningResource(Resource):
    def get(self, id):
        opening = Opening.query.filter_by(id=id).first_or_404()
        if not opening:
            return abort(404)
        return create_opening_response(opening)


class PlaylistMetaResource(Resource):
    @requires_login()
    def get(self):
        user_id = session["user_id"]
        print(user_id)


class LoginResource(Resource):
    def __init__(self):
        self.login_request_args = {
            "username": fields.Str(required=True),
            "password": fields.Str(required=True)
        }

    def post(self):
        args = parser.parse(self.login_request_args, request)
        username = args["username"]
        password = args["password"]
        user = User.query.filter_by(username=username).one_or_none()
        if not user:
            abort(401)
        if not user.check_password(password):
            return abort(401)
        session["user_id"] = user.id
        return list(map(lambda r: r.name, user.roles))


api.add_resource(LoginResource, "/api/auth")
api.add_resource(GameResource, "/api/game/<int:id>")
api.add_resource(OpeningResource, "/api/opening/<int:id>")
api.add_resource(OpeningMetaResource, "/api/opening/meta")
api.add_resource(PlaylistMetaResource, "/api/playlist/meta")
