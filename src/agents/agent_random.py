import random
from base.agent import Agent

class Agent_random(Agent):

	def __init__(self, game):
		self.game = game

    def get_move(self, state):
        moves = game.get_valid_movements()
        return random.choice(moves)
