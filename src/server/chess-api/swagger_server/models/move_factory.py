import chess
from swagger_server.models.move import Move

def create_move_model(board, move):
    copy = board.copy()
    fen_before = board.fen()
    src = chess.square_name(move.from_square)
    dst = chess.square_name(move.to_square)
    piece = copy.piece_at(move.from_square).symbol()
    is_enpessant = copy.is_en_passant(move)
    is_capture = copy.is_capture(move)
    is_castle = copy.is_castling(move)
    captured_piece = None
    if is_capture:
        captured_piece = copy.piece_at(move.to_square).symbol()
    if is_enpessant:
        if copy.turn:
            captured_piece = "p"
        else:
            captured_piece = "P"
    copy.push(move)
    fen_after = copy.fen()
    is_check = copy.is_check()
    is_mate = copy.is_checkmate()
    is_stalemate = copy.is_stalemate()
    return Move(piece, src, dst, is_check=is_check, is_mate=is_mate, 
        is_stalemate=is_stalemate, is_enpessant=is_enpessant, 
        is_castle=is_castle, captured_piece=captured_piece, 
        fen_before=fen_before, fen_after=fen_after)

def create_move_models(board, moves):
    copy = board.copy()
    models = []
    for move in moves:
        model = create_move_model(copy, move)
        models.append(model)
        copy.push(move)

    return models