import numpy
import random
import math
from copy import deepcopy
import operator


def sudokuCheckLine(line, n):
    return set(line) == set(numpy.arange(1, n + 1))


def sudokuCheckRow(row, n):
    return set(row) == set(numpy.arange(1, n + 1))


def sudokuCheckSquare(square, n):
    return set(square.flatten()) == set(numpy.arange(1, n + 1))


def sudokuCheckSquares(board, n):
    for i in range(int(math.sqrt(n))):
        for j in range(int(math.sqrt(n))):
            auxI = 0 + i * (int(math.sqrt(n)))
            auxJ = 0 + j * (int(math.sqrt(n)))
            if not sudokuCheckSquare(board[0 + auxI: 0 + auxI + int(math.sqrt(n)), 0 + auxJ: 0 + auxJ + int(math.sqrt(n))], n):
                return False
    return True


def sudokuCheckLinesAndRows(board, n):
    for i in range(n):
        if not (sudokuCheckLine(board[i], n) and sudokuCheckRow(board[:, i], n)):
            return False
    return True


def sudokuCheck(board, n):
    return sudokuCheckLinesAndRows(board, n) and sudokuCheckSquares(board, n)


def sudoku(attempts, n, sudokuBoard):

    for attempt in range(attempts):

        board = deepcopy(sudokuBoard)

        for i in range(n):
            for j in range(n):
                if board[i][j] == 0:
                    board[i][j] = random.SystemRandom().randint(1, n + 1)

        if sudokuCheck(board, n):
            print("Solution on the attempt with number: " + str(attempt + 1))
            print(board)
            return True


def sudokuUI(attempts):
    n = int(input("N: ").strip())

    board = numpy.empty((n, n))

    for i in range(n):
        print("Input line " + str(i + 1))
        line = input().strip()
        line = [int(x) for x in line]
        auxLine = numpy.array(line)
        board[i] = auxLine

    # board = numpy.array([[0, 1, 0, 3],
    #                      [4, 0, 0, 2],
    #                      [0, 2, 0, 0],
    #                      [3, 0, 2, 1]])

    print(board)

    if not sudoku(attempts, n, board):
        print("No solution found.")


def convertToNumber(hexa, letters):
    sum = 0
    for i in range(len(letters)):
        sum += hexa[letters[i]] * (16 ** (len(letters) - (i + 1)))
    return sum


def cryptarithmeticCheck(hexa, allLetters, op):
    if hexa[allLetters[0][0]] == 0 or hexa[allLetters[1][0]] == 0 or hexa[allLetters[2][0]] == 0:
        return False
    return op(convertToNumber(hexa, allLetters[0]), convertToNumber(hexa, allLetters[1])) == convertToNumber(hexa, allLetters[2])


def assignHexa(letterSet):
    letterDict = dict()
    for x in letterSet:
        letterDict[x] = random.randint(0, 15)
    return letterDict


def cryptarithmetic(attempts, allLetters, operation):
    lettersSet = deepcopy(allLetters[0])
    lettersSet.extend(allLetters[1])
    lettersSet.extend(allLetters[2])
    lettersSet = set(lettersSet)
    ops = {"+": operator.add, "-": operator.sub}

    for attempt in range(attempts):
        hexa = assignHexa(lettersSet)

        if cryptarithmeticCheck(hexa, allLetters, ops[operation]):
            print("Solution on the attempt with number: " + str(attempt + 1))
            print(hexa)
            return True


def cryptarithmeticUI(attempts):
    firstWord = input("Enter first word: ").strip()
    secondWord = input("Enter the second word: ").strip()
    operation = input("Enter operation: ").strip()
    solution = input("Enter solution: ").strip()
    allLetters = [list(firstWord), list(secondWord), list(solution)]
    if not cryptarithmetic(attempts, allLetters, operation):
        print("No solution found.")



def geoFormsCheck(board):
    return set(numpy.unique(board)) == {0, 1}


def geoForms(attempts, allForms):
    for attempt in range(attempts):
        board = numpy.zeros((5, 6))
        try:
            x = random.randrange(board.shape[0])
            y = random.randrange(board.shape[1])  # -3
            board[x, y: y + allForms[0].shape[0]] += allForms[0]
            for i in range(1, len(allForms)):
                x = random.randrange(board.shape[0])  # -1
                y = random.randrange(board.shape[1])  # -2
                board[x:x + allForms[i].shape[0], y:y + allForms[i].shape[1]] += allForms[1]
        except IndexError:
            continue
        except ValueError:
            continue

        if geoFormsCheck(board):
            print("Solution on the attempt with number: " + str(attempt + 1))
            print(board)
            return True

    return False


def geoFormsUI(attempts):
    firstForm = numpy.array([1, 1, 1, 1])
    secondForm = numpy.array([[1, 0, 1],
                              [1, 1, 1]])
    thirdForm = numpy.array([[1, 0, 0],
                             [1, 1, 1]])
    forthForm = numpy.array([[1, 1, 1],
                             [0, 0, 1]])
    fifthForm = numpy.array([[0, 1, 0],
                             [1, 1, 1]])
    allForms = [firstForm, secondForm, thirdForm, forthForm, fifthForm]
    if not geoForms(attempts, allForms):
        print("No solution found.")


def main():

    while True:
        try:
            print("Type 1 for Sudoku.")
            print("Type 2 for Cryptarithmetic.")
            print("Type 3 for Geometric forms.")

            selection = input(">>").strip()

            if selection == "exit":
                return

            selection = int(selection)

            attempts = int(input("Max nr of attempts: ").strip())

            if selection == 1:
                sudokuUI(attempts)
            elif selection == 2:
                cryptarithmeticUI(attempts)
            elif selection == 3:
                geoFormsUI(attempts)
            else:
                raise ValueError("No valid selection was made")
        except ValueError as e:
            print(e)


main()
