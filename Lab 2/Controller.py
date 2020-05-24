class Controller:

    def __init__(self, problem):
        self.__problem = problem

    def BestFS(self):
        visited = []
        q = [self.__problem.getRoot()]

        while len(q) > 0:
            currentState = q.pop(0)

            lastConfig = currentState.getValues()[-1]

            if lastConfig.getSize() == lastConfig.getNrOfValues():
                if self.__problem.isFinal(lastConfig):
                    return currentState.getValues()

            if lastConfig.getNrOfValues() < lastConfig.getSize():
                keySet = set(lastConfig.getValues().keys())

                if (not keySet in visited) and self.__problem.heuristic(lastConfig):
                    q = q + self.__problem.expand(currentState)
                    visited.append(keySet)

    def BFS(self):

        sol = []

        q = [self.__problem.getRoot()]

        while len(q) > 0:
            currentState = q.pop(0)
            currentConfig = currentState.getValues()[-1]

            if self.__problem.isFinal(currentConfig):
                if currentConfig not in sol:
                    sol.append(currentConfig)

            if currentConfig.getNrOfValues() < currentConfig.getSize():
                q = q + self.__problem.expand(currentState)

        return sol
