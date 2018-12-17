class EvaluationModel(object):
    '''
        Evaluation model must predict two metrics
        - Value : value of the current state of the board
        - Probabilities : Probabilities for each moves of the game
    '''

    def predict(self, state):
        NotImplemented
