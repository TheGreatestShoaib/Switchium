
from src import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

cl



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    Ui_MainWindow().setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())