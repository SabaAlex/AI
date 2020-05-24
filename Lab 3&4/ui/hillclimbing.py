from PyQt5 import QtCore, QtGui, QtWidgets

from algorithm.HillClimbingAlgorithm import HillClimbingAlgorithm


class Ui_HillClimbing(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        self.widget = QtWidgets.QWidget(self)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.lineN = QtWidgets.QLineEdit(self.widget)
        self.verticalLayout.addWidget(self.lineN)
        self.lineIterations = QtWidgets.QLineEdit(self.widget)
        self.verticalLayout.addWidget(self.lineIterations)
        self.btnOk = QtWidgets.QPushButton(self.widget)
        self.verticalLayout.addWidget(self.btnOk)
        self.horizontalLayout.addWidget(self.widget)
        self.algorithm = None
        self.setupUi()

    def getAlgorithm(self):
        return self.algorithm

    def setupUi(self):
        self.setModal(True)
        self.lineN.setAlignment(QtCore.Qt.AlignCenter)
        self.lineIterations.setAlignment(QtCore.Qt.AlignCenter)
        self.btnOk.clicked.connect(self.btnClicked)

        self.retranslateUi()

    def btnClicked(self):
        try:
            self.algorithm = HillClimbingAlgorithm(int(self.lineN.text()), int(self.lineIterations.text()))
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
        self.setWindowTitle(_translate("HillClimbing", "HillClimbing"))
        self.lineN.setPlaceholderText(_translate("HillClimbing", "n"))
        self.lineIterations.setPlaceholderText(_translate("HillClimbing", "iterations"))
        self.btnOk.setText(_translate("HillClimbing", "Ok"))
