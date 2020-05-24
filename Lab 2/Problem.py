from State import State


class Problem:

    def __init__(self, iniC):
        self.__iniC = iniC
        self.__iniState = State()
        self.__iniState.setValues([self.__iniC])


    def expand(self, currentState):
        myList = []
        currentConfig = currentState.getValues()[-1]

        for x in currentConfig.nextConfig():
            myList.append(currentState + x)

        return myList

    def heuristic(self, configuration):
        rowIndexSet = set()
        colIndexSet = set()
        diagDiffSet = set()

        for key in list(configuration.getValues().keys()):
            rowIndexSet.add(key[0])
            colIndexSet.add(key[1])
            diagDiffSet.add(key[0] - key[1])

        return len(rowIndexSet) == len(colIndexSet) == len(diagDiffSet) == configuration.getNrOfValues()

    def getRoot(self):
        return self.__iniState

    def isFinal(self, configuration):
        n = configuration.getSize()

        sumCol = [0] * n
        sumRow = [0] * n

        for i in range(n):
            for j in range(n):
                if configuration.exists(i, j):
                    sumCol[j] += configuration.getValue(i, j)
                    sumRow[i] += configuration.getValue(i, j)

        if not (all(valCol == 1 for valCol in sumCol) and all(valRow == 1 for valRow in sumRow)):
            return False

        keyList = list(configuration.getValues().keys())

        for key1 in range(len(keyList) - 1):
            for key2 in range(key1 + 1, len(keyList)):
                if abs(keyList[key1][0] - keyList[key2][0]) - abs(keyList[key1][1] - keyList[key2][1]) == 0:
                    return False

        return True
