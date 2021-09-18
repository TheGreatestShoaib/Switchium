

from src import Ui_MainWindow as mainbox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
import sys
from data_maker import *
from src import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
import CoreUtils as cu

class StartQT4(QtWidgets.QMainWindow):
    data= cu.find_key()
    #profiled_data = data[self.comboBox.currentText()]
    
    # def return_val(self):
    #     profiled_data = self.data[self.comboBox.currentText()]
    #     return profiled_data

        
    def dialog(self):
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        files, _ =  QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        #files = QFileDialog.getExistingDirectory(self, 'Select an awesome directory')
        if files:
            if len(files) <= 1:
                saves =POST_data(files,self.data[self.ui.comboBox.currentText()])
                cu.dump_data(self.ui.comboBox.currentText(),saves)
                #print(type(files))
            else:
                #print(files)
                saves = POST_data(files,self.data[self.ui.comboBox.currentText()])
                cu.dump_data(self.ui.comboBox.currentText(),saves)



    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.ui.pushButton_8.clicked.connect(self.printer)
        self.ui.pushButton_4.clicked.connect(self.CloseApp)
        #QtCore.qInstallMessageHandler(self.handler)
        self.ui.pushButton.clicked.connect(self.dialog)


        #self.clicked = False
        self.ui.frame_2.clicked = False

    def CloseApp(self):
        QApplication. quit()

    def mousePressEvent(self, event):
        self.old_pos = event.screenPos()

    def mouseMoveEvent(self, event):
        #if self.clicked:
        if self.ui.frame_2.clicked:
            dx = self.old_pos.x() - event.screenPos().x()
            dy = self.old_pos.y() - event.screenPos().y()
            self.move(self.pos().x() - dx, self.pos().y() - dy)
        self.old_pos = event.screenPos()
        #self.clicked = True
        self.ui.frame_2.clicked = True

        return QWidget.mouseMoveEvent(self, event)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = StartQT4()

    myapp.show()
    sys.exit(app.exec_())




    

    # sys_window = QtWidgets.QWidget()
    # sys_tray_icon = SystemTray(QtGui.QIcon("res/Icons/Active.png"), sys_window)
    # sys_tray_icon.show()
