import sys
import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def read_hosts():
    file = open("hosts.ini", "r") 
    return file.readlines() 

class Worker(QObject):
    update = pyqtSignal(str, int)
    exception = pyqtSignal(str)

    def check_ping(self):
        hosts = read_hosts()
        while True:
            for host in hosts:
                params = "-l 1000"
                response = os.system("ping  {} {}".format(host, params))
                print("weiter")
                self.update.emit(host, response)

class Window(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.layout = QVBoxLayout(self)

        hosts = read_hosts()
        for host in hosts:
            label = QLabel(host)
            label.setObjectName(host)
            label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("QLabel {background-color: green;}")
            self.layout.addWidget(label)
        self.startWorker()

    def startWorker(self):
        self.thread = QThread() 
        self.obj = Worker()  
        self.thread = QThread() 
        self.obj.moveToThread(self.thread)
        self.obj.update.connect(self.onUpdate)
        self.obj.exception.connect(self.onException)
        self.thread.started.connect(self.obj.check_ping)
        self.thread.start()

    def onException(self, msg):
        QMessageBox.warning(self, "Eine Exception im Worker wurde geworfen: ", msg)

    def onUpdate(self, host, value):
        label = self.findChild(QLabel, host)
        label.setText("{}".format(value))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())