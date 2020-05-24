import math

import numpy

from domain.ProblemData import ProblemData


class LinearRegression:
    def __init__(self, dataSetFile) -> None:
        self.__dataSet, self.__means = self.__initDataSet(dataSetFile)
        self.__dataSetAttributesMatrix = [self.__dataSet[i].getAttributeList() for i in range(len(self.__dataSet))]
        self.__dataSetPredictionList = [self.__dataSet[i].getCorrespondingValue() for i in range(len(self.__dataSet))]
        self.__deviations = [math.sqrt(sum([(self.__dataSetAttributesMatrix[j][i] - self.__means[i]) ** 2
                                            for j in range(len(self.__dataSetAttributesMatrix))])
                                       / len(self.__dataSetAttributesMatrix)) for i in range(len(self.__means))]

    def normalizeData(self):
        attrSize = len(self.__dataSetAttributesMatrix[0])
        predMean = sum([self.getDataSet()[i].getCorrespondingValue() for i in range(len(self.getDataSet()))]) / len(
            self.getDataSet())
        predStd = math.sqrt(sum([(pred - predMean) ** 2 for pred in self.__dataSetPredictionList])
                            / len(self.__dataSetPredictionList))
        self.__dataSetAttributesMatrix = [[(self.__dataSetAttributesMatrix[i][j] - self.__means[j]) / self.__deviations[j]
                                           for j in range(attrSize)]
                                          for i in range(len(self.__dataSetAttributesMatrix))]

    def getMeanPred(self):
        return sum(self.__dataSetPredictionList) / len(self.__dataSetPredictionList)

    def getDataSet(self):
        return self.__dataSet

    def predIDK(self):
        return self.__dataSetPredictionList

    def getMeans(self):
        return self.__means

    def runAlgorithm(self):
        self.normalizeData()
        X = numpy.array(self.__dataSetAttributesMatrix)
        ones = numpy.ones([X.shape[0], 1])
        X = numpy.concatenate((ones, X), axis=1)
        y = numpy.array([self.__dataSet[i].getCorrespondingValue() for i in range(len(self.__dataSet))])
        y = y.reshape(-1, 1)
        theta = numpy.zeros([1, 6])
        alpha = 0.00378
        iters = 1000

        finalTheta, values = self.gradientDescent(X, y, theta, iters, alpha)
        print(finalTheta)
        return values[-1]

    def gradientDescent(self, X, y, theta, iters, alpha):
        value = numpy.zeros(iters)
        for i in range(iters):
            theta = theta - (alpha / len(X)) * numpy.sum(X * (X @ theta.T - y), axis=0)
            value[i] = self.computeCost(X, y, theta)
        return theta, value

    @staticmethod
    def computeCost(X, y, theta):
        toBeSummed = numpy.power(((X @ theta.T) - y), 2)
        return numpy.sum(toBeSummed) / (len(X))

    @staticmethod
    def __initDataSet(dataSetFile):
        dataSet = []
        means = [0, 0, 0, 0, 0]
        with open(dataSetFile) as openfileobject:
            for line in openfileobject:
                if line is '\n':
                    continue
                line = line.split(" ")
                forMean = [float(element) for element in line[:-1]]
                dataSet.append(ProblemData(float(line[-1]), forMean))
                means = [(means[i] + forMean[i]) for i in range(len(means))]

        means = [summation/len(dataSet) for summation in means]
        return dataSet, means
