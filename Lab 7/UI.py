from domain.LinearRegression import LinearRegression


class UI:
    def __init__(self) -> None:
        super().__init__()

    def startUI(self):
        alg = LinearRegression("resources/data.data")
        finalValue = alg.runAlgorithm()
        print("Final mean value of the algorithm: " + str(finalValue))
        print("Mean of the dataSet value: " + str(alg.getMeanPred()))
        precision = abs(alg.getMeanPred() - finalValue)
        print("Error: " + str(precision))