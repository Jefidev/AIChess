import chess
import numpy as np

from base.game import Game
from games.chess_util import convertBoardState, convertMove, convertBoardStateToInputModel, get_castling_state


class ChessGame(Game):

    def __init__(self,player):
        self.board = chess.Board()
        self.state_vec = convertBoardState(self.board)
        self.player = player #True : jeu normal, false : jeu inversé
        self.next_player = True #True : Blanc joue en premier, False : Noir

        super(ChessGame, self).__init__(64*64)

    def restart(self):
        self.board = chess.Board()
        self.state_vec = convertBoardState(self.board)

    def set_board(self,board_val,player,next_player):
        self.board = chess.Board(board_val)
        self.state_vec = convertBoardState(self.board)
        self.player = player #True : jeu normal, false : jeu inversé
        self.next_player = next_player #True : Blanc joue en premier, False : Noir

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
        self.next_player = not self.next_player

    def is_move_valid(self, move):
        conv_move = self._convert_vec_to_move(move[0], move[1])
        return (conv_move in [str(m) for m in self.board.legal_moves])

    def turn(self):
        return self.board.turn

    def _convert_vec_to_move(self, start_position, end_position):
        conv_move = convertMove(start_position, end_position)
        return conv_move

    #Renvoie le plateau en fonction du prochain joueur qui doir jouer
    def get_state(self):
        if(self.next_player):
            player_int = 1 # 1 = joueur blanc
            return convertBoardStateToInputModel(self.state_vec ,self.player,castling,self.board.fullmove_number)
        else:
            player_int = 0 # 0 = joueur noir
            vec_board_mirror = np.flip(np.negative(self.state_vec))

            castling = get_castling_state(self.state_vec,self.board)
            castling_mirror = np.flip(castling)

            return convertBoardStateToInputModel(vec_board_mirror,player_int,castling_mirror,self.board.fullmove_number)


    def get_state_input_model(self,mirror=False):

        #castling = [haut-gauche,haut-droite,bas-gauche,bas-droite]
        castling = get_castling_state(self.state_vec,self.board)

        if(self.player ^ mirror) : 
            player_int = 1
            return convertBoardStateToInputModel(self.state_vec ,self.player,castling,self.board.fullmove_number)

        else : 
            player_int = 0
            vec_board_mirror = np.flip(np.negative(self.state_vec))

            castling = get_castling_state(self.state_vec,self.board)
            castling_mirror = np.flip(castling)

            return convertBoardStateToInputModel(vec_board_mirror,player_int,castling_mirror,self.board.fullmove_number)
    

