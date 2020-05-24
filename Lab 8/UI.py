from copy import deepcopy
from ANN import ANN
from ProblemData import ProblemData
import matplotlib.pyplot


class UI:
    def __init__(self) -> None:
        super().__init__()

    def __preloaded(self):
        self.__process(100, 0.000001, 4, 0.5)

    def run(self):
        print("Choose a parameter input style:")
        print("1. PreLoaded")
        print("2. User Input")
        print("0. Exit program")
        while True:
            try:
                option = int(input(">> ").strip())
                if option is 1:
                    self.__preloaded()
                elif option is 2:
                    self.__userInput()
                elif option is 0:
                    return
            except ValueError:
                print("An option was not chosen correctly! Try again")

    def __userInput(self):
        while True:
            try:
                nrOfIterations = int(input("Enter the Number of Iterations: ").strip())
                learningRate = float(input("Enter the learning rate: ").strip())
                hiddenNeuronsNumber = int(input("Enter the hidden neurons number: ").strip())
                aConst = float(input("Enter the constant for the sigmoid and dsigmoid functions: ").strip())
                self.__process(nrOfIterations, learningRate, hiddenNeuronsNumber, aConst)
                return
            except ValueError:
                print("Not the right input!")

    @staticmethod
    def __process(nrOfIterations, learningRate, hiddenNeuronsNumber, aConst):
        dataset = ProblemData("resources/data.data")
        trainX, trainY, testX, testY = dataset.splitData()

        neuralNetwork = ANN(deepcopy(trainX), deepcopy(trainY), learningRate, hiddenNeuronsNumber, aConst)

        iterations = []
        for i in range(nrOfIterations):
            neuralNetwork.feedForward()
            neuralNetwork.backProp()
            iterations.append(i)

        for i in range(len(testX)):
            predictedOut = neuralNetwork.getOutput(testX[i])
            print("Predicted output: {0}\nReal value: {1}".format(predictedOut, testY[i]))

        matplotlib.pyplot.plot(iterations, neuralNetwork.getLoss(), label='loss value vs iteration')
        matplotlib.pyplot.xlabel('Iterations')
        matplotlib.pyplot.ylabel('Loss function')
        matplotlib.pyplot.legend()
        matplotlib.pyplot.show()

