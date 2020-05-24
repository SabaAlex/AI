class Node:
    def __init__(self) -> None:
        self.__children = []
        self.__label = ""
        self.__isLeaf = False
        self.__branchesValues = []

    def addChild(self, child):
        self.__children.append(child)

    def getChildren(self):
        return self.__children

    def setLeaf(self):
        self.__isLeaf = True

    def addValueBranch(self, value):
        self.__branchesValues.append(value)

    def returnBranchValues(self):
        return self.__branchesValues

    def isLeaf(self):
        return self.__isLeaf

    def setLabel(self, label):
        self.__label = label

    def getLabel(self):
        return self.__label

    def __str__(self) -> str:
        return self.__label + " " + str(self.__children)

    def __repr__(self) -> str:
        return self.__label + " " + str(self.__children)






