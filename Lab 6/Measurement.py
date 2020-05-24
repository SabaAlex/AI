class Measurement:
    def __init__(self, prediction, measurementList) -> None:
        self.__prediction = prediction
        self.__measurementList = measurementList

    def getPrediction(self):
        return self.__prediction

    def getMeasurements(self):
        return self.__measurementList

    def __str__(self) -> str:
        return str(self.__prediction + " " + str(self.__measurementList))

    def __repr__(self) -> str:
        return str(self.__prediction + " " + str(self.__measurementList))




