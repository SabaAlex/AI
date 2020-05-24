import operator
import random

from Measurement import Measurement
from Node import Node


class DTAlgorithm:
    def __init__(self, dataSetFile) -> None:
        self.__dataSet = self.__initDataSet(dataSetFile)
        self.__constructionSample = random.sample(self.__dataSet, len(self.__dataSet) // 2)
        self.__testSample = list(set(self.__dataSet) - set(self.__constructionSample))
        self.__giniValues = random.choices([1, 2, 3, 4, 5], k=4)
        self.__giniOutcome = [True, False]
        self.__atributeList = [0, 1, 2, 3]
        self.__classes = set(map(lambda measurement: measurement.getPrediction(),
                               self.__constructionSample))
        self.__attributeDictionary = {
            0: "left weight",
            1: "left distance",
            2: "right weight",
            3: "right distance"
        }

    @staticmethod
    def __initDataSet(dataSetFile):
        dataSet = []
        with open(dataSetFile) as openfileobject:
            for line in openfileobject:
                line = line[:-1]
                dataSet.append(Measurement(line[0],
                               [int(list(line[2:].split(","))[i]) for i in range(len(line.split(",")) - 1)]))
        return dataSet

    def __generateDT(self, dataPartition, attributeList):
        node = Node()

        attributeListFromDataSet = list(map(lambda measurement: measurement.getPrediction(), dataPartition))
        attributeDistribution = {i: attributeListFromDataSet.count(i) for i in set(attributeListFromDataSet)}

        if len(set(map(lambda measurement: measurement.getPrediction(), dataPartition))) == 1:
            node.setLeaf()
            node.setLabel(dataPartition[0].getPrediction())
            return node

        else:
            if not attributeList:
                node.setLeaf()
                node.setLabel(max(attributeDistribution.items(), key=lambda x: x[1])[0])
                return node

            else:
                separationAttribute = self.__AttributeSelection(dataPartition, attributeList)
                node.setLabel(self.__attributeDictionary[separationAttribute])

                for value in self.__giniOutcome:
                    newDataPartition = \
                        list(filter(lambda measurement:
                               (measurement.getMeasurements()[separationAttribute] >=
                                self.__giniValues[separationAttribute]) == value,
                               dataPartition))

                    if not newDataPartition:
                        newChild = Node()
                        newChild.setLeaf()
                        newChild.setLabel(max(attributeDistribution.items(), key=lambda x: x[1])[0])
                        node.addChild(newChild)
                        node.addValueBranch(value)

                    else:
                        node.addChild(self.__generateDT(newDataPartition,
                                                        list(set(attributeList) - {separationAttribute})))
                        node.addValueBranch(value)

                return node

    def getTree(self):
        return self.__generateDT(self.__constructionSample, self.__atributeList)

    def runAlgorithm(self):
        tree = self.__generateDT(self.__constructionSample, self.__atributeList)
        #print(tree)
        attributeListFromDataSet = list(map(lambda measurement: measurement.getPrediction(), self.__testSample))
        attributeDistribution = {i: attributeListFromDataSet.count(i) for i in set(attributeListFromDataSet)}
        #print(attributeDistribution)
        predictionCounter = 0
        for measurement in self.__testSample:
            auxTree = tree
            while not auxTree.isLeaf():
                label = auxTree.getLabel()
                attribute = list(self.__attributeDictionary.keys())[list(self.__attributeDictionary.values()).index(label)]
                auxTree = auxTree.getChildren()[0] if auxTree.returnBranchValues()[0] ==\
                                                      (measurement.getMeasurements()[attribute] >=
                                                       self.__giniValues[attribute]) else auxTree.getChildren()[1]
            if auxTree.getLabel() == measurement.getPrediction():
                predictionCounter += 1
        #print(predictionCounter)
        return predictionCounter/len(attributeListFromDataSet)

    def __AttributeSelection(self, dataPartition, attributeList):
        giniIndexes = dict()

        for attribute in attributeList:
            giniAuxiliary1 = 0
            giniAuxiliary2 = 0

            # More or equal than gini index value
            dataPartitionFiltered = list(filter(lambda measurement:
                                                 measurement.getMeasurements()[attribute] >=
                                                 self.__giniValues[attribute], dataPartition))
            if len(dataPartitionFiltered) is not 0:
                for classification in self.__classes:
                    dataPartitionedFilteredClass = list(filter(lambda measurement:
                                                               measurement.getPrediction() == classification
                                                               , dataPartitionFiltered))
                    giniAuxiliary1 += (len(dataPartitionedFilteredClass)/len(dataPartitionFiltered)) * \
                                      (len(dataPartitionedFilteredClass)/len(dataPartitionFiltered))

                giniAuxiliary1 = (1 - giniAuxiliary1) * ((len(dataPartitionFiltered) / len(dataPartition)))

            # Less then gini index value
            dataPartitionFiltered = list(filter(lambda measurement:
                                                 measurement.getMeasurements()[attribute] <
                                                 self.__giniValues[attribute], dataPartition))
            if len(dataPartitionFiltered) is not 0:
                for classification in self.__classes:
                    dataPartitionedFilteredClass = list(filter(lambda measurement:
                                                               measurement.getPrediction() == classification
                                                               , dataPartitionFiltered))
                    giniAuxiliary2 += (len(dataPartitionedFilteredClass) / len(dataPartitionFiltered)) ** 2

                giniAuxiliary2 = (1 - giniAuxiliary2) * (len(dataPartitionFiltered) / len(dataPartition))

            giniIndexes[attribute] = giniAuxiliary1 + giniAuxiliary2

        return min(giniIndexes.items(), key=lambda x: x[1])[0]
