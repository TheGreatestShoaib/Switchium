# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwin.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1125, 832)
        MainWindow.setStyleSheet("background:rgb(35, 32, 34);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stacked_frame = QtWidgets.QStackedWidget(self.centralwidget)
        self.stacked_frame.setGeometry(QtCore.QRect(10, 100, 1101, 621))
        self.stacked_frame.setMouseTracking(False)
        self.stacked_frame.setAcceptDrops(True)
        self.stacked_frame.setAutoFillBackground(False)
        self.stacked_frame.setStyleSheet("background:white;")
        self.stacked_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.stacked_frame.setLineWidth(1)
        self.stacked_frame.setMidLineWidth(-1)
        self.stacked_frame.setObjectName("stacked_frame")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(570, 60, 131, 41))
        self.pushButton.setStyleSheet("background:rgb(68, 61, 67);\n"
"color:white;\n"
"font-size:13px;\n"
"font-family:Georgia;\n"
"border:3px solid black;\n"
"border-radius:15px;")
        self.pushButton.setObjectName("pushButton")
        self.preview_label1 = QtWidgets.QLabel(self.page)
        self.preview_label1.setGeometry(QtCore.QRect(90, 250, 591, 321))
        self.preview_label1.setAcceptDrops(True)
        self.preview_label1.setStyleSheet("border:4px solid white;\n"
"border-radius:3px;")
        self.preview_label1.setText("")
        self.preview_label1.setPixmap(QtGui.QPixmap("../../java_codes/124257240_3161320557306202_7239468197628284308_o.jpg"))
        self.preview_label1.setScaledContents(True)
        self.preview_label1.setObjectName("preview_label1")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(60, 60, 491, 41))
        self.label.setStyleSheet("background:rgb(68, 61, 67);\n"
"color:white;\n"
"font-size:18px;\n"
"font-family:Georgia;\n"
"border:3px solid black;\n"
"border-radius:15px;")
        self.label.setObjectName("label")
        self.preview_text_label1 = QtWidgets.QLabel(self.page)
        self.preview_text_label1.setGeometry(QtCore.QRect(290, 170, 151, 31))
        self.preview_text_label1.setStyleSheet("background:rgb(68, 61, 67);\n"
"color:white;\n"
"font-size:17px;\n"
"font-family:Georgia;\n"
"border:3px solid black;\n"
"")
        self.preview_text_label1.setObjectName("preview_text_label1")
        self.line = QtWidgets.QFrame(self.page)
        self.line.setGeometry(QtCore.QRect(770, 40, 20, 521))
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(5)
        self.line.setMidLineWidth(21)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.pushButton_2 = QtWidgets.QPushButton(self.page)
        self.pushButton_2.setGeometry(QtCore.QRect(890, 110, 91, 91))
        self.pushButton_2.setStyleSheet("\n"
"border:5px solid black;\n"
"border-radius:45px;\n"
"background:cyan;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(900, 60, 91, 21))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.page)
        self.label_6.setGeometry(QtCore.QRect(800, 240, 101, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.page)
        self.label_7.setGeometry(QtCore.QRect(800, 380, 141, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.page)
        self.label_8.setGeometry(QtCore.QRect(80, 220, 61, 16))
        self.label_8.setStyleSheet("font-size:18px;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.page)
        self.label_9.setGeometry(QtCore.QRect(40, 265, 51, 21))
        self.label_9.setStyleSheet("font-size:18px;")
        self.label_9.setObjectName("label_9")
        self.horizontalSlider = QtWidgets.QSlider(self.page)
        self.horizontalSlider.setGeometry(QtCore.QRect(800, 440, 191, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.pushButton_3 = QtWidgets.QPushButton(self.page)
        self.pushButton_3.setGeometry(QtCore.QRect(1020, 420, 51, 51))
        self.pushButton_3.setStyleSheet("\n"
"border:2px solid black;\n"
"border-radius:25px;\n"
"background:cyan;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.line_2 = QtWidgets.QFrame(self.page)
        self.line_2.setGeometry(QtCore.QRect(790, 400, 301, 20))
        self.line_2.setLineWidth(3)
        self.line_2.setMidLineWidth(1)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.page)
        self.line_3.setGeometry(QtCore.QRect(790, 480, 301, 20))
        self.line_3.setLineWidth(3)
        self.line_3.setMidLineWidth(1)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.page)
        self.line_4.setGeometry(QtCore.QRect(790, 260, 301, 20))
        self.line_4.setLineWidth(3)
        self.line_4.setMidLineWidth(1)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.page)
        self.line_5.setGeometry(QtCore.QRect(790, 330, 301, 20))
        self.line_5.setLineWidth(3)
        self.line_5.setMidLineWidth(1)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.page)
        self.line_6.setGeometry(QtCore.QRect(790, 210, 301, 20))
        self.line_6.setLineWidth(3)
        self.line_6.setMidLineWidth(1)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.instruction_message1 = QtWidgets.QLabel(self.page)
        self.instruction_message1.setGeometry(QtCore.QRect(30, 10, 381, 21))
        self.instruction_message1.setStyleSheet("\n"
"\n"
"font-size:15px;\n"
"font-family:Georgia;\n"
"\n"
"")
        self.instruction_message1.setObjectName("instruction_message1")
        self.highlightor_star1 = QtWidgets.QLabel(self.page)
        self.highlightor_star1.setGeometry(QtCore.QRect(0, 10, 31, 21))
        self.highlightor_star1.setStyleSheet("color:red;\n"
"font-size:25px;\n"
"font-family:Georgia;")
        self.highlightor_star1.setObjectName("highlightor_star1")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(160, 210, 201, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("res/Icons/horizontalarrow.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(40, 310, 41, 191))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("res/Icons/verticalarrow.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.stacked_frame.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setGeometry(QtCore.QRect(280, 270, 211, 121))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../../java_codes/124257240_3161320557306202_7239468197628284308_o.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_10 = QtWidgets.QLabel(self.page_2)
        self.label_10.setGeometry(QtCore.QRect(30, 270, 211, 121))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("../../java_codes/abandonsa.jpg"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.page_2)
        self.label_11.setGeometry(QtCore.QRect(80, 230, 131, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.page_2)
        self.label_12.setGeometry(QtCore.QRect(340, 240, 81, 20))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.page_2)
        self.label_13.setGeometry(QtCore.QRect(40, 100, 321, 41))
        self.label_13.setStyleSheet("background:rgb(68, 61, 67);\n"
"color:white;\n"
"font-size:18px;\n"
"font-family:Georgia;\n"
"border:3px solid black;\n"
"border-radius:15px;")
        self.label_13.setObjectName("label_13")
        self.pushButton_6 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_6.setGeometry(QtCore.QRect(380, 100, 131, 41))
        self.pushButton_6.setStyleSheet("background:rgb(68, 61, 67);\n"
"color:white;\n"
"font-size:13px;\n"
"font-family:Georgia;\n"
"border:3px solid black;\n"
"border-radius:15px;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.widget = QtWidgets.QWidget(self.page_2)
        self.widget.setGeometry(QtCore.QRect(850, 30, 241, 581))
        self.widget.setStyleSheet("background:gray;")
        self.widget.setObjectName("widget")
        self.scrollArea = QtWidgets.QScrollArea(self.widget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 50, 201, 521))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 199, 519))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_18.setGeometry(QtCore.QRect(10, 40, 101, 61))
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("../../java_codes/124257240_3161320557306202_7239468197628284308_o.jpg"))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName("label_18")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.stacked_frame.addWidget(self.page_2)
        self.footer_frame = QtWidgets.QFrame(self.centralwidget)
        self.footer_frame.setGeometry(QtCore.QRect(10, 730, 1101, 80))
        self.footer_frame.setStyleSheet("background:rgb(0, 170, 255);")
        self.footer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer_frame.setObjectName("footer_frame")
        self.pushButton_4 = QtWidgets.QPushButton(self.footer_frame)
        self.pushButton_4.setGeometry(QtCore.QRect(920, 20, 161, 31))
        self.pushButton_4.setStyleSheet("background:black;\n"
"color:rgb(255, 60, 12);\n"
"font-size:15px;\n"
"font-family:Georgia;\n"
"text-shadow: 12px 2px black;\n"
"opacity:809%;\n"
"")
        self.pushButton_4.setCheckable(False)
        self.pushButton_4.setChecked(False)
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.header_frame = QtWidgets.QFrame(self.centralwidget)
        self.header_frame.setGeometry(QtCore.QRect(10, 0, 1101, 91))
        self.header_frame.setStyleSheet("background:rgb(157, 198, 202)")
        self.header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_frame.setLineWidth(0)
        self.header_frame.setObjectName("header_frame")
        self.comboBox = QtWidgets.QComboBox(self.header_frame)
        self.comboBox.setGeometry(QtCore.QRect(910, 10, 181, 31))
        self.comboBox.setStyleSheet("background:rgb(68, 61, 67);\n"
"color:white;\n"
"font-size:15px;\n"
"font-family:Georgia;\n"
"border:5px solid black;\n"
"")
        self.comboBox.setInputMethodHints(QtCore.Qt.ImhUrlCharactersOnly)
        self.comboBox.setEditable(False)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtCurrent)
        self.comboBox.setObjectName("comboBox")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/Icons/Innactive.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("res/Icons/Active.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        self.comboBox.addItem(icon, "")
        self.comboBox.addItem("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("res/Icons/Innactive.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        self.comboBox.addItem(icon1, "")
        self.pushButton_5 = QtWidgets.QPushButton(self.header_frame)
        self.pushButton_5.setGeometry(QtCore.QRect(300, 30, 171, 31))
        self.pushButton_5.setStyleSheet("background:rgb(68, 61, 67);\n"
"color:white;\n"
"font-size:15px;\n"
"font-family:Georgia;\n"
"border:3px solid black;\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("res/Icons/create_profile_addicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon2)
        self.pushButton_5.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit = QtWidgets.QLineEdit(self.header_frame)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 281, 31))
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit.setMouseTracking(False)
        self.lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit.setStyleSheet("background:white;")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(60)
        self.lineEdit.setFrame(True)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setCursorPosition(0)
        self.lineEdit.setDragEnabled(True)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1125, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stacked_frame.setCurrentIndex(1)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Select Wallapaper"))
        self.label.setText(_translate("MainWindow", "    D:\\Pictures\\Images\\wallpaper.jpeg"))
        self.preview_text_label1.setText(_translate("MainWindow", "          Preview:"))
        self.pushButton_2.setText(_translate("MainWindow", "Color"))
        self.label_3.setText(_translate("MainWindow", "Use Solid color"))
        self.label_6.setText(_translate("MainWindow", "Change Display size"))
        self.label_7.setText(_translate("MainWindow", "Add Overlay"))
        self.label_8.setText(_translate("MainWindow", "   1920"))
        self.label_9.setText(_translate("MainWindow", "1080"))
        self.pushButton_3.setText(_translate("MainWindow", "Color"))
        self.instruction_message1.setText(_translate("MainWindow", " Press Right Arrow for switching Multipaper Mode"))
        self.highlightor_star1.setText(_translate("MainWindow", "  *"))
        self.label_11.setText(_translate("MainWindow", "Currentpaper Preview"))
        self.label_12.setText(_translate("MainWindow", "Next Wallpaper"))
        self.label_13.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_6.setText(_translate("MainWindow", "Select Directory"))
        self.pushButton_4.setText(_translate("MainWindow", "Know how to use"))
        self.comboBox.setItemText(0, _translate("MainWindow", " Select Profile"))
        self.comboBox.setItemText(1, _translate("MainWindow", "MidNight"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Sunlight"))
        self.pushButton_5.setText(_translate("MainWindow", "Create Profile"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Create Profile"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    Ui_MainWindow().setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
