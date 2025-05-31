"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

BOARD_SIZE = 3

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    flat_board = [cell for row in board for cell in row]

    x_count = flat_board.count(X)
    o_count = flat_board.count(O)

    if x_count <= o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == EMPTY:
                moves.add((i, j))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if board[i][j] != EMPTY:
        raise Exception("Invalid action!")

    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)

    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    lines = []

    # Rows and columns

    for i in range(BOARD_SIZE):
        lines.append(board[i])
        lines.append([board[0][i], board[1][i], board[2][i]])

    # Diagonals

    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])

    for line in lines:
        if line[0] is not None and line.count(line[0]) == 3:
            return line[0]

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for row in board:
        if EMPTY in row:
            return False

    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)

    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        value = float('-inf')
        best_move = None
        for action in actions(board):
            move_val = min_value(result(board, action))
            if move_val > value:
                value = move_val
                best_move = action
            return best_move

    else:
        value = float('inf')
        best_move = None
        for action in actions(board):
            move_val = max_value(result(board, action))
            if move_val < value:
                value = move_val
                best_move = action
        return best_move

def max_value(board):
    if terminal(board):
        return utility(board)
    v = float('-inf')
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = float('inf')
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v