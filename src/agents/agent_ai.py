import random
from base.agent import Agent
from games.chess_game import ChessGame

class Agent_random(Agent):

	# memoire de coups joué

	def __init__(self,treeSearch):
		self.treeSearch = treeSearch

    def get_move(self, state):
        return self.treeSearch.get_best_move(state)
