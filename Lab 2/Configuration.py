class Configuration:

    def __init__(self, dictionary, size):
        self.__board = dict(dictionary)
        self.__size = size

    def getSize(self):
        return self.__size

    def exists(self, x, y):
        return (x, y) in self.__board

    def getValue(self, x, y):
        return self.__board[(x, y)]

    def getNrOfValues(self):
        return len(self.__board)

    def getValues(self):
        return self.__board

    def nextConfig(self):
        nextC = []

        for i in range(self.__size):
            for j in range(self.__size):
                aux = dict(self.__board)
                if not (i, j) in aux:
                    aux[(i, j)] = 1
                    nextC.append(Configuration(aux, self.__size))

        return nextC

    def __str__(self):
        return str(self.__board)

    def __eq__(self, other):
        if not isinstance(other, Configuration):
            return False
        if self.__size != other.getSize():
            return False

        return self.__board == other.getValues()
