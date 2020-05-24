from domain.Ant import Ant


class ACOAlgorithm:
    def __init__(self, n, noEras, eraSize, q0, trace, alpha, beta, rho):
        self.__alpha = alpha
        self.__rho = rho
        self.__q0 = q0
        self.__noEras = noEras
        # trace matrix, [x][y][z], x = 2 * n, y = n, z = n
        # x = index of the permutation, y = current permutation element, y = next permutation element
        self.__trace = trace
        self.__beta = beta
        self.__n = n
        self.__eraSize = eraSize

    def __iteration(self):
        self.__initPopulation()
        for ant in self.__colony:
            ant.addToEachGraph(self.__q0, self.__trace, self.__alpha, self.__beta)

        dTrace = [1.0 / self.__colony[i].getMinFitness() for i in range(self.__eraSize)]

        for i in range(2 * self.__n):
            for j in range(self.__n):
                for k in range(self.__n):
                    self.__trace[i][j][k] = (1 - self.__rho) * self.__trace[i][j][k]

        for i in range(self.__eraSize):
            for j in range(self.__n * 2):
                for k in range(self.__n - 1):
                    x = self.__colony[i].getListOfPermutations()[j].getPermutation()[k]
                    y = self.__colony[i].getListOfPermutations()[j].getPermutation()[k + 1]
                    self.__trace[j][x][y] = self.__trace[j][x][y] + dTrace[i]

        return self.getFittest()

    def runAlgorithm(self):
        best = self.__iteration()
        for i in range(self.__noEras - 1):
            sol = self.__iteration()
            if sol.getMinFitness() < best.getMinFitness():
                best = sol
        return best

    def __initPopulation(self):
        self.__colony = [Ant(self.__n, x) for x in range(self.__eraSize)]

    def getFittest(self):
        return max(self.__colony, key=lambda ant: ant.getFitness())

    def __str__(self) -> str:
        separator = '\n '
        return separator.join([str(x) for x in self.__colony])

    def __repr__(self) -> str:
        separator = '\n '
        return separator.join([str(x) for x in self.__colony])