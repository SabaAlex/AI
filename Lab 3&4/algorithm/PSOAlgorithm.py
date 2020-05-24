import random

import numpy

from domain.Swarm import Swarm


class PSOAlgorithm:
    def __init__(self, n, iterations, swarmSize, numberOfNeighbours, c1, c2, w) -> None:
        self.__n = n
        self.__iterations = iterations
        self.__iterationCounter = 1
        self.__globalMax = n * n + n
        self.__swarmSize = swarmSize
        self.__numberOfNeighbours = numberOfNeighbours
        self.__c1 = c1
        self.__c2 = c2
        self.__w = w
        self.__swarm = Swarm(n, swarmSize)
        self.__neighbours = self.__computeNeighbours()

    def getN(self):
        return self.__n

    def getSwarm(self):
        return self.__swarm

    def getBestUntilNow(self):
        self.__swarm.getFittest()

    def __computeNeighbours(self):
        neighbors = []

        for i in range(self.__swarmSize):
            localNeighbuor = []

            for j in range(self.__numberOfNeighbours):
                x = random.randint(0, self.__swarmSize - 1)
                while x in localNeighbuor:
                    x = random.randint(0, self.__swarmSize - 1)
                localNeighbuor.append(x)

            neighbors.append(localNeighbuor.copy())

        return neighbors

    @staticmethod
    def manhattenDistance(permutation, otherPermutation):
        return sum([abs(permutation[i] - otherPermutation[i]) for i in range(len(permutation))])

    @staticmethod
    def __sigmoid(power):
        return 1 / (1 + numpy.exp(-1*power))

    def runAlgorithm(self):
        while self.__iterationCounter < self.__iterations:

            bestNeighbors = []
            for i in range(self.__swarmSize):
                bestNeighbors.append(self.__neighbours[i][0])
                for j in range(1, self.__numberOfNeighbours):
                    if self.__swarm.getParticleAtIndex(bestNeighbors[i]).getFitness() <\
                            self.__swarm.getParticleAtIndex(self.__neighbours[i][j]).getFitness():
                        bestNeighbors[i] = self.__neighbours[i][j]

            for i in range(self.__swarmSize):
                particle = self.__swarm.getParticleAtIndex(i)
                velocity = particle.getVelocity()
                for j in range(2 * self.__n):
                    newVelocity = (self.__w / self.__iterationCounter) * velocity[j]
                    newVelocity = newVelocity + self.__c1 * random.random() * self.manhattenDistance(
                        self.__swarm.getParticleAtIndex(bestNeighbors[i]).getListOfPermutations()[j],
                        particle.getListOfPermutations()[j])
                    newVelocity = newVelocity + self.__c2 * random.random() * self.manhattenDistance(
                        particle.getBestListOfPermutations()[j], particle.getListOfPermutations()[j])
                    velocity[j] = newVelocity

            for i in range(self.__swarmSize):
                newListOfPermutations = list()
                particleAtIndex = self.__swarm.getParticleAtIndex(i)
                oldPermutations = particleAtIndex.getListOfPermutations()
                computedVelocity = particleAtIndex.getVelocity()
                bestNeighbourParticlePermutations = self.__swarm.getParticleAtIndex(bestNeighbors[i])\
                    .getListOfPermutations()
                for j in range(2 * self.__n):
                    rand = random.random()
                    calc = self.__sigmoid(computedVelocity[j])
                    if rand < calc:
                        newListOfPermutations = newListOfPermutations + [bestNeighbourParticlePermutations[j]]
                    else:
                        newListOfPermutations = newListOfPermutations + [oldPermutations[j]]
                self.__swarm.getParticleAtIndex(i).setListOfPermutations(newListOfPermutations)

            self.__iterationCounter += 1

        return self.__swarm.getFittest()