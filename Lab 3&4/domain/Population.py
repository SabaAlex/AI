from domain.Genotype import Genotype
from exceptions.PopulationTooBigException import PopulationTooBigException


class Population:
    def __init__(self, n, populationSize, population=None):
        self.__n = n
        self.__populationSize = populationSize
        if population is None:
            self.__initPopulation()
        else:
            self.__population = population[:]

    def getMeanFitness(self):
        return sum(map(lambda individual: individual.getFitness(), self.__population)) / self.__populationSize

    def __initPopulation(self):
        self.__population = [Genotype(self.__n) for x in range(self.__populationSize)]

    def getPopulation(self):
        return self.__population[:]

    def getFittest(self):
        return max(self.__population, key=lambda individ: individ.getFitness())

    def addIndividual(self, individual):
        if len(self.__population) < self.__populationSize:
            self.__population.append(individual)
        else:
            raise PopulationTooBigException("Cannot insert a new member in a population at the max size")

    def removeIndividual(self, individual):
        self.__population.remove(individual)

    def __str__(self) -> str:
        separator = '\n '
        return separator.join([str(x) for x in self.__population])

    def __repr__(self) -> str:
        separator = '\n '
        return separator.join([str(x) for x in self.__population])


