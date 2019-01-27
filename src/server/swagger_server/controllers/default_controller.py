import connexion
import six
import chess
from swagger_server.models.move import Move  # noqa: E501
from swagger_server.models.opening import Opening  # noqa: E501
from swagger_server import util


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
    moves = []
    for move in board.generate_legal_moves():
        copy = chess.Board(fen)
        src = chess.square_name(move.from_square)
        dst = chess.square_name(move.to_square)
        piece = copy.piece_at(move.from_square).symbol()
        is_enpessant = copy.is_en_passant(move)
        is_capture = copy.is_capture(move)
        is_castle = copy.is_castling(move)
        captured_piece = None
        if is_capture:
            captured_piece = copy.piece_at(move.to_square)
        if is_enpessant:
            if copy.turn:
                captured_piece = "p"
            else:
                captured_piece = "P"
        copy.push(move)
        is_check = copy.is_check()
        is_mate = copy.is_checkmate()
        is_stalemate = copy.is_stalemate()
        m = Move(piece, src, dst, is_check=is_check, is_mate=is_mate, is_stalemate=is_stalemate, is_enpessant=is_enpessant, is_castle=is_castle, captured_piece=captured_piece)
        moves.append(m)
    return moves


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
