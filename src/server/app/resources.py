from app import api, session_scope
from app.models import Game, Opening, User, GamePlaylist, OpeningPlaylist, \
    OpeningPlaylistOpening, GamePlaylistGame, GameAttempt, OpeningAttempt
from app.auth import requires_login
from flask import abort, request, session
from flask_restful import Resource
from webargs import fields
from webargs.flaskparser import parser


def create_user_response(user):
    return {
        "id": user.id,
        "username": user.username,
        "roles": list(map(lambda x: x.name, user.roles))
    }


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
        "is_check": position.position.is_check,
        "is_checkmate": position.position.is_checkmate,
        "is_stalemate": position.position.is_stalemate,
    }


def create_game_response(game):
    return {
        "id": game.id,
        "slug": game.slug,
        "headers": {h["key"]: h["value"] for h in game.headers},
        "positions": list(map(create_position_response, game.positions))
    }


def create_opening_response(opening):
    return {
        "id": opening.id,
        "eco": opening.eco,
        "name": opening.name,
        "slug": opening.slug,
        "positions": list(map(create_position_response, opening.positions))
    }


def create_game_playlist_response(game_playlist):
    return {
        "id": game_playlist.id,
        "type": "game",
        "name": game_playlist.name,
        "created": str(game_playlist.created),
        "ids": list(map(lambda g: g.game.id, game_playlist.games))
    }


def create_opening_playlist_response(opening_playlist):
    return {
        "id": opening_playlist.id,
        "type": "opening",
        "name": opening_playlist.name,
        "created": str(opening_playlist.created),
        "ids": list(map(
            lambda o: o.opening.id, opening_playlist.openings))
    }


def create_game_meta_response(game):
    return {
        "id": game.id,
        "name": game.name,
        "slug": game.slug,
        "num_moves": len(game.positions) - 1,
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


class GameMetaResource(Resource):
    def get(self):
        games = Game.query.all()
        return list(map(create_game_meta_response, games))


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


class OpeningBatchResource(Resource):
    def __init__(self):
        self.batch_request_args = {
            "ids": fields.List(fields.Integer, required=True)
        }

    def post(self):
        args = parser.parse(self.batch_request_args)
        ids = args["ids"]
        openings = Opening.query.filter(Opening.id.in_(ids)).all()
        return list(map(create_opening_response, openings))


class PlaylistItemRecommendation(Resource):
    def __init__(self):
        self.opening_query = """with rec_cte as (
select opo.opening_id,
    (select count() from opening_attempt oa where oa.opening_id
        = opo.opening_id and oa.success = 1) as num_success,
    (select count() from opening_attempt oa where oa.opening_id
        = opo.opening_id) as total
from opening_playlist_opening opo
where opo.playlist_id = :id
) select * from rec_cte order by num_success asc, total desc"""

    @requires_login()
    def get(self, cat, id):
        user_id = session["user_id"]
        if cat == "opening":
            with session_scope() as s:
                playlist = OpeningPlaylist.query.get(id)
                if not playlist:
                    return abort(404)
                if playlist.owner != user_id:
                    return abort(401)
                res = s.execute(self.opening_query, {"id": id}).fetchall()
                opening_id = res[0][0]
                opening = Opening.query.get(opening_id)
                return create_opening_response(opening)


class LoginResource(Resource):
    def __init__(self):
        self.login_request_args = {
            "username": fields.Str(required=True),
            "password": fields.Str(required=True)
        }

    @requires_login()
    def get(self):
        user_id = session["user_id"]
        u = User.query.get(user_id)
        if not u:
            return abort(401)
        return create_user_response(u)

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
        return create_user_response(user)


class PlaylistResource(Resource):
    def __init__(self):
        self.create_playlist_args = {
            "name": fields.Str(required=True),
            "ids": fields.List(fields.Integer, required=True)
        }

        self.update_playlist_args = {
            "name": fields.Str(allow_missing=True),
            "ids": fields.List(fields.Integer, allow_missing=True)
        }

        self.delete_playlists_args = {
            "ids": fields.List(fields.Integer, required=True)
        }

    @requires_login()
    def get(self, cat=None, id=None):
        user_id = session["user_id"]
        if cat is None:
            opening_playlists = OpeningPlaylist.query.filter_by(owner=user_id)
            game_playlists = GamePlaylist.query.filter_by(owner=user_id)
            return {
                "opening": list(map(
                    create_opening_playlist_response, opening_playlists)),
                "game":
                    list(map(create_game_playlist_response, game_playlists))
            }
        if cat == "opening":
            if id is not None:
                opening = OpeningPlaylist.query.get(id)
                if opening is None:
                    return abort(404)
                return create_opening_playlist_response(opening)
            opening_playlists = OpeningPlaylist.query.filter_by(owner=user_id)
            return create_opening_playlist_response(opening_playlists)
        elif cat == "game":
            if id is not None:
                game = GamePlaylist.query.get(id)
                if game is None:
                    return abort(404)
                return create_game_playlist_response(game)
            game_playlists = GamePlaylist.query.filter_by(owner=user_id)
            return create_game_playlist_response(game_playlists)
        else:
            return abort(404)

    @requires_login()
    def post(self, cat=None, id=None):
        with session_scope() as s:
            user_id = session["user_id"]
            args = parser.parse(self.create_playlist_args)
            name = args["name"]
            if cat == "opening":
                playlist = OpeningPlaylist(owner=user_id, name=name)
                s.add(playlist)
                for i in list(set(args["ids"])):
                    opening = Opening.query.get(i)
                    if opening is None:
                        continue
                    link = OpeningPlaylistOpening(
                        playlist=playlist, opening=opening)
                    s.add(link)
                    playlist.openings.append(link)
                s.commit()
                return create_opening_playlist_response(playlist)
            elif cat == "game":
                playlist = GamePlaylist(owner=user_id, name=name)
                s.add(playlist)
                for i in list(set(args["ids"])):
                    game = Game.query.get(i)
                    if game is None:
                        continue
                    link = GamePlaylistGame(
                        playlist=playlist, game=game)
                    s.add(link)
                    playlist.games.append(link)
                s.commit()
                return create_game_playlist_response(playlist)
            else:
                return abort(400)

    @requires_login()
    def put(self, cat=None, id=None):
        args = parser.parse(self.update_playlist_args)
        with session_scope() as s:
            if cat == "opening":
                playlist = OpeningPlaylist.query.get(id)
                if playlist is None:
                    return abort(404)
                for link in playlist.openings:
                    s.delete(link)
                for i in list(set(args["ids"])):
                    opening = Opening.query.get(i)
                    if opening is None:
                        continue
                    link = OpeningPlaylistOpening(
                        playlist=playlist, opening=opening)
                    s.add(link)
                    playlist.openings.append(link)
                s.commit()
                return create_opening_playlist_response(playlist)
            elif cat == "game":
                playlist = GamePlaylist.query.get(id)
                if playlist is None:
                    return abort(404)
                for link in playlist.games:
                    s.delete(link)
                for i in list(set(args["ids"])):
                    game = Game.query.get(i)
                    if game is None:
                        continue
                    link = GamePlaylistGame(
                        playlist=playlist, game=game)
                    s.add(link)
                    playlist.games.append(link)
                s.commit()
                return create_game_playlist_response(playlist)
            else:
                return abort(404)

    @requires_login()
    def delete(self, cat):
        with session_scope() as s:
            args = parser.parse(self.delete_playlists_args)
            ids = args["ids"]
            if cat == "opening":
                for i in ids:
                    playlist = OpeningPlaylist.query.get(i)
                    if playlist is None:
                        continue
                    for link in playlist.openings:
                        s.delete(link)
                    s.delete(playlist)
                s.commit()
            elif cat == "game":
                for i in ids:
                    playlist = GamePlaylist.query.get(i)
                    if playlist is None:
                        continue
                    for link in playlist.games:
                        s.delete(link)
                    s.delete(playlist)
                s.commit()
            else:
                return abort(404)


class StatsResource(Resource):
    def __init__(self):
        self.add_attempt_args = {
            "success": fields.Boolean(required=True)
        }

    @requires_login()
    def get(self, cat, id):
        user_id = session["user_id"]
        attempts = []
        if cat == "game":
            attempts = GameAttempt.query.filter_by(
                user_id=user_id, game_id=id).all()
        if cat == "opening":
            attempts = OpeningAttempt.query.filter_by(
                user_id=user_id, opening_id=id).all()
        if not attempts:
            attempts = []
        return {
            "attempts": len(attempts),
            "successes": len(list(filter(lambda a: a.success, attempts)))
        }

    @requires_login()
    def post(self, cat, id):
        with session_scope() as s:
            user_id = session["user_id"]
            args = parser.parse(self.add_attempt_args)
            success = args["success"]
            if cat == "opening":
                attempt = OpeningAttempt(
                    user_id=user_id, opening_id=id, success=success)
            if cat == "game":
                attempt = GameAttempt(
                    user_id=user_id, game_id=id, success=success)
            if attempt:
                s.add(attempt)
                s.commit()


api.add_resource(LoginResource, "/api/login")
api.add_resource(GameResource, "/api/game/<int:id>")
api.add_resource(OpeningResource, "/api/opening/<int:id>")
api.add_resource(OpeningMetaResource, "/api/opening/meta")
api.add_resource(PlaylistResource, "/api/playlist",
                 "/api/playlist/<string:cat>",
                 "/api/playlist/<string:cat>/<int:id>")
api.add_resource(PlaylistItemRecommendation,
                 "/api/playlist/recommendation/<string:cat>/<int:id>")
api.add_resource(StatsResource, "/api/stats/<string:cat>/<int:id>")
api.add_resource(GameMetaResource, "/api/game/meta")
