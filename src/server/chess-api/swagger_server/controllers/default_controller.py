import connexion
import six

from swagger_server.models.fen_request import FenRequest  # noqa: E501
from swagger_server.models.move import Move  # noqa: E501
from swagger_server.models.opening import Opening  # noqa: E501
from swagger_server.models.opening_meta import OpeningMeta  # noqa: E501
from swagger_server import util


def fen_post(body):  # noqa: E501
    """Apply the provided moves to the provided FEN

    The position on the board, described in FEN notation, is to have the moves applied to it, and the resulting FEN returned # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = FenRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def moves_get(fen, flags=None):  # noqa: E501
    """Get moves for the given position

     # noqa: E501

    :param fen: FEN of the position to find moves for
    :type fen: str
    :param flags: Restrict the moves to certain types
    :type flags: List[str]

    :rtype: List[Move]
    """
    return 'do some magic!'


def openings_get():  # noqa: E501
    """Get all ECO openings

     # noqa: E501


    :rtype: List[OpeningMeta]
    """
    return 'do some magic!'


def openings_id_get(id):  # noqa: E501
    """Get an opening and its variants by id

     # noqa: E501

    :param id: ECO id e.g. C42
    :type id: str

    :rtype: Opening
    """
    return 'do some magic!'


def openings_search_get(term):  # noqa: E501
    """Fuzzy search for openings

     # noqa: E501

    :param term: Search term to use in search
    :type term: str

    :rtype: List[Opening]
    """
    return 'do some magic!'
