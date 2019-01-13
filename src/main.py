import numpy as np

from games.chess_game import ChessGame
from games.chess_util import convertCaseNameToId

print("main")

move = np.zeros((64, 64)) 
move[2][2] = 1

chess_game = ChessGame(True)

print(move)

print(chess_game.board)

# Print la taille du vecteur qui permettra d'encoder les mouvements (taille de l'output de notre réseau)
print(chess_game.moves_shape)

print(chess_game.is_move_valid(move))
print([str(m) for m in chess_game.board.legal_moves])

print(chess_game.set_board("r3kbnr/pppppppp/8/8/8/P7/1PPPPPPP/RNBQKBNR b KQkq - 0 1",True,True))

print(chess_game.board)

print(chess_game.get_state_input_model())
