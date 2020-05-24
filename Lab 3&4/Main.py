from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from SimpleUI import SimpleUI
from ui.choosealgorithm import Ui_ChooseAlgorithm

if __name__ == '__main__':
    ok = True
    while ok:
        choice = input("Enter 1 or 2\n"
                       "1. GUI(very unstable)\n"
                       "2. Console UI\n"
                       ">>")
        if int(choice) == 1:
            ok = False
            app = QtWidgets.QApplication(sys.argv)
            ui = Ui_ChooseAlgorithm()
            ui.show()
            sys.exit(app.exec_())
        elif int(choice) == 2:
            ok = False
            ui = SimpleUI()
            ui.runUI()
        else:
            print("Try Again!")