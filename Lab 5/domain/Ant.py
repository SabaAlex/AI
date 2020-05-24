from domain.PermutationGraph import PermutationGraph


class Ant:
    def __init__(self, n, antIndex):
        self.__n = n
        self.__allNodes = [x for x in range(1, self.__n + 1)]
        self.__permutations()
        self.__fitness = 0
        self.__maxFitness = n * n + 2 * n
        self.__antIndex = antIndex

    def getAntIndex(self):
        return self.__antIndex

    def getFitness(self):
        return self.__fitnessComputation()

    def getMinFitness(self):
        return self.__maxFitness - self.__fitnessComputation() + 1

    def addToEachGraph(self, q0, trace, alpha, beta):
        for i in range(0, self.__n * 2):
            notFinished = True
            while notFinished:
                notFinished = self.__listOfPermutations[i].addMove(q0, trace, i, alpha, beta)

    def __permutations(self):
        self.__listOfPermutations = []
        for i in range(self.__n * 2):
            self.__listOfPermutations.append(PermutationGraph(self.__n))

    def getListOfPermutations(self):
        return self.__listOfPermutations

    def __fitnessComputation(self):
        colFitness = []
        individualFitness = set()

        for j in range(self.__n):
            colFitness.append([self.__listOfPermutations[i].getPermutation()[j] for i in range(self.__n)])
            colFitness.append([self.__listOfPermutations[i + self.__n].getPermutation()[j] for i in range(self.__n)])
            for i in range(self.__n):
                individualFitness.add((self.__listOfPermutations[j].getPermutation()[i],
                                       self.__listOfPermutations[j + self.__n].getPermutation()[i]))

        return len(individualFitness) + \
               sum(map(lambda colPermutation: len(set(colPermutation)) == self.__n, colFitness))

    def __str__(self):
        tupleList = [[(self.__listOfPermutations[j].getPermutation()[i]  + 1,
                       self.__listOfPermutations[j + self.__n].getPermutation()[i]  + 1)
                      for i in range(self.__n)] for j in range(self.__n)]

        resultString = '\n'
        for j in range(self.__n):
            resultString += ' '.join([str(tupleList[j][i]) for i in range(self.__n)]) + '\n'
        return resultString

    def __eq__(self, other) -> bool:
        if type(other) is list:
            return other == self.__listOfPermutations
        return other.getListOfPermutations() == self.__listOfPermutations

    def __repr__(self) -> str:
        return str(self.__listOfPermutations)
