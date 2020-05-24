import itertools

from domain.Genotype import Genotype


class HillClimbingAlgorithm:

    def __init__(self, n, iterations):
        self.__n = n
        self.__globalMax = n * n + n
        self.__iterations = iterations
        self.__individual = Genotype(n)
        self.__pastBestIndividuals = []
        self.__possiblePermutations = itertools.permutations([x for x in range(1, n + 1)])
        self.__iterationCounter = 1

    def getBestUntilNow(self):
        return self.__individual

    def getN(self):
        return self.__n

    def getIndividual(self):
        return self.__individual

    def __allIndividuals(self):
        individuals = [self.__individual]
        startingGenotype = self.__individual.getListOfPermutations()
        for permutation in self.__possiblePermutations:
            for i in range(2 * self.__n):
                newPerm = startingGenotype[:]
                newPerm[i] = permutation
                if newPerm not in individuals:
                    individuals.append(Genotype(self.__n, newPerm))
        return individuals

    def runAlgorithm(self):
        while self.__iterationCounter < self.__iterations:
            possibleIndividuals = self.__allIndividuals()

            bestIndividual = max(possibleIndividuals, key=lambda individual: individual.getFitness())
            if bestIndividual.getFitness() > self.__individual.getFitness():
                self.__pastBestIndividuals.append(self.__individual)
                self.__individual = bestIndividual

            if self.__individual.getFitness() == self.__globalMax:
                return self.__individual

            self.__iterationCounter += 1

        return self.__individual
