import random

from domain.Genotype import Genotype
from domain.Population import Population
from exceptions.SampleTooBiglException import SampleTooBigException
from exceptions.SampleTooSmallException import SampleTooSmallException


class EvolutionaryAlgorithm:
    def __init__(self, n, generationsNR, mutationChance, populationSize, breedCuts, selectionSample=None):
        self.__n = n
        self.__mutationChance = float(mutationChance)
        self.__generationsNR = generationsNR
        self.__populationSize = populationSize
        self.__generations = [Population(n, populationSize)]
        self.__breedCuts = breedCuts
        self.__selectionSample = selectionSample
        self.__generationCounter = 1

    def getBestUntilNow(self):
        return self.getLastGeneration().getFittest()

    def __newGeneration(self, populationList=None):
        if populationList is not None:
            self.__generations.append(Population(self.__n, self.__populationSize, populationList))
        self.__generations.append(Population(self.__n, self.__populationSize, self.__generations[-1].getPopulation()))

    def __breed(self, firstIndividual, secondIndividual):
        firstPermList = firstIndividual.getListOfPermutations()
        secondPermList = secondIndividual.getListOfPermutations()

        son = []
        cuts = set([random.randint(0, 2 * self.__n) for i in range(self.__breedCuts)])

        currentPermList = firstPermList
        for i in range(2 * self.__n):
            if i in cuts:
                currentPermList = secondPermList if currentPermList is firstPermList else firstPermList
            son.append(currentPermList[i][:])

        return son

    def __chooseCrossoverStyle(self):
        if self.__selectionSample is None:
            return self.__crossoverRandom()
        else:
            return self.__crossoverTournament()

    def __crossoverRandom(self):
        # Random selection at the moment, will try other methods
        lastGeneration = self.__generations[-1]
        firstIndividual = random.choice(lastGeneration.getPopulation())
        secondIndividual = random.choice(lastGeneration.getPopulation())

        while firstIndividual == secondIndividual:
            secondIndividual = random.choice(lastGeneration.getPopulation())

        return self.__breed(firstIndividual, secondIndividual)

    def __crossoverTournament(self):
        if self.__selectionSample < 2:
            raise SampleTooSmallException()
        elif self.__selectionSample > self.__populationSize:
            raise SampleTooBigException()
        samplePopulationToReproduce = sorted(
            random.sample(self.__generations[-1].getPopulation(), self.__selectionSample),
            key=lambda individual: individual.getFitness())

        return self.__breed(samplePopulationToReproduce[0], samplePopulationToReproduce[1])

    def __mutate(self, individual):
        if self.__mutationChance > random.random():
            random.shuffle(random.choice(individual))
        return individual

    def __killLeastFit(self):
        lastGeneration = self.getLastGeneration().getPopulation()
        lastGeneration.remove(min(lastGeneration, key=lambda individ: individ.getFitness()))
        return lastGeneration

    def runAlgorithm(self):
        while self.__generationCounter < self.__generationsNR:
            newIndividual = Genotype(self.__n, self.__mutate(self.__chooseCrossoverStyle()))
            newGeneration = self.__killLeastFit()
            newGeneration.append(newIndividual)
            self.__newGeneration(newGeneration)
            if not len(self.getLastGeneration().getPopulation()) is self.__populationSize:
                raise Exception("WTF")
            self.__generationCounter += 1
        return self.getLastGeneration().getFittest()

    def getN(self):
        return self.__n

    def getGenerations(self):
        return self.__generations[:]

    def getLastGeneration(self):
        return self.__generations[-1]

    def __str__(self) -> str:
        return str(self.__generations)
