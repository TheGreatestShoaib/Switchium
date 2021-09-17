import os
import sys
from PySide2 import QtWidgets, QtGui
from changebg import change_wallpaper,change_single_wallpaper,paper_plot

class SystemTray(QtWidgets.QSystemTrayIcon):

    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
       
        menu = QtWidgets.QMenu(parent)
        
        change_paper = menu.addAction("Change Wallpaper")
        change_paper.triggered.connect(self.change_background)
        change_paper.setIcon(QtGui.QIcon("wallpapers/arch.png"))

        EXIT = menu.addAction("Exit")
        EXIT.triggered.connect(self.closeapp)
        EXIT.setIcon(QtGui.QIcon("res/Icons/Active.png"))
        self.setContextMenu(menu)
        self.activated.connect(self.onTrayIconActivated)

    def onTrayIconActivated(self, reason):

        if reason == self.DoubleClick:
            self.change_background()

    def change_background(self):
        if paper_plot == "single":
            change_single_wallpaper()
        else:
            change_wallpaper()



    def closeapp(self):
        sys.exit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    sys_tray_icon = SystemTray(QtGui.QIcon("res/Icons/Active.png"), window)
    sys_tray_icon.show()
    sys.exit(app.exec_())
