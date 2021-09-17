

from src import Ui_MainWindow as mainbox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget

import sys

from src import Ui_MainWindow

class StartQT4(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #self.setFrameStyle(QFrame::HLine | QFrame::Sunken)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_8.clicked.connect(self.printer)
        self.ui.pushButton_4.clicked.connect(self.CloseApp)
        self.clicked = False


    def printer(self):
        for i in range(10):
            print("bruh")

    def CloseApp(self):
        QApplication. quit()


    def mousePressEvent(self, event):
        self.old_pos = event.screenPos()

    def mouseMoveEvent(self, event):
        if self.clicked:
            dx = self.old_pos.x() - event.screenPos().x()
            dy = self.old_pos.y() - event.screenPos().y()
            self.move(self.pos().x() - dx, self.pos().y() - dy)
        self.old_pos = event.screenPos()
        self.clicked = True

        return QWidget.mouseMoveEvent(self, event)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
