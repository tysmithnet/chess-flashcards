import connexion
import six
import chess
import chess.pgn
from swagger_server.models.move import Move  # noqa: E501
from swagger_server.models.move_factory import create_move_model
from swagger_server.models.opening import Opening  # noqa: E501
from swagger_server import util
from swagger_server.openings import OPENINGS

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
    return map(lambda x: create_move_model(board, x), board.generate_legal_moves())

def openings_get():  # noqa: E501
    """Get all ECO openings

     # noqa: E501


    :rtype: List[Opening]
    """
    return OPENINGS


def openings_id_get(id):  # noqa: E501
    """Get an opening and its variants by id

     # noqa: E501

    :param id: ECO id e.g. C42
    :type id: str

    :rtype: List[Opening]
    """
    return 'do some magic!'