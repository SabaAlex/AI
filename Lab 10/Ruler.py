class FuzzyRule:

    def __init__(self, inputs, output):
        self.__inputs = inputs
        self.__output = output

    def evaluate(self, inputs):
        return [self.__output, min([inputs[description][varName] for description, varName in self.__inputs.items()])]
