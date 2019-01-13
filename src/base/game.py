

class Game(object):

    def __init__(self, moves_shape):
        self.moves_shape = moves_shape

    def restart(self):
        NotImplemented

    def get_current_state(self):
        NotImplemented

    def restore_state(self, state):
        NotImplemented

    def is_move_valid(self, move):
        NotImplemented

    def perform_move(self, move):
        NotImplemented

    def is_game_ended(self, player):
        # Retourne 0 si pas fini, 1 si le joureur gagner -1 si le joueur perd
        # Les joueurs sont numérotés 0 et 1
        NotImplemented

    def get_action_space_size(self):
        NotImplemented
