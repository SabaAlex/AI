class FuzzyDescriptions:

    def __init__(self):
        self.__regions = {}
        self.__inverse = {}

    def addRegion(self, varName, assignedFunction, inverse=None):
        self.__regions[varName] = assignedFunction
        self.__inverse[varName] = inverse

    def fuzzy(self, value):
        return {name: assignedFunction(value) for name, assignedFunction in self.__regions.items()}

    def defuzzy(self, varName, value):
        return self.__inverse[varName](value)
