import numpy


class ANN:

    def __init__(self, x: numpy.array, y: numpy.array, learnRate: float, hiddenNr: int, aConst: float):
        self.__dataIn = x
        self.__weightsInToHide = numpy.random.rand(self.__dataIn.shape[1], hiddenNr)
        self.__weightsHideToOut = numpy.random.rand(hiddenNr, 1)
        self.__output_data = y
        self.__learnRate = learnRate
        self.__predictedOut = numpy.zeros(y.shape)
        self.__loss = []
        self.__aConst = aConst

    def __activationFunction(self, x):
        return self.__aConst * x

    def __dActivationFunction(self, x):
        return numpy.full_like(x, self.__aConst)

    def feedForward(self):
        self.__hiddenLayer = self.__activationFunction(numpy.dot(self.__dataIn, self.__weightsInToHide))

        self.__predictedOut = self.__activationFunction(numpy.dot(self.__hiddenLayer, self.__weightsHideToOut))

    def backProp(self):
        backWeightsHideToOut = numpy.dot(
            self.__hiddenLayer.T,
            (2 * (self.__output_data - self.__predictedOut) * self.__dActivationFunction(self.__predictedOut))
        )

        backWeightsInToHide = numpy.dot(
            self.__dataIn.T,
            (numpy.dot(
                2 * (self.__output_data - self.__predictedOut) * self.__dActivationFunction(self.__predictedOut),
                self.__weightsHideToOut.T) * self.__dActivationFunction(self.__hiddenLayer)
             )
        )

        self.__weightsInToHide += self.__learnRate * backWeightsInToHide
        self.__weightsHideToOut += self.__learnRate * backWeightsHideToOut

        self.__loss.append(sum((self.__output_data - self.__predictedOut) ** 2))

    def getOutput(self, data):
        hidden = self.__activationFunction(numpy.dot(data, self.__weightsInToHide))
        output = self.__activationFunction(numpy.dot(hidden, self.__weightsHideToOut))
        return output

    def getLoss(self):
        return self.__loss
