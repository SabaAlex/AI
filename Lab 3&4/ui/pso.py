import typing

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

from algorithm.PSOAlgorithm import PSOAlgorithm


class Ui_PSO(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.widget = QtWidgets.QWidget(self)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.lineN = QtWidgets.QLineEdit(self.widget)
        self.verticalLayout.addWidget(self.lineN)
        self.lineIterations = QtWidgets.QLineEdit(self.widget)
        self.lineIterations.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.lineIterations)
        self.lineSwarmSize = QtWidgets.QLineEdit(self.widget)
        self.verticalLayout.addWidget(self.lineSwarmSize)
        self.lineNeighboursNR = QtWidgets.QLineEdit(self.widget)
        self.verticalLayout.addWidget(self.lineNeighboursNR)
        self.lineC1 = QtWidgets.QLineEdit(self.widget)
        self.verticalLayout.addWidget(self.lineC1)
        self.lineC2 = QtWidgets.QLineEdit(self.widget)
        self.verticalLayout.addWidget(self.lineC2)
        self.lineW = QtWidgets.QLineEdit(self.widget)
        self.verticalLayout.addWidget(self.lineW)
        self.btOK = QtWidgets.QPushButton(self.widget)
        self.verticalLayout.addWidget(self.btOK)
        self.verticalLayout_2.addWidget(self.widget)
        self.algorithm = None
        self.setupUi()

    def getAlgorithm(self):
        return self.algorithm

    def setupUi(self):
        self.setModal(True)
        self.lineN.setAlignment(QtCore.Qt.AlignCenter)
        self.lineW.setAlignment(QtCore.Qt.AlignCenter)
        self.lineC2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineC1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineNeighboursNR.setAlignment(QtCore.Qt.AlignCenter)
        self.lineSwarmSize.setAlignment(QtCore.Qt.AlignCenter)
        self.btOK.clicked.connect(self.btnClicked)

        self.retranslateUi()

    def btnClicked(self):
        try:
            self.algorithm = PSOAlgorithm(int(self.lineN.text()), int(self.lineIterations.text()),
                                          int(self.lineSwarmSize.text()), int(self.lineNeighboursNR.text()),
                                          float(self.lineC1.text()), float(self.lineC2.text()), float(self.lineW.text()))
        except Exception:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Wrong Type of data was entered!")
            msg.setWindowTitle("Error")
            msg.exec_()
        if self.algorithm is not None:
            self.accept()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.lineN.setPlaceholderText(_translate("PSO", "N"))
        self.lineIterations.setPlaceholderText(_translate("PSO", "iterations"))
        self.lineSwarmSize.setPlaceholderText(_translate("PSO", "swarmSize"))
        self.lineNeighboursNR.setPlaceholderText(_translate("PSO", "numberOfNeighbours"))
        self.lineC1.setPlaceholderText(_translate("PSO", "c1"))
        self.lineC2.setPlaceholderText(_translate("PSO", "c2"))
        self.lineW.setPlaceholderText(_translate("PSO", "w"))
        self.btOK.setText(_translate("PSO", "OK"))
