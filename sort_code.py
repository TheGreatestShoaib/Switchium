#!/usr/bin/env python

from PyQt5.QtWidgets import QApplication, QWidget , QInputDialog, QLineEdit, QFileDialog ,QColorDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from src import Ui_MainWindow


import CoreUtils as cu
from data_maker import *
from CoreUtils.platform_info import ult_screensize


from CoreUtils.create_wallpaper import create_solid_wallpaper,overlay_wallpaper


import sys
import json
import random



#from src import Ui_MainWindow as mainbox


class Switchium_Main_Window(QtWidgets.QMainWindow):

    #screensize = cu.platform_info.ult_screensize
    screensize = ult_screensize()


    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        #call functions

        self.show_profile_names()
        #self.show_allowed_extensions()
        self.set_upcoming_wallpaper()


        #connect functions with buttons

        self.ui.pushButton_4.clicked.connect(lambda : QApplication. quit()) #functions for exit 
        self.ui.pushButton_9.clicked.connect(lambda: self.showMinimized()) #lambda fucntion to minimize window
        
        self.ui.set_wallpaper_btn.clicked.connect(self.dialog)
        self.ui.solid_back_color_btn.clicked.connect(self.color_dialog_bg)
        self.ui.overlay_color_btn.clicked.connect(self.color_dialog_overlay)
       
       
        self.ui.label_8.setText( f"   { self.screensize[0] }")
        self.ui.label_9.setText( f"{ self.screensize[1] }")
        self.ui.create_profile_btn.clicked.connect(self.create_profile)


        self.ui.select_profile_combo.currentIndexChanged.connect(self.active_user_profile)
       
        self.ui.show_preview_btn.clicked.connect(self.do_overlay)

        #self.clicked = False
        self.ui.frame_2.clicked = False


    data= cu.find_key()
    profile_count = 0

    def hide_single_stuffs(self):
        pass


    def create_profile(self):

        text = self.ui.lineEdit.text()
        if text != "":
            cu.dump_data(text,cu.dummy_data)
            self.ui.lineEdit.clear()
            
            self.show_profile_names()


    def show_profile_names(self):
        self.profile_count = 0
        self.ui.select_profile_combo.clear()
        #self.ui.select_profile_combo.refresh
        with open("CoreUtils/_paperDetails_update.json") as f:
            data = json.load(f)
       
        
        for usr_profile in data.keys():
            if usr_profile == "active_profile" or usr_profile == "last_wallpaper" :
                pass
            else:
                self.ui.select_profile_combo.addItem(usr_profile,usr_profile)
                #self.ui.select_profile_combo.setItemText(self.profile_count,usr_profile)

                #self.profile_count +=1


            

    def active_user_profile(self):
        
        try :
            profile_name_text = self.ui.select_profile_combo.currentText()
            
            with open("CoreUtils/_paperDetails_update.json") as f:
                data = json.load(f)

            
            if profile_name_text:
                self.data["active_profile"] = self.ui.select_profile_combo.currentText()
            else:
                pass

            mode = self.data[self.data["active_profile"]]["mode"]
            active_profile = data["active_profile"]
            cu.dump_data("active_profile",self.data["active_profile"])

            self.data["last_wallpaper"] = random.choice(self.data[active_profile]["file_path"])
            
            cu.dump_data("last_wallpaper",self.data["last_wallpaper"])


            self.clear_wcuser_profile()
            self.set_upcoming_wallpaper()
            #self.set_upcoming_wallpaper()

        except:
            pass



        
   
    def dialog(self):
        options = QFileDialog.Options()
        files, _ =  QFileDialog.getOpenFileNames(self,"Select Files", "","All Files (*)", options=options)
        print(files)
        time_interval = self.ui.time_set_combo.currentText()
        active_profile = self.ui.select_profile_combo.currentText()
        key_name = self.data[active_profile]
        
        if files:
                saves = POST_data(files,cu.dummy_data,time_interval) #file_paths , data , time_interval
                cu.dump_data(active_profile,saves)

                if len(files) <= 1:
                    self.hide_single_stuffs()





    def set_upcoming_wallpaper(self):
        with open("CoreUtils/_paperDetails_update.json") as f:
            data = json.load(f)

        last_wallpaper = data["last_wallpaper"]
        active_profile = data["active_profile"]
        wallpaper_paths = data[active_profile]["file_path"]

        single_mode = bool(data[active_profile]["mode"] == "single")

        if not single_mode:
            try:
                for x in range(len(wallpaper_paths)) :
                    if wallpaper_paths[x] == last_wallpaper:
                        self.ui.upcoming_wallpaper.setPixmap(QtGui.QPixmap(wallpaper_paths[x+1]))
                        self.ui.next_wallpaper.setPixmap(QtGui.QPixmap(wallpaper_paths[x+2]))
                
            except IndexError:
                x = 0
                self.ui.upcoming_wallpaper.setPixmap(QtGui.QPixmap(wallpaper_paths[x+1]))
                self.ui.next_wallpaper.setPixmap(QtGui.QPixmap(wallpaper_paths[x+2]))
        else:
            self.ui.upcoming_wallpaper.setPixmap(QtGui.QPixmap(wallpaper_paths))










    def color_dialog_bg(self):
        color = QColorDialog.getColor()
        active_profile = self.data["active_profile"]
   
        solid_bg = create_solid_wallpaper((1920,1080),color.getRgb())

        temp_path_sim = [solid_bg]

        print(solid_bg)
        saves = POST_data(temp_path_sim,cu.dummy_data,10) #file_paths , data , time_interval
        cu.dump_data(active_profile,saves)

        print(active_profile,saves)

        self.set_upcoming_wallpaper()

        if color.isValid():
            #print(color.name())
            self.ui.solid_back_color_btn.setStyleSheet("\n"
            "border:5px solid #44475a;\n"
            "border-radius:45px;\n"
            f"background:{color.name()};")



    def color_dialog_overlay(self):
        self.color_overlay = QColorDialog.getColor()
       
       	# color = self.color_overlay

        # active_profile = self.data["active_profile"]

        # current_wallpaper = self.data[active_profile]["file_path"]
        # print(current_wallpaper)
        # overlayed_wallpaper = overlay_wallpaper(current_wallpaper,color.getRgb()) 
       	# temp_path_sim = [overlayed_wallpaper]

        # saves = POST_data(temp_path_sim,cu.dummy_data,10) #file_paths , data , time_interval
        # cu.dump_data(active_profile,saves)

        # self.set_upcoming_wallpaper()




        if self.color_overlay.isValid():
            #print(color.name())
            self.ui.overlay_color_btn.setStyleSheet("\n"
                "border:2px solid #44475a;\n"
                "border-radius:25px;\n"
                f"background:{self.color_overlay.name()};")



    def do_overlay(self):
        color = self.color_overlay

        opacity = self.ui.overylay_percentage_slider.value()


        masked_opacities = color.getRgb()
        masked_opacity = (masked_opacities[0],masked_opacities[1],masked_opacities[2],opacity)


        active_profile = self.data["active_profile"]

        current_wallpaper = self.data[active_profile]["file_path"]

        overlayed_wallpaper = overlay_wallpaper(current_wallpaper,masked_opacity) 
       	temp_path_sim = [overlayed_wallpaper]

       	bruh = color.getRgb()

        saves = POST_data(temp_path_sim,cu.dummy_data,10) #file_paths , data , time_interval
        cu.dump_data(active_profile,saves)

        self.set_upcoming_wallpaper()







    def clear_wcuser_profile(self):

        total_items_count = self.ui.select_profile_combo.count()
        context = self.ui.select_profile_combo.currentText()

        for count in range(total_items_count):
            if context == None or context == "":
                self.ui.select_profile_combo.removeItem(count)
            else:
                pass



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
    myapp = Switchium_Main_Window()

    myapp.show()
    sys.exit(app.exec_())

