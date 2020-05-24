import random


class PermutationGraph:
    def __init__(self, n):
        self.__n = n
        self.__allNodes = [x for x in range(self.__n)]
        self.__permutations()

    def __permutations(self):
        self.__permutation = []
        self.__permutation.append(random.randrange(0, self.__n))

    def getPermutation(self):
        return self.__permutation

    def __nextMoves(self):
        return list(set(self.__allNodes) - set(self.__permutation))

    #No costs for path so all the distances between the nodes are 1
    @staticmethod
    def __distMove():
        return 1

    def addMove(self, q0, trace, permIndex, alpha, beta):
        p = [0 for i in range(self.__n)]
        nextSteps = self.__nextMoves()

        if len(nextSteps) == 0:
            return False

        for i in nextSteps:
            p[i] = self.__distMove()

        p = [(p[i] ** beta) * (trace[permIndex][self.__permutation[-1]][i] ** alpha) for i in range(len(p))]
        if random.random() < q0:
            p = [[i, p[i]] for i in range(len(p))]
            p = max(p, key=lambda a: a[1])
            self.__permutation.append(p[0])
        else:

            s = sum(p)
            if s == 0:
                return random.choice(nextSteps)
            p = [p[i] / s for i in range(len(p))]
            p = [sum(p[0:i + 1]) for i in range(len(p))]
            r = random.random()
            i = 0
            while r > p[i]:
                i = i + 1
            self.__permutation.append(i)

        return True
