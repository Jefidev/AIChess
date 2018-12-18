import chess
import numpy as np

from base.game import Game
from games.chess_util import convertBoardState, convertMove


class ChessGame(Game):

    def __init__(self):
        self.board = chess.Board()
        self.state_vec = convertBoardState(self.board)

        super(ChessGame, self).__init__(64*64)

    def restart(self):
        self.board = chess.Board()
        self.state_vec = convertBoardState(self.board)

    def get_current_state(self):
        return self.state_vec

    def restore_state(self, state):
        NotImplemented

    def perform_move(self, move):
        conv_move = self._convert_vec_to_move(move[0], move[1])

        conv_move = chess.Move.from_uci(conv_move)
        self.board.push(conv_move)
        print(self.board)
        self.state_vec = convertBoardState(self.board)

    def is_move_valid(self, move):
        conv_move = self._convert_vec_to_move(move[0], move[1])
        return (conv_move in [str(m) for m in self.board.legal_moves])

    def turn(self):
        return self.board.turn

    def _convert_vec_to_move(self, start_position, end_position):
        conv_move = convertMove(start_position, end_position)
        return conv_move
