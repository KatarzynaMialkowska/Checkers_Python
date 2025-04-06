from copy import deepcopy
from checkers.constants import PIECES_G1, PIECES_G2


def minimax(board, depth, is_max_player, game):
    if depth == 0 or board.is_winner() != None:
        return board.score(), board

    if is_max_player:
        maxScore = float('-inf')
        best_move = None
        for move in get_all_moves(board, PIECES_G2):
            rate = minimax(move, depth-1, False, game)[0]
            maxScore = max(maxScore, rate)
            if maxScore == rate:
                best_move = move

        return maxScore, best_move
    else:
        minScore = float('inf')
        best_move = None
        for move in get_all_moves(board, PIECES_G1):
            rate = minimax(move, depth-1, True, game)[0]
            minScore = min(minScore, rate)
            if minScore == rate:
                best_move = move

        return minScore, best_move


def get_all_moves(board, color):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_square(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, skip)
            moves.append(new_board)

    return moves


def simulate_move(piece, move, board, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove_skipped_piece(skip)

    return board
