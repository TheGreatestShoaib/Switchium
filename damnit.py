#!/usr/bin/env pythonw

from src import Ui_MainWindow as mainbox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
import sys
from data_maker import *
from src import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog ,QColorDialog
import CoreUtils as cu
import ctypes

class StartQT4(QtWidgets.QMainWindow):
    data= cu.find_key()
    #profiled_data = data[self.comboBox.currentText()]
    
    # def return_val(self):
    #     profiled_data = self.data[self.comboBox.currentText()]
    #     return profiled_data


    def screensize(self):
        user32 = ctypes.windll.user32
        screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

        return screensize


    def minimize_app(self):
        self.showMinimized()
        
   
    def dialog(self):
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        files, _ =  QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        #files = QFileDialog.getExistingDirectory(self, 'Select an awesome directory')
        time_interval = self.ui.comboBox_2.currentText()
        if files:
            if len(files) <= 1:
                saves =POST_data(files,self.data[self.ui.comboBox.currentText()],time_interval)
                cu.dump_data(self.ui.comboBox.currentText(),saves)
                #print(type(files))
            else:
                #print(files)
                saves = POST_data(files,self.data[self.ui.comboBox.currentText()],time_interval)
                cu.dump_data(self.ui.comboBox.currentText(),saves)





    def color_dialog_bg(self):
        color = QColorDialog.getColor()


        if color.isValid():
            #print(color.name())
            self.ui.pushButton_2.setStyleSheet("\n"
            "border:5px solid #44475a;\n"
            "border-radius:45px;\n"
            f"background:{color.name()};")

    def color_dialog_overlay(self):
        color = QColorDialog.getColor()


        if color.isValid():
            #print(color.name())
            self.ui.pushButton_3.setStyleSheet("\n"
                "border:2px solid #44475a;\n"
                "border-radius:25px;\n"
                f"background:{color.name()};")



    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.ui.pushButton_8.clicked.connect(self.printer)
        self.ui.pushButton_4.clicked.connect(self.CloseApp)
        #QtCore.qInstallMessageHandler(self.handler)
        self.ui.pushButton.clicked.connect(self.dialog)
        self.ui.pushButton_2.clicked.connect(self.color_dialog_overlay)
        self.ui.pushButton_3.clicked.connect(self.color_dialog_overlay)
        self.ui.pushButton_9.clicked.connect(lambda: self.showMinimized())

        self.ui.label_8.setText( f"   { self.screensize()[0] }")
        self.ui.label_9.setText( f"{ self.screensize()[1] }")



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
