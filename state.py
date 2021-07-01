import numpy as np
from board2 import board
class GameMove(object):
    def __init__(self, move, table):
        self.move = move
        self.table = table

    def __repr__(self):
        return  "move:"+str(self.value)

class GameState(object):
    P1 = 1
    P2 = -1
    def __init__(self, state, next_to_move=1,c_move=None):
        self.board = state
        self.next_to_move = next_to_move
        self.current_move = c_move

    @property
    def game_result(self):
        # check if game is over
        status = self.board.check_score()
        if status == 1:
            return 1.
        elif status == -1:
            return -1.
        else:
            # if not over - no result
            return None

    def is_game_over(self):
        return self.game_result is not None

    def is_move_legal(self, move):
        return self.board.move_check(move.value, move.table)

    def move(self, move):
        new_board = board.game_array
        new_board.player_move(move.table)
        next_to_move = GameState.P2 if self.next_to_move == GameState.P1 else GameState.P1
        return GameState(new_board, next_to_move, move)

    def get_legal_actions(self):
        possibleStates = []
        moves = self.next_to_move
        availableMoves = self.board.get_Possible_Moves(moves)
        for move in availableMoves:
            i = move[i]
            j = move[j]
            possibleStates.append(GameMove(self.next_to_move, self.table,i,j))
        return possibleStates