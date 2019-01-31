import connexion
import six
import chess
import chess.pgn
from swagger_server.models.move import Move  # noqa: E501
from swagger_server.models.move_factory import create_move_model
from swagger_server.models.opening import Opening  # noqa: E501
from swagger_server.models.opening_meta import OpeningMeta
from swagger_server import util
from swagger_server.openings import OPENINGS
from flask import abort
from fuzzywuzzy import process

def extract_meta_data(opening):
    id = opening.id
    name = opening.name
    variant_names = list(map(lambda v: v.name, opening.variants))
    return OpeningMeta(name, id, variant_names)

def moves_get(fen, flags=None):  # noqa: E501
    """Get moves for the given position

     # noqa: E501

    :param fen: FEN of the position to find moves for
    :type fen: str
    :param flags: Restrict the moves to certain types
    :type flags: List[str]

    :rtype: List[Move]
    """
    board = chess.Board(fen)
    return list(map(lambda x: create_move_model(board, x), board.generate_legal_moves()))

def openings_get():  # noqa: E501
    """Get all ECO openings

     # noqa: E501


    :rtype: List[OpeningMeta]
    """
    return list(map(extract_meta_data, OPENINGS))


def openings_id_get(id):  # noqa: E501
    """Get an opening and its variants by id

     # noqa: E501

    :param id: ECO id e.g. C42
    :type id: str

    :rtype: Opening
    """
    first = next((o for o in OPENINGS if o.id == id), None)
    if first is None:
        abort(404)
    else:
        return first


def openings_search_get(term):  # noqa: E501
    """Fuzzy search for openings

     # noqa: E501

    :param term: Search term to use in search
    :type term: str

    :rtype: List[Opening]
    """
    choices = map(lambda x: x.name, OPENINGS)
    results = process.extract(term, choices)
    results = list(map(lambda x: x[0], results))
    return list(filter(lambda x: x.name in results, OPENINGS))
