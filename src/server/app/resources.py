from app import api, session_scope
from app.models import Game, Opening, User, GamePlaylist, OpeningPlaylist, \
    OpeningPlaylistOpening, GamePlaylistGame
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


def create_game_playlist_response(game_playlist):
    return {
        "id": game_playlist.id,
        "name": game_playlist.name,
        "created": str(game_playlist.created),
        "games": list(map(lambda g: g.game.id, game_playlist.games))
    }


def create_opening_playlist_response(opening_playlist):
    return {
        "id": opening_playlist.id,
        "name": opening_playlist.name,
        "created": str(opening_playlist.created),
        "openings": list(map(
            lambda o: o.opening.id, opening_playlist.openings))
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


class OpeningPlaylistResource(Resource):
    def __init__(self):
        self.create_playlist_args = {
            "name": fields.Str(required=True),
            "ids": fields.List(fields.Integer, required=True)
        }
        self.update_playlist_args = {
            "name": fields.Str(),
            "ids": fields.List(fields.Integer)
        }

    def get(self, user_id=None, id=None):
        if user_id is not None:
            user = User.query.get(user_id)
            if user is None:
                return abort(404)
            return list(map(
                create_opening_playlist_response, user.opening_playlists))
        if id is not None:
            playlist = OpeningPlaylist.query.get(id)
            if playlist is None:
                return abort(404)
            return create_opening_playlist_response(playlist)
        return abort(400)

    @requires_login()
    def post(self):
        with session_scope() as s:
            args = parser.parse(self.create_playlist_args)
            user_id = session["user_id"]
            openings = Opening.query.filter(Opening.id.in_(args["ids"]))
            playlist = OpeningPlaylist(name=args["name"], owner=user_id)
            s.add(playlist)
            for opening in openings:
                new_link = OpeningPlaylistOpening(
                    playlist=playlist, opening=opening)
                s.add(new_link)
            s.commit()
            return create_opening_playlist_response(playlist)

    @requires_login()
    def put(self, id):
        with session_scope() as s:
            playlist = OpeningPlaylist.query.get(id)
            if playlist is None:
                return abort(404)
            args = parser.parse(self.update_playlist_args)
            if "name" in args:
                playlist.name = args["name"]
            if "ids" in args:
                for opening_link in playlist.openings:
                    s.delete(opening_link)
                openings = Opening.query.filter(Opening.id.in_(args["ids"]))
                for opening in openings:
                    new_link = OpeningPlaylistOpening(
                        playlist=playlist, opening=opening)
                    s.add(new_link)
            s.commit()
            return create_opening_playlist_response(playlist)


class GamePlaylistResource(Resource):
    def __init__(self):
        self.create_playlist_args = {
            "name": fields.Str(required=True),
            "ids": fields.List(fields.Integer, required=True)
        }
        self.update_playlist_args = {
            "name": fields.Str(),
            "ids": fields.List(fields.Integer)
        }

    def get(self, user_id=None, id=None):
        if user_id is not None:
            user = User.query.get(user_id)
            if user is None:
                return abort(404)
            return list(map(
                create_game_playlist_response, user.game_playlists))
        if id is not None:
            playlist = GamePlaylist.query.get(id)
            if playlist is None:
                return abort(404)
            return create_game_playlist_response(playlist)
        return abort(400)

    @requires_login()
    def post(self):
        with session_scope() as s:
            args = parser.parse(self.create_playlist_args)
            user_id = session["user_id"]
            games = Game.query.filter(Game.id.in_(args["ids"]))
            playlist = GamePlaylist(name=args["name"], owner=user_id)
            s.add(playlist)
            for game in games:
                new_link = GamePlaylistGame(
                    playlist=playlist, game=game)
                s.add(new_link)
            s.commit()
            return create_game_playlist_response(playlist)

    @requires_login()
    def put(self, id):
        with session_scope() as s:
            playlist = GamePlaylist.query.get(id)
            if playlist is None:
                return abort(404)
            args = parser.parse(self.update_playlist_args)
            if "name" in args:
                playlist.name = args["name"]
            if "ids" in args:
                for game_link in playlist.games:
                    s.delete(game_link)
                games = Game.query.filter(Game.id.in_(args["ids"]))
                for game in games:
                    new_link = GamePlaylistGame(
                        playlist=playlist, game=game)
                    s.add(new_link)
            s.commit()
            return create_game_playlist_response(playlist)


api.add_resource(LoginResource, "/api/login")
api.add_resource(GameResource, "/api/game/<int:id>")
api.add_resource(OpeningResource, "/api/opening/<int:id>")
api.add_resource(OpeningMetaResource, "/api/opening/meta")
api.add_resource(
    OpeningPlaylistResource,
    "/api/playlist/opening",
    "/api/playlist/opening/<int:id>",
    "/api/user/<int:user_id>/playlist/opening",
)
api.add_resource(
    GamePlaylistResource,
    "/api/playlist/game",
    "/api/playlist/game/<int:id>",
    "/api/user/<int:user_id>/playlist/game",
)