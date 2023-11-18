from PyQt6 import QtWidgets
from fractals.fractalwindow import Ui_FractalWindow
from colorModels.colorwindow import Ui_ColorWindow
from mainPage.mainwindow import Ui_MainWindow
from rotatingPicture.figurewindow import Ui_FigureWindow
from aboutPage.aboutwindow import Ui_AboutWindow
from lecturesPage.lectureswindow import Ui_LecturesWindow


class MainWindowController:
    def __init__(self):
        self.main_window = QtWidgets.QMainWindow()
        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self.main_window)

        self.fractal_window = QtWidgets.QMainWindow()
        self.ui_fractal = Ui_FractalWindow()
        self.ui_fractal.setupUi(self.fractal_window)

        self.color_window = QtWidgets.QMainWindow()
        self.ui_color = Ui_ColorWindow()
        self.ui_color.setupUi(self.color_window)

        self.figure_window = QtWidgets.QMainWindow()
        self.ui_figure = Ui_FigureWindow()
        self.ui_figure.setupUi(self.figure_window)

        self.about_window = QtWidgets.QMainWindow()
        self.ui_about = Ui_AboutWindow()
        self.ui_about.setupUi(self.about_window)

        self.lectures_window = QtWidgets.QMainWindow()
        self.ui_lectures = Ui_LecturesWindow()
        self.ui_lectures.setupUi(self.lectures_window)

        # Connect signals and slots for button clicks or any other events
        self.ui_main.lab2.clicked.connect(self.show_color_window)
        self.ui_main.lab3.clicked.connect(self.show_figure_window)
        self.ui_main.lab1.clicked.connect(self.show_fractal_window)
        self.ui_main.about.clicked.connect(self.show_about_window)
        self.ui_main.lectures.clicked.connect(self.show_lectures_window)

        self.ui_about.lab2.clicked.connect(self.show_color_window)
        self.ui_about.lab3.clicked.connect(self.show_figure_window)
        self.ui_about.lab1.clicked.connect(self.show_fractal_window)
        self.ui_about.mainPage.clicked.connect(self.show_main_window)
        self.ui_about.lectures.clicked.connect(self.show_lectures_window)

        self.ui_lectures.lab2.clicked.connect(self.show_color_window)
        self.ui_lectures.lab3.clicked.connect(self.show_figure_window)
        self.ui_lectures.lab1.clicked.connect(self.show_fractal_window)
        self.ui_lectures.mainPage.clicked.connect(self.show_main_window)
        self.ui_lectures.about.clicked.connect(self.show_about_window)

        self.ui_fractal.lab2.clicked.connect(self.show_color_window)
        self.ui_fractal.lab3.clicked.connect(self.show_figure_window)
        self.ui_fractal.mainPage.clicked.connect(self.show_main_window)
        self.ui_fractal.about.clicked.connect(self.show_about_window)
        self.ui_fractal.lectures.clicked.connect(self.show_lectures_window)

        self.ui_figure.lab2.clicked.connect(self.show_color_window)
        self.ui_figure.lab1.clicked.connect(self.show_fractal_window)
        self.ui_figure.mainPage.clicked.connect(self.show_main_window)
        self.ui_figure.about.clicked.connect(self.show_about_window)
        self.ui_figure.lectures.clicked.connect(self.show_lectures_window)

        self.ui_color.lab3.clicked.connect(self.show_figure_window)
        self.ui_color.lab1.clicked.connect(self.show_fractal_window)
        self.ui_color.mainPage.clicked.connect(self.show_main_window)
        self.ui_color.about.clicked.connect(self.show_about_window)
        self.ui_color.lectures.clicked.connect(self.show_lectures_window)

    def show_main_window(self):
        self.main_window.show()
        self.color_window.hide()
        self.figure_window.hide()
        self.about_window.hide()
        self.fractal_window.hide()
        self.lectures_window.hide()

    def show_color_window(self):
        self.main_window.hide()
        self.color_window.show()
        self.figure_window.hide()
        self.about_window.hide()
        self.fractal_window.hide()
        self.lectures_window.hide()

    def show_figure_window(self):
        self.main_window.hide()
        self.color_window.hide()
        self.figure_window.show()
        self.about_window.hide()
        self.fractal_window.hide()
        self.lectures_window.hide()

    def show_fractal_window(self):
        self.main_window.hide()
        self.color_window.hide()
        self.figure_window.hide()
        self.about_window.hide()
        self.fractal_window.show()
        self.lectures_window.hide()

    def show_about_window(self):
        self.main_window.hide()
        self.color_window.hide()
        self.figure_window.hide()
        self.about_window.show()
        self.fractal_window.hide()
        self.lectures_window.hide()

    def show_lectures_window(self):
        self.main_window.hide()
        self.color_window.hide()
        self.figure_window.hide()
        self.about_window.hide()
        self.fractal_window.hide()
        self.lectures_window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindowW()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    controller = MainWindowController()
    controller.show_main_window()
    sys.exit(app.exec())
