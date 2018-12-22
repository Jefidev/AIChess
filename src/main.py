import numpy as np

from games.chess_game import ChessGame
from games.chess_util import convertCaseNameToId

print("main")

start_move = np.zeros((8, 8))
end_move = np.zeros((8, 8))

start_move[1, 1] = 1
end_move[2, 1] = 1

move = (start_move, end_move)

chess_game = ChessGame(True)

print(chess_game.board)
print(start_move)

# Print la taille du vecteur qui permettra d'encoder les mouvements (taille de l'output de notre réseau)
print(chess_game.moves_shape)

print(chess_game.is_move_valid(move))
print([str(m) for m in chess_game.board.legal_moves])

print(chess_game.set_board("r3kbnr/pppppppp/8/8/8/P7/1PPPPPPP/RNBQKBNR b KQkq - 0 1"))

print(chess_game.board)

print(chessGame.get_state_input_model())
