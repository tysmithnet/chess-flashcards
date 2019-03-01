from app import api
from app.models import Game
from flask import abort
from flask_restful import Resource


def create_game_response(game):
    return {
        "id": game.id,
        "slug": game.slug
    }


class GameResource(Resource):
    def get(self, id):
        game = Game.query.filter_by(id=id).first_or_404()
        if not game:
            return abort(404)
        return create_game_response(game)


api.add_resource(GameResource, "/game/<int:id>")
