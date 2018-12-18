import chess
import numpy as np
from chess_util import convertBoardState,convertMove




class ChessGame:

    def __init__(self):
        self.board = chess.Board()   
        self.state_vec = convertBoardState(self.board)

        
    def restart(self):
        self.board = chess.Board()   
        self.state_vec = convertBoardState(self.board)

    def get_state(self):
        return self.state_vec

    #pos_before et pos_after est un np.array (8 * 8) qui indique la position passée et futur
    def move_vec(self,pos_before,pos_after):
        move = convertMove(pos_before,pos_after)
        print(move)
        self.move_case(move)

    def move_case(self,move):
        move = chess.Move.from_uci(move)
        self.board.push(move) 
        print(self.board)
        self.state_vec = convertBoardState(self.board)


    def check_move(self,pos_before,pos_after):
        move = convertMove(pos_before,pos_after)
        return ( move in [str(m) for m in self.board.legal_moves])



    

