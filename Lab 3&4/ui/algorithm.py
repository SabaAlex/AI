import math
import multiprocessing
import threading
from multiprocessing.pool import ThreadPool

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Algorithm(QtWidgets.QDialog):
    def __init__(self, algorithm, statistics, statsNR):
        super().__init__()
        self.setupUi()
        self.setModal(True)
        self.algorithm = algorithm
        self.statistics = statistics
        self.statsNR = statsNR
        statThread = threading.Thread(target=self.loadStatistics)
        statThread.setDaemon(True)
        statThread.start()

    def loadStatistics(self):
        standardDeviation, meanFitness = self.runStatistics()
        self.labelFit.setText(self.labelFit.text() + str(meanFitness))
        self.labelSTD.setText(self.labelSTD.text() + str(standardDeviation))

    def runStatistics(self):
        pool = ThreadPool(10)
        results = pool.map(self.computeStatistics, [i for i in range(self.statsNR)])
        pool.close()
        pool.join()
        mean = sum(results)/len(results)
        return math.sqrt(sum([(results[i] - mean) ** 2 for i in range(self.statsNR)]) / self.statsNR), mean

    def computeStatistics(self, index):
        return self.statistics[index].runAlgorithm().getBestFitness()

    def runAlgorithm(self):
        self.pool = multiprocessing.Pool(3)
        sol = self.pool.map(self.algorithm.runAlgorithm, )
        self.pool.close()
        self.pool.join()
        self.plainSol.setText(str(sol[0]) + '\n\n' + sol[0].getBestFitness())

    def setBestUntilNow(self):
        self.plainBest.setPlainText(str(self.algorithm.getBestUntilNow()))

    def stopRun(self):
        self.pool.terminate()

    def setupUi(self):
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.widget_3 = QtWidgets.QWidget(self)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_3)
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_5.addWidget(self.label_3)
        self.plainSol = QtWidgets.QTextEdit(self.widget_3)
        self.verticalLayout_5.addWidget(self.plainSol)
        self.horizontalLayout.addWidget(self.widget_3)
        self.widget_2 = QtWidgets.QWidget(self)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_3.addWidget(self.label_4)
        self.plainBest = QtWidgets.QTextEdit(self.widget_2)
        self.verticalLayout_3.addWidget(self.plainBest)
        self.horizontalLayout.addWidget(self.widget_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.labelSTD = QtWidgets.QLabel(self)
        self.verticalLayout_2.addWidget(self.labelSTD)
        self.labelFit = QtWidgets.QLabel(self)
        self.verticalLayout_2.addWidget(self.labelFit)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.btnStop = QtWidgets.QPushButton(self)
        self.btnStop.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.TuvaluCountry))
        self.verticalLayout_4.addWidget(self.btnStop)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.btnRun = QtWidgets.QPushButton(self)
        self.horizontalLayout_3.addWidget(self.btnRun)
        self.btnBest = QtWidgets.QPushButton(self)
        self.horizontalLayout_3.addWidget(self.btnBest)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.btnBest.clicked.connect(self.setBestUntilNow)
        self.btnStop.clicked.connect(self.stopRun)
        self.btnBest.clicked.connect(self.runAlgorithm)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_3.setText(_translate("Dialog", "Best Solution"))
        self.label_4.setText(_translate("Dialog", "Best Until Now"))
        self.labelSTD.setText(_translate("Dialog", "Standard Deviation: "))
        self.labelFit.setText(_translate("Dialog", "Fitness Mean: "))
        self.btnStop.setText(_translate("Dialog", "Stop Run"))
        self.btnRun.setText(_translate("Dialog", "Run Algorithm"))
        self.btnBest.setText(_translate("Dialog", "Get Best Solution"))
