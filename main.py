from fractal import *
from cut import *
from enum import Enum
from PyQt6 import QtCore, QtGui, QtWidgets
from fractalwindow import Ui_MainWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())