from PyQt5 import QtCore, QtGui, QtWidgets

from algorithm.EvolutionaryAlgorithm import EvolutionaryAlgorithm
from algorithm.HillClimbingAlgorithm import HillClimbingAlgorithm
from algorithm.PSOAlgorithm import PSOAlgorithm
from ui.algorithm import Ui_Algorithm
from ui.ea import Ui_EvolutionaryAlgorithm
from ui.hillclimbing import Ui_HillClimbing
from ui.pso import Ui_PSO

class Ui_ChooseAlgorithm(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.widget = QtWidgets.QWidget(self)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.btEA = QtWidgets.QPushButton(self.widget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.addWidget(self.btEA)
        self.btHill = QtWidgets.QPushButton(self.widget)
        self.verticalLayout.addWidget(self.btHill)
        self.btPSO = QtWidgets.QPushButton(self.widget)
        self.verticalLayout.addWidget(self.btPSO)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.btPSO.clicked.connect(self.psoAlgBtn)
        self.btEA.clicked.connect(self.eaAlgBtn)
        self.btHill.clicked.connect(self.hillAlgBtn)
        self.setupUi()

    def setupUi(self):
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setObjectName("centralwidget")
        self.widget.setGeometry(QtCore.QRect(20, 20, 136, 101))
        self.widget.setObjectName("widget")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout.setObjectName("verticalLayout")
        self.btEA.setObjectName("btEA")
        self.btHill.setObjectName("btHill")
        self.btPSO.setObjectName("btPSO")
        self.retranslateUi()

    def eaAlgBtn(self):
        self.prepareInput = Ui_EvolutionaryAlgorithm()
        if self.prepareInput.exec() == QtWidgets.QDialog.Accepted:
            alg = Ui_Algorithm(self.prepareInput.getAlgorithm(),
                               [EvolutionaryAlgorithm(4, 500, 0.4, 40, 2) for x in range(30)], 30)
            alg.exec()

    def hillAlgBtn(self):
        self.prepareInput = Ui_HillClimbing()
        if self.prepareInput.exec() == QtWidgets.QDialog.Accepted:
            alg = Ui_Algorithm(self.prepareInput.getAlgorithm(),
                               [HillClimbingAlgorithm(4, 500) for x in range(30)], 30)
            alg.exec()

    def psoAlgBtn(self):
        self.prepareInput = Ui_PSO()
        if self.prepareInput.exec() == QtWidgets.QDialog.Accepted:
            alg = Ui_Algorithm(self.prepareInput.getAlgorithm(),
                               [PSOAlgorithm(4, 500, 40, 5, 1, 2.5, 1.0) for x in range(30)], 30)
            alg.exec()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("ChooseAlgorithm", "Choose Algorithm"))
        self.btEA.setText(_translate("ChooseAlgorithm", "Evolutionary Algorithm"))
        self.btHill.setText(_translate("ChooseAlgorithm", "Hill Climbing"))
        self.btPSO.setText(_translate("ChooseAlgorithm", "PSO"))

