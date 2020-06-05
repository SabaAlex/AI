import System


class Controller:

    def __init__(self, temperature, humidity, time, rules):
        self.__system = System.FuzzySystem(rules)
        self.__system.addDescription('temperature', temperature)
        self.__system.addDescription('humidity', humidity)
        self.__system.addDescription('time', time, out=True)

    def compute(self, inputs):
        return "Hummidity: " + str(inputs['humidity']) + '\n' +\
               "Temperature: " + str(inputs['temperature']) + '\n' +\
               "Aprox operating time: " + str(self.__system.compute(inputs))
