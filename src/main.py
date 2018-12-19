import numpy as np

from games.chess_game import ChessGame

start_move = np.zeros((8, 8))
end_move = np.zeros((8, 8))

start_move[1, 1] = 1
end_move[2, 1] = 1

move = (start_move, end_move)

chess_game = ChessGame()

print(chess_game.board)
print(start_move)

# Print la taille du vecteur qui permettra d'encoder les mouvements (taille de l'output de notre réseau)
print(chess_game.moves_shape)

print(chess_game.is_move_valid(move))
