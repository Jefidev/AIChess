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
