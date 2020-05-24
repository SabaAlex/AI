class ProblemData:
    def __init__(self, correspondingValue, attributeList) -> None:
        self.__correspondingValue = correspondingValue
        self.__attributeList = attributeList

    def getCorrespondingValue(self):
        return self.__correspondingValue

    def getAttributeList(self):
        return self.__attributeList
