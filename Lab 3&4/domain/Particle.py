import random


class Particle:
    def __init__(self, n, listOfPermutations=None):
        self.__n = n
        if listOfPermutations is None:
            self.__permutations()
        else:
            self.__listOfPermutations = [x[:] for x in listOfPermutations]
        self.__velocity = [0 for j in range(2 * n)]
        self.__fitness = self.__fitnessComputation()
        self.__bestFitness = self.__fitness
        self.__bestListOfPermutations = self.__listOfPermutations.copy()

    def getListOfBestPermutations(self):
        return self.__bestListOfPermutations[:]

    def getBestFitness(self):
        return self.__bestFitness

    def getVelocity(self):
        return self.__velocity

    def getIndexedVelocity(self, i, j):
        return self.__velocity[i][j]

    def __evaluate(self):
        self._fitness = self.__fitnessComputation()

    def setListOfPermutations(self, newListOfPermutations):
        self.__listOfPermutations = newListOfPermutations.copy()
        self.__evaluate()
        if self._fitness > self.__bestFitness:
            self.__bestListOfPermutations = self.__listOfPermutations
            self.__bestFitness = self._fitness

    def getFitness(self):
        return self.__fitness

    def __fitnessComputation(self):
        colFitness = []
        individualFitness = set()

        for j in range(self.__n):
            colFitness.append([self.__listOfPermutations[i][j] for i in range(self.__n)])
            colFitness.append([self.__listOfPermutations[i + self.__n][j] for i in range(self.__n)])
            for i in range(self.__n):
                individualFitness.add((self.__listOfPermutations[j][i], self.__listOfPermutations[j + self.__n][i]))

        return len(individualFitness) + \
               sum(map(lambda colPermutation: len(set(colPermutation)) == self.__n, colFitness))

    def __permutations(self):
        myPermutation = [x for x in range(1, self.__n + 1)]
        self.__listOfPermutations = []
        for j in range(2 * self.__n):
            random.shuffle(myPermutation)
            self.__listOfPermutations.append(myPermutation[:])

    def getBestListOfPermutations(self):
        return self.__bestListOfPermutations[:]

    def getListOfPermutations(self):
        return self.__listOfPermutations[:]

    def __str__(self):
        tupleList = [[(self.__bestListOfPermutations[j][i], self.__bestListOfPermutations[j + self.__n][i]) for i in range(self.__n)] for j in range(self.__n)]
        resultString = '\n'
        for j in range(self.__n):
            resultString += ' '.join([str(tupleList[j][i]) for i in range(self.__n)]) + '\n'
        return resultString

    def __eq__(self, other) -> bool:
        if type(other) is list:
            return other == self.__listOfPermutations
        return other.getListOfPermutations() == self.__listOfPermutations

    def __repr__(self) -> str:
        return str(self.__bestListOfPermutations)


