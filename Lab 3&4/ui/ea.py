import typing

from PyQt5 import QtCore, QtGui, QtWidgets

from algorithm.EvolutionaryAlgorithm import EvolutionaryAlgorithm


class Ui_EvolutionaryAlgorithm(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self)
        self.widget = QtWidgets.QWidget(self)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.lineN = QtWidgets.QLineEdit(self.widget)
        self.verticalLayout.addWidget(self.lineN)
        self.lineGenerationsNr = QtWidgets.QLineEdit(self.widget)
        self.verticalLayout.addWidget(self.lineGenerationsNr)
        self.lineMutationChance = QtWidgets.QLineEdit(self.widget)
        self.verticalLayout.addWidget(self.lineMutationChance)
        self.linePopulationSize = QtWidgets.QLineEdit(self.widget)
        self.verticalLayout.addWidget(self.linePopulationSize)
        self.lineBreedCuts = QtWidgets.QLineEdit(self.widget)
        self.verticalLayout.addWidget(self.lineBreedCuts)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.btnOK = QtWidgets.QPushButton(self.widget)
        self.verticalLayout_2.addWidget(self.btnOK)
        self.verticalLayout_3.addWidget(self.widget)
        self.setupUi()
        self.algorithm = None

    def getAlgorithm(self):
        return self.algorithm

    def setupUi(self):
        self.setModal(True)
        self.lineGenerationsNr.setAlignment(QtCore.Qt.AlignCenter)
        self.lineMutationChance.setAlignment(QtCore.Qt.AlignCenter)
        self.linePopulationSize.setAlignment(QtCore.Qt.AlignCenter)
        self.lineN.setAlignment(QtCore.Qt.AlignCenter)
        self.lineBreedCuts.setAlignment(QtCore.Qt.AlignCenter)
        self.btnOK.clicked.connect(self.btnClicked)
        self.retranslateUi()

    def btnClicked(self):
        try:
            self.algorithm = EvolutionaryAlgorithm(int(self.lineN.text()),
                                                   int(self.lineGenerationsNr.text()),
                                                   float(self.lineMutationChance.text()),
                                                   int(self.linePopulationSize.text()),
                                                   int(self.lineBreedCuts.text()))
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
        self.setWindowTitle(_translate("EvolutionaryAlgorithm", "EvolutionaryAlgorithm"))
        self.lineN.setPlaceholderText(_translate("EvolutionaryAlgorithm", "n"))
        self.lineN.setPlaceholderText(_translate("EvolutionaryAlgorithm", "N"))
        self.lineGenerationsNr.setPlaceholderText(_translate("EvolutionaryAlgorithm", "generationsNR"))
        self.lineMutationChance.setPlaceholderText(_translate("EvolutionaryAlgorithm", "mutationChance"))
        self.linePopulationSize.setPlaceholderText(_translate("EvolutionaryAlgorithm", "populationSize"))
        self.lineBreedCuts.setPlaceholderText(_translate("EvolutionaryAlgorithm", "breedCuts"))
        self.btnOK.setText(_translate("EvolutionaryAlgorithm", "OK"))
