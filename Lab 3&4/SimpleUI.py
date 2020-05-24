import math

from algorithm.EvolutionaryAlgorithm import EvolutionaryAlgorithm
from algorithm.HillClimbingAlgorithm import HillClimbingAlgorithm
from algorithm.PSOAlgorithm import PSOAlgorithm


class SimpleUI:
    def __init__(self):
        self.__statNREA = 30
        self.__statNRPSO = 2
        self.__statNRHill = 10

    def runUI(self):
        ok = False
        while not ok:
            print("Type 'Exit' to exit")
            algorithm = input("Enter Algorithm(EA, Hill, PSO): ")
            try:
                if algorithm == "EA":
                    self.runUIEA()
                elif algorithm == "Hill":
                    self.runUIHill()
                elif algorithm == "PSO":
                    self.runUIPSO()
                elif algorithm == "Exit":
                    ok = True
                else:
                    print("Try again")
            except TabError as e:
                print(str(e))

    def runUIPSO(self):
        self.statistics = [PSOAlgorithm(4, 100, 40, 10, 1.0, 2.5, 1.0) for x in range(self.__statNRPSO)]
        results = []
        for i in range(self.__statNRPSO):
            results += [self.computeStatistics(i)]
        mean = sum(results) / len(results)
        print("Mean :" + str(mean))
        print("Standard Deviation :" + str(math.sqrt(sum([(results[i] - mean) ** 2 for i in range(self.__statNRPSO)]) / self.__statNRPSO)))

        n = int(input("Enter N:"))
        iter = int(input("Nr of iterations/generations: "))
        if iter < 1:
            raise Exception("Enter a higher iteration number!")
        swarmsize = int(input("Swarm size: "))
        if swarmsize < 1:
            raise Exception("Enter a higher swarmSize number!")
        neighbours = int(input("Neighbourhoods Size"))
        if neighbours < 1:
            raise Exception("Enter a higher neighbourhood number!")
        if neighbours > swarmsize:
            raise Exception("Cannot have more neighbours than particles!")
        c1 = float(input("Cog Coeff: "))
        c2 = float(input("Social Coeff: "))
        w = float(input("Inertia: "))
        if c1 < 0:
            raise Exception("Cog Coeff is neg!")
        if c2 < 0:
            raise Exception("Social Coeff is neg!")
        if w < 0:
            raise Exception("Inertia is neg!")
        if c1 + c2 >= 4:
            raise Exception("Enter coeff which are lower")
        pso = PSOAlgorithm(n, iter, swarmsize, neighbours, c1, c2, w)
        fittest = pso.runAlgorithm()
        print(str(fittest))
        print("Fitness = " + str(fittest.getFitness()))

    def runUIHill(self):
        self.statistics = [HillClimbingAlgorithm(4, 250) for x in range(self.__statNRHill)]
        results = []
        for i in range(self.__statNRHill):
            results += [self.computeStatistics(i)]
        mean = sum(results) / len(results)
        print("Mean :" + str(mean))
        print("Standard Deviation :" + str(math.sqrt(sum([(results[i] - mean) ** 2 for i in range(self.__statNRHill)]) / self.__statNRHill)))

        n = int(input("Enter N:"))
        iter = int(input("Nr of iterations/generations: "))
        if iter < 1:
            raise Exception("Enter a higher iteration number!")
        hill = HillClimbingAlgorithm(n, iter)
        fittest = hill.runAlgorithm()
        print(str(fittest))
        print("Fitness = " + str(fittest.getBestFitness()))

    def computeStatistics(self, index):
        return self.statistics[index].runAlgorithm().getBestFitness()

    def runUIEA(self):
        self.statistics = [EvolutionaryAlgorithm(4, 500, 0.4, 40, 2) for x in range(self.__statNREA)]
        results = []
        for i in range(self.__statNREA):
            results += [self.computeStatistics(i)]
        mean = sum(results) / len(results)
        print("Mean :" + str(mean))
        print("Standard Deviation :" + str(math.sqrt(sum([(results[i] - mean) ** 2 for i in range(self.__statNREA)]) / self.__statNREA)))

        n = int(input("Enter N:"))
        iter = int(input("Nr of iterations/generations: "))
        if iter < 1:
            raise Exception("Enter a higher iteration number!")
        mut = float(input("Mutation Change(<= 1 and pozitive):"))
        if mut > 1.0:
            raise Exception("Mutation must be < =1 and pozitive")
        popsize = int(input("Population Size: "))
        if popsize < 1:
            raise Exception("Enter a higher popSize number!")
        breedcuts = int(input("Breed Cuts: "))
        if breedcuts < 1:
            raise Exception("Enter a higher breedCuts number!")
        if breedcuts >= n * 2:
            raise Exception("Enter a lower breedCuts number!")
        ea = EvolutionaryAlgorithm(n, iter, mut, popsize, breedcuts)
        fittest = ea.runAlgorithm()
        print(str(fittest))
        print("Fitness = " + str(fittest.getFitness()))