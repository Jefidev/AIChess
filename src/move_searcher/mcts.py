import math

import numpy as np

from games.chess_util import neural_output_to_move


class MCTS(object):

    def __init__(self, game, nnet, temp, nbr_sim=1000):
        # Expected reward for taking action a from s
        self.Qsa = {}

        # Nbr of time action a has been taken from s
        self.Nsa = {}

        # Nbr of time s was visited
        self.Ns = {}

        # Initial policy for s given by the neuralnet
        self.Ps = {}

        self.game = game
        self.nnet = nnet
        self.temp = temp
        self.nbr_simulation = nbt_sim

        self.EPS = 1e-8

    def get_actions(self, state, t=1):

        for i in range(self.nbr_simulation):
            self.game.restore_state(state)
            self.search(state)

        nbr_actions = self.game.getActionSize()
        counts = [self.Nsa[(state, a)], if (state, a) in self.Nsa else 0 for a in range(nbr_actions)]

        if t == 0:
            # On ne prend que la meilleur action sans en explorer d'autres
            bestA = np.argmax(counts)
            proba = [0] * len(counts)

            proba[bestA] = 1
            return proba

        counts = [x**(1./temp) for x in counts]
        proba = [x/float(sum(counts)) for x in counts]
        return proba

    def search(self, state):

        # Si le noeud atteint et la fin du jeu, on backpropage le résultat
        ended = game.is_game_ended()

        if ended:
            return -ended

        # Si le noeud n'a jamais été évalué par le NN
        if state not in self.Ps:
            return self._process_new_node(state)

        # On est pas à un noeud feuille, on va choisir par ou descendre
        valid_moves = self.game.get_valid_moves()
        cur_best = -float("inf")
        best_action = -1

        # Calculer la Upper Confidence U(s,a)
        for a_idx in range(self.game.get_action_space_size()):

            if valid_moves[a_idx]:
                u = self._compute_upper_confidence(a_idx, state)

                if u > cur_best:
                    cur_best = u
                    best_action = a_idx

        move = neural_output_to_move(a_idx)
        self.game.perform_move()
        new_state = self.game.get_current_state()

        v = self.search(new_state)

        # Grâce aux info de la search sur mon enfant, je peux update mes info
        self._update_node_info(state, a_idx, v)
        self.Ns[state] += 1

        return -v

    def _process_new_node(self, state):

        proba, V = self.nnet.predict(state)
        valid_moves = self.game.get_valid_moves()

        # On masque les mouvements invalides
        proba = proba * valid_moves
        sum_proba = np.sum(proba)

        if sum_proba > 0:
            # On renormalise les proba pour que la somme soit bien 1
            proba = proba / sum_proba
        else:
            # Notre réseau n'a sortis aucun move valide. On met la même proba
            # Pour chaque move valide
            print("Aucun move valide trouvé")
            proba = proba + valid_moves

        self.Ps[state] = proba
        self.Ns[state] = 0

        return -V

    def _compute_upper_confidence(self, a_idx, s):

        if (s, a) in self.Qsa:
            u = self.Qsa[(s, a_idx)] + self.temp * self.Ps[s][a_idx] * \
                math.sqrt(self.Ns[s])/(1+self.Nsa[(s, a_idx)])
        else:
            # Q = 0 :
            u = self.args.cpuct*self.Ps[s][a]*math.sqrt(self.Ns[s] + self.EPS)

        return u

    def _update_node_info(self, s, a, child_v):
        '''
            Change the expected reward and the number of visit
            of the state 
        '''

        if (s, a) in self.Qsa:
            self.Qsa[(s, a)] = (self.Nsa[(s, a)] *
                                self.Qsa[(s, a)] + v)/(self.Nsa[(s, a)]+1)
            self.Nsa[(s, a)] += 1

        else:
            self.Qsa[(s, a)] = child_v
            self.Nsa[(s, a)] = 1
