from timeit import default_timer as timer
from Controller import Controller
from Problem import Problem
from Configuration import Configuration


class UI:

    def __init__(self):
        self.__iniC = Configuration(dict(), 4)
        self.__p = Problem(self.__iniC)
        self.__ctrl = Controller(self.__p)

    def __mainMenu(self):
        s = ''
        s += "The empty board is the default initial config.\n"
        s += "0 - exit \n"
        s += "1 - Configure board size \n"
        s += "2 - Find a path with BFS \n"
        s += "3 - Find a path with BestFS\n"
        print(s)

    def __readConfigSubMenu(self):

        n = 4

        try:
            print("NxN board (implicit n=4)")
            n = int(input("n = "))
        except:
            print("invalid number, the implicit value is still 4")
            n = 4

        self.__iniC = Configuration(dict(), n)
        self.__p = Problem(self.__iniC)
        self.__ctrl = Controller(self.__p)

    def __printBoard(self, keyList):
        board = [[0 for x in range(len(keyList))] for y in range(len(keyList))]

        for key in keyList.keys():
            board[key[0]][key[1]] = 1

        formatString = '{:' + str(len(keyList)) + '}'

        print('\n'.join([''.join([formatString.format(item) for item in row])
                         for row in board]))

    def __findPathBFS(self):

        startClock = timer()

        try:
            boards = self.__ctrl.BFS()
        except TypeError:
            print("No solution")
            pass

        endClock = timer()
        print('Number of solutions: ' + str(len(boards)))
        count = 1
        for board in boards:
            print("Sol Nr. " + str(count))
            count += 1
            self.__printBoard(board.getValues())
            print('-------------------')
        print('execution time = ', endClock - startClock, " seconds")

    def __findPathBestFS(self):

        startClock = timer()

        try:
            board = self.__ctrl.BestFS()[-1]
        except TypeError:
            print("No solution")
            pass

        endClock = timer()
        self.__printBoard(board.getValues())
        print('execution time = ', endClock - startClock, " seconds")

    def run(self):

        exit = True
        self.__mainMenu()

        while exit:
            try:
                command = int(input(">>"))
                if command == 0:
                    exit = False
                elif command == 1:
                    self.__readConfigSubMenu()
                elif command == 2:
                    self.__findPathBFS()
                elif command == 3:
                    self.__findPathBestFS()
            except:
                print("Try Again!")

