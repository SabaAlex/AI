import operator

from DTAlgorithm import DTAlgorithm
from Measurement import Measurement

if __name__ == '__main__':
    # dtAlg = DTAlgorithm("DECISION/balance-scale.data")
    # print(dtAlg.runAlgorithm())
    mean = []
    for i in range(1000):
        dtAlg = DTAlgorithm("DECISION/balance-scale.data")
        mean.append(dtAlg.runAlgorithm())
    print(sum(mean)/len(mean))