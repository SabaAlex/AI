import math

from algorithm.ACOAlgorithm import ACOAlgorithm
import matplotlib.pyplot as plt

class ACOUI:
    def __init__(self):
        self.__statNRACO = 30

    def runUI(self):
        ok = False
        while not ok:
            print("Type 'Exit' to exit")
            algorithm = input("Enter Algorithm(ACO): ")
            try:
                if algorithm == "ACO":
                    self.__runUIACO()
                elif algorithm == "Exit":
                    ok = True
                else:
                    print("Try again")
            except TabError as e:
                print(str(e))

    def computeStatistics(self, index):
        return self.__statistics[index].runAlgorithm().getMinFitness() - 1

    def __runUIACO(self):
        statN = 4
        print("For n={0}, noEras=1000, eraSize=4, q0=0.5, alpha=1.5, beta=0.9, rho=0.05, run 30 times.".format(statN))
        self.__statistics = \
            [ACOAlgorithm(n=statN, noEras=1000, eraSize=4, q0=0.5,
                trace=[[[1 for k in range(statN)] for j in range(statN)] for i in range(2 * statN)],
                alpha=1.5, beta=0.9, rho=0.05)
                for x in range(self.__statNRACO)]
        #q0 = exploration coeff
        #rho = degradation coeff
        #alpha = trail importance coeff
        #beta = visibility importance
        results = []
        for i in range(self.__statNRACO):
            results += [self.computeStatistics(i)]

        plt.plot(results)
        plt.axis([0, len(results), 0, max(results) + max(results) / 4])
        plt.ylabel("Fitness")
        plt.xlabel("Run")
        plt.show()

        mean = sum(results) / len(results)
        print("Mean :" + str(mean))
        print("Standard Deviation :" +
              str(math.sqrt(sum([(results[i] - mean) ** 2 for i in range(self.__statNRACO)]) / self.__statNRACO)))

        n = int(input("Enter N: "))

        noEras = int(input("Nr of eras: "))

        if noEras < 1:
            raise Exception("Enter a higher iteration number!")

        eraSize = int(input("Era size: "))
        if eraSize < 1:
            raise Exception("Enter a higher swarmSize number!")

        q0 = float(input("Exploration Coeff(q0): "))
        if q0 < 0:
            raise Exception("Enter a higher Exploration Coeff!")
        if q0 > 1:
            raise Exception("Exploration Coeff is <= 1!")

        rho = float(input("Degradation coeff(rho): "))
        alpha = float(input("Trail importance coeff(aplha): "))
        beta = float(input("Visibility importance(beta): "))
        if rho < 0:
            raise Exception("Degradation coeff is neg!")
        if alpha < 0:
            raise Exception("Trail importance coeff is neg!")
        if beta < 0:
            raise Exception("Visibility importance is neg!")

        trace = [[[1 for k in range(n)] for j in range(n)] for i in range(2 * n)]

        pso = ACOAlgorithm(n=n, noEras=noEras, eraSize=eraSize, q0=q0, alpha=alpha, beta=beta, rho=rho,
                           trace=trace)

        fittest = pso.runAlgorithm()
        print(str(fittest))
        print("Fitness = " + str(fittest.getMinFitness() - 1))