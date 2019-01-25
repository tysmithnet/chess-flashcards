import connexion
import six

from swagger_server.models.move import Move  # noqa: E501
from swagger_server.models.opening import Opening  # noqa: E501
from swagger_server import util


def moves_get(fen, legal=None, flags=None):  # noqa: E501
    """Get moves for the given position

     # noqa: E501

    :param fen: FEN of the position to find moves for
    :type fen: str
    :param legal: Only allow legal moves
    :type legal: bool
    :param flags: Restrict the moves to certain types
    :type flags: List[str]

    :rtype: List[Move]
    """
    return {"a": 1}


def openings_get():  # noqa: E501
    """Get all ECO openings

     # noqa: E501


    :rtype: List[Opening]
    """
    return 'do some magic!'


def openings_id_get(id):  # noqa: E501
    """Get an opening and its variants by id

     # noqa: E501

    :param id: ECO id e.g. C42
    :type id: str

    :rtype: List[Opening]
    """
    return 'do some magic!'
