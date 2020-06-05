class FuzzySystem:

    def __init__(self, rules):
        self.__inDescriptions = {}
        self.__outDescription = None
        self.__rules = rules

    def addDescription(self, name, description, out=False):
        if out:
            self.__outDescription = description
        else:
            self.__inDescriptions[name] = description

    def compute(self, inputs):
        fuzzy = self.__computeDescriptions(inputs)
        rule = self.__computeRulesFuzzy(fuzzy)

        fuzzyOut = [(list(description[0].values())[0], description[1]) for description in rule]

        weightedTotal = 0
        weightSum = 0
        for var in fuzzyOut:
            weightSum += var[1]
            weightedTotal += self.__outDescription.defuzzy(*var) * var[1]

        return weightedTotal / weightSum

    def __computeDescriptions(self, inputs):
        return {
            var: self.__inDescriptions[var].fuzzy(inputs[var])
            for var, val in inputs.items()
        }

    def __computeRulesFuzzy(self, fuzzyVals):
        return [rule.evaluate(fuzzyVals) for rule in self.__rules
                if rule.evaluate(fuzzyVals)[1] != 0]
