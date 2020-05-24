from domain.Particle import Particle


class Swarm:
    def __init__(self, n, swarmSize, swarm=None):
        self.__n = n
        self.__swarmSize = swarmSize
        if swarm is None:
            self.__initPopulation()
        else:
            self.__population = swarm[:]

    def getMeanFitness(self):
        return sum(map(lambda particle: particle.getBestFitness(), self.__population)) / self.__swarmSize

    def getParticleAtIndex(self, index) -> Particle:
        return self.__population[index]

    def __initPopulation(self):
        self.__population = [Particle(self.__n) for x in range(self.__swarmSize)]

    def getPopulation(self):
        return self.__population[:]

    def getFittest(self):
        return max(self.__population, key=lambda particle: particle.getBestFitness())

    def __str__(self) -> str:
        separator = '\n '
        return separator.join([str(x) for x in self.__population])

    def __repr__(self) -> str:
        separator = '\n '
        return separator.join([str(x) for x in self.__population])


