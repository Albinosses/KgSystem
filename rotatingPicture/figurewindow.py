# Form implementation generated from reading ui file 'FigureWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QPixmap
import matplotlib.pyplot as plt
import numpy as np
from PyQt6.QtWidgets import QSizePolicy, QLabel

from rotatingPicture.figureFunctions import *


class ClickableLabel(QLabel):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()

class Ui_FigureWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(851, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 200, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.submitButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(180, 460, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.submitButton.setFont(font)
        self.submitButton.setObjectName("submitButton")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(430, 70, 411, 371))
        self.widget.setObjectName("widget")
        self.image = QtWidgets.QLabel(parent=self.widget)
        self.image.setGeometry(QtCore.QRect(8, 5, 401, 361))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy)
        self.image.setText("")
        self.image.setScaledContents(False)
        self.image.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.image.setObjectName("image")
        self.clear_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(580, 460, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.clear_button.setFont(font)
        self.clear_button.setObjectName("clear_button")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 240, 391, 180))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 1, 1, 1)
        self.x2 = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.x2.setMinimum(-100.0)
        self.x2.setObjectName("x2")
        self.gridLayout.addWidget(self.x2, 2, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)
        self.y3 = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.y3.setMinimum(-100.0)
        self.y3.setObjectName("y3")
        self.gridLayout.addWidget(self.y3, 3, 4, 1, 1)
        self.sizeCoefficient = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.sizeCoefficient.setObjectName("sizeCoefficient")
        self.gridLayout.addWidget(self.sizeCoefficient, 6, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 1, 1, 1)
        self.y1 = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.y1.setMinimum(-100.0)
        self.y1.setObjectName("y1")
        self.gridLayout.addWidget(self.y1, 0, 4, 1, 1)
        self.x1 = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.x1.setMinimum(-100.0)
        self.x1.setObjectName("x1")
        self.gridLayout.addWidget(self.x1, 0, 2, 1, 1)
        self.x3 = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.x3.setMinimum(-100.0)
        self.x3.setObjectName("x3")
        self.gridLayout.addWidget(self.x3, 3, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 3, 1, 1)
        self.x4 = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.x4.setMinimum(-100.0)
        self.x4.setObjectName("x4")
        self.gridLayout.addWidget(self.x4, 4, 2, 1, 1)
        self.rotationDegrees = QtWidgets.QSpinBox(parent=self.gridLayoutWidget)
        self.rotationDegrees.setMinimum(-360)
        self.rotationDegrees.setMaximum(360)
        self.rotationDegrees.setObjectName("rotationDegrees")
        self.gridLayout.addWidget(self.rotationDegrees, 5, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 1, 1, 1)
        self.y2 = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.y2.setMinimum(-100.0)
        self.y2.setObjectName("y2")
        self.gridLayout.addWidget(self.y2, 2, 4, 1, 1)
        self.y4 = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.y4.setMinimum(-100.0)
        self.y4.setObjectName("y4")
        self.gridLayout.addWidget(self.y4, 4, 4, 1, 1)
        self.label_10 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 4, 3, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 851, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.mainPage = ClickableLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        self.mainPage.setFont(font)
        self.mainPage.setObjectName("mainPage")
        self.horizontalLayout.addWidget(self.mainPage)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.lab1 = ClickableLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        self.lab1.setFont(font)
        self.lab1.setObjectName("lab1")
        self.horizontalLayout.addWidget(self.lab1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.lab2 = ClickableLabel(parent=self.horizontalLayoutWidget)
        self.lab2.setObjectName("lab2")
        self.horizontalLayout.addWidget(self.lab2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.lab3 = ClickableLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        self.lab3.setFont(font)
        self.lab3.setObjectName("lab3")
        self.horizontalLayout.addWidget(self.lab3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.lectures = ClickableLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        self.lectures.setFont(font)
        self.lectures.setObjectName("lectures")
        self.horizontalLayout.addWidget(self.lectures)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.about = ClickableLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        self.about.setFont(font)
        self.about.setObjectName("about")
        self.horizontalLayout.addWidget(self.about)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 851, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Own code here
        self.add_functions()

        self.image.setPixmap(QPixmap())
        self.image.setPixmap(QPixmap("gray_placeholder.png"))

        self.x4.setEnabled(False)
        self.y4.setEnabled(False)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FractalWindow"))
        self.label.setText(_translate("MainWindow", "Fill in the forms"))
        self.submitButton.setText(_translate("MainWindow", "Submit"))
        self.clear_button.setText(_translate("MainWindow", "Clear"))
        self.label_8.setText(_translate("MainWindow", "Enter x2:"))
        self.label_3.setText(_translate("MainWindow", "Enter y1:"))
        self.label_9.setText(_translate("MainWindow", "Enter x4:"))
        self.label_2.setText(_translate("MainWindow", "Enter x1:"))
        self.label_5.setText(_translate("MainWindow", "Enter y3:"))
        self.label_6.setText(_translate("MainWindow", "Enter rotation degrees:"))
        self.label_4.setText(_translate("MainWindow", "Enter x3:"))
        self.label_7.setText(_translate("MainWindow", "Enter size coefficient:"))
        self.label_10.setText(_translate("MainWindow", "Enter y2:"))
        self.label_11.setText(_translate("MainWindow", "Enter y4:"))
        self.mainPage.setText(_translate("MainWindow", "Main page"))
        self.lab1.setText(_translate("MainWindow", "Lab 1"))
        self.lab2.setText(_translate("MainWindow", "Lab 2"))
        self.lab3.setText(_translate("MainWindow", "Lab 3"))
        self.lectures.setText(_translate("MainWindow", "Lectures"))
        self.about.setText(_translate("MainWindow", "About"))

    def add_functions(self):
        self.submitButton.clicked.connect(lambda: self.rotateImage())

        self.x1.valueChanged.connect(lambda: self.fixPoints())
        self.x2.valueChanged.connect(lambda: self.fixPoints())
        self.x3.valueChanged.connect(lambda: self.fixPoints())
        self.y1.valueChanged.connect(lambda: self.fixPoints())
        self.y2.valueChanged.connect(lambda: self.fixPoints())
        self.y3.valueChanged.connect(lambda: self.fixPoints())

    def fixPoints(self):
        x1 = self.x1.value()
        x2 = self.x2.value()
        x3 = self.x3.value()

        y1 = self.y1.value()
        y2 = self.y2.value()
        y3 = self.y3.value()

        x4, y4 = calculate_fourth_point(x1, y1, x2, y2, x3, y3)

        self.x4.setValue(x4)
        self.y4.setValue(y4)

    def rotateImage(self):
        x1 = self.x1.value()
        x2 = self.x2.value()
        x3 = self.x3.value()
        x4 = self.x4.value()

        y1 = self.y1.value()
        y2 = self.y2.value()
        y3 = self.y3.value()
        y4 = self.y4.value()

        rotation_degrees = self.rotationDegrees.value()
        resizing_coefficient = self.sizeCoefficient.value()

        parallelogram_matrix = np.array([[x1, x2, x3, x4], [y1, y2, y3, y4]])
        rotated_parallelogram = parallelogram_matrix.copy()

        display_rotated_parallelogram(parallelogram_matrix, rotated_parallelogram, 10, resizing_coefficient,
                                      rotation_degrees)

        original_pixmap = QPixmap("rotated_parallelogram.png")
        self.image.setPixmap(
            original_pixmap.scaled(self.image.size(), aspectRatioMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_FigureWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
