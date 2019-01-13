import numpy as np

listPieceJ1 = ['n', 'b', 'q', 'k', 'r', 'p']
listPieceJ2 = ['N', 'B', 'Q', 'K', 'R', 'P']

typePiece = {
    'n': 1,
    'b': 2,
    'q': 3,
    'k': 4,
    'r': 5,
    'p': 6,
}


def caseVecToName(vec):
    indexBefore = np.argmax(vec)

    axeX = indexBefore % 8
    axeX = (chr(97+axeX))
    axeY = indexBefore // 8 + 1
    result = axeX+str(axeY)

    return result


def convertCaseNameToId(name):
    axeX = ord(name[0]) - 97
    axeY = int(name[1]) - 1
    return axeX + axeY*8


def convertMove(before, after):
    return caseVecToName(before) + caseVecToName(after)


def convertBoardState(board):
    stateBoard = np.zeros(8*8, dtype=int)
    x = board.fen().split(" ")[0].split("/")
    axeY = 0
    for line in x:
        axeX = 0
        for p in line:
            if (p in (listPieceJ1)):
                stateBoard[createIndex(axeX, axeY)] = typePiece[p]
                axeX = axeX + 1
            else:
                if(p in (listPieceJ2)):
                    stateBoard[createIndex(axeX, axeY)] = -typePiece[p.lower()]
                    axeX = axeX + 1
                else:
                    axeX = axeX + int(p)
        axeY = axeY + 1

    return stateBoard


def createIndex(x, y):
    return x + y * 8

# 18 matrice de 8*8


def convertBoardStateToInputModel(vector, player, castling, nb_moves):
    vec_player_turn = np.full((1, 8, 8), player)

    player_down = np.zeros((6, 8*8))
    player_up = np.zeros((6, 8*8))

    for i in range(0, len(vector)):
        if (vector[i] > 0):
            player_down[vector[i]-1][i] = 1
        if (vector[i] < 0):
            player_up[-(vector[i]+1)][i] = 1

    player_down = player_down.reshape((6, 8, 8))
    player_up = player_up.reshape((6, 8, 8))

    result = np.append(vec_player_turn, player_down, axis=0)
    result = np.append(result, player_up, axis=0)

    vec_castling = np.zeros((4, 8, 8))
    for i in range(0, 4):
        vec_castling[i] = np.full((8, 8), castling[i])

    result = np.append(result, vec_castling, axis=0)

    vec_nb_moves = np.full((1, 8, 8), nb_moves)
    result = np.append(result, vec_nb_moves, axis=0)

    return result

# return castling = [haut-gauche,haut-droite,bas-gauche,bas-droite]


def get_castling_state(state_vec, board):
    castling = np.zeros(4)
    board_8_8 = np.array(state_vec).reshape((8, 8))

    if((sum(board_8_8[0][1:4]) == 0) and board.has_queenside_castling_rights(True)):
        castling[0] = 1

    if((sum(board_8_8[0][5:7]) == 0) and board.has_kingside_castling_rights(True)):
        castling[1] = 1

    if((sum(board_8_8[7][1:4]) == 0) and board.has_queenside_castling_rights(False)):
        castling[2] = 1

    if((sum(board_8_8[7][5:7]) == 0) and board.has_kingside_castling_rights(False)):
        castling[3] = 1

    return castling


def IsGameOver(player, state):
    '''
        Recupere un joueur (0 ou 1). Renvoie 
            0 si la partie est toujours en cours,
            1 si la partie est gagnée pour le jour
            -1 si la partie est perdue.
    '''

    raise NotImplemented


def neural_output_to_move(move_nbr):
    NotImplemented
