

class Game(object):

    def __init__(self, moves_shape):
        self.moves_shape = moves_shape

    def get_valid_movements(self):
        NotImplemented

    def get_current_state(self):
        NotImplemented

    def restore_state(self, state):
        NotImplemented

    def is_move_valid(self, move):
        NotImplemented
