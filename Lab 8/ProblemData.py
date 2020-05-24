import numpy
import math
from copy import deepcopy


class ProblemData:

    def __init__(self, dataSetFile):
        self.__initDataSet(dataSetFile)
        self.__addBias()

    def getDataset(self):
        return self.__dataSet

    def __initDataSet(self, dataSetFile):
        dataSet = []

        with open(dataSetFile) as openfileobject:
            for line in openfileobject:
                if line is '\n':
                    continue
                line = line.strip().split(" ")
                elements = [float(element) for element in line]
                dataSet.append(elements)

        numpy.random.shuffle(dataSet)
        self.__dataSet = dataSet

    def __addBias(self):
        bias = 1.
        dataSet = []

        for data in self.__dataSet:
            newData = [bias]
            [newData.append(x) for x in data]
            dataSet.append(newData)

        self.__dataSet = dataSet


    @staticmethod
    def __separateData(dataSet):
        yVal = []
        numpy.random.shuffle(dataSet)

        for index in range(len(dataSet)):
            yVal.append([dataSet[index].pop()])

        xVal = numpy.array(dataSet)
        yVal = numpy.array(yVal)

        return xVal, yVal

    def splitData(self):
        trainData = self.__dataSet[:math.floor(len(self.__dataSet) * 0.75)]
        testData = self.__dataSet[math.floor(len(self.__dataSet) * 0.25):]

        trainX, trainY = self.__separateData(deepcopy(trainData))
        testX, testY = self.__separateData(testData)

        return trainX, trainY, testX, testY
