#!/usr/bin/env python

from PyQt5.QtWidgets import QApplication, QWidget , QInputDialog, QLineEdit, QFileDialog ,QColorDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from src import Ui_MainWindow


import Switchium as cu
from data_maker import *
from Switchium.platform_info import ult_screensize


from Switchium.create_wallpaper import create_solid_wallpaper,overlay_wallpaper


import sys
import json
import random


sys.setrecursionlimit(100000)

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
        self.show_allowed_extensions()
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
        self.ui.filter_ext_combo.currentIndexChanged.connect(self.show_cleaned_allowed_extensions)



        #self.clicked = False
        self.ui.frame_2.clicked = False

        self.ui.time_set_combo.addItem("30 Sec","30")
        self.ui.time_set_combo.addItem("1 Min","60")

        self.ui.time_set_combo.addItem("2 Min","160")
        self.ui.time_set_combo.addItem("15 Min","900")
        self.ui.time_set_combo.addItem("10 Min","1800")

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
        # with open("data/_paperDetails_update.json") as f:
        #     data = json.load(f)

        data = cu.RAW_DATA()
       
        
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
            

            data = cu.RAW_DATA()

            
            if profile_name_text:
                data["active_profile"] = self.ui.select_profile_combo.currentText()
            else:
                pass

            active_profile = data["active_profile"]
            mode = data[active_profile]["mode"]
            
            cu.dump_data("active_profile",data["active_profile"])

            data["last_wallpaper"] = data[active_profile]["file_path"][3]
            
            cu.dump_data("last_wallpaper",data["last_wallpaper"])


            self.clear_wcuser_profile()
            self.set_upcoming_wallpaper()
            #self.set_upcoming_wallpaper()

        except:
            pass



        
   
    def dialog(self):

        data = cu.RAW_DATA()

        options = QFileDialog.Options()
        files, _ =  QFileDialog.getOpenFileNames(self,"Select Files", "","All Files (*)", options=options)
        print(files)
        time_interval = self.ui.time_set_combo.currentText()
        active_profile = self.ui.select_profile_combo.currentText()
        key_name = data[active_profile]
        
        if files:
                saves = POST_data(files,cu.dummy_data,time_interval) #file_paths , data , time_interval
                cu.dump_data(active_profile,saves)
                self.ui.label.setText( "/".join(files[0].split("/")[:-1] )) 
                if len(files) <= 1:
                    self.hide_single_stuffs()
                    self.ui.label.setText(files[0])


                self.set_upcoming_wallpaper()





    def set_upcoming_wallpaper(self):
        # with open("data/_paperDetails_update.json") as f:
        #     data = json.load(f)


        data = cu.RAW_DATA()

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

        data = cu.RAW_DATA()

        color = QColorDialog.getColor()
        active_profile = data["active_profile"]
   
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

        data = cu.RAW_DATA()

        color = self.color_overlay

        opacity = self.ui.overylay_percentage_slider.value()


        masked_opacities = color.getRgb()
        masked_opacity = (masked_opacities[0],masked_opacities[1],masked_opacities[2],opacity)


        active_profile = data["active_profile"]

        current_wallpaper = data[active_profile]["file_path"]

        overlayed_wallpaper = overlay_wallpaper(current_wallpaper,masked_opacity) 
       	temp_path_sim = [overlayed_wallpaper]

       	bruh = color.getRgb()

        saves = POST_data(temp_path_sim,cu.dummy_data,10) #file_paths , data , time_interval
        cu.dump_data(active_profile,saves)

        self.set_upcoming_wallpaper()


    def disable_single_mode(self):
        self.ui.next_wallpaper.setEnabled(False)
        self.ui.preview_text_label1_2.setEnabled(False)

        #disable Others

        self.ui.img_ratio_combo.setEnabled(True)
        self.ui.solid_back_color_btn.setEnabled(True)
        self.ui.overlay_color_btn.setEnabled(True)
        self.ui.show_preview_btn.setEnabled(True)
        self.ui.overylay_percentage_slider.setEnabled(True)

    def disable_mult_mode(self):
        self.ui.img_ratio_combo.setEnabled(False)
        self.ui.solid_back_color_btn.setEnabled(False)
        self.ui.overlay_color_btn.setEnabled(False)
        self.ui.show_preview_btn.setEnabled(False)
        self.ui.overylay_percentage_slider.setEnabled(False)



    def filter_extensions(self):
        pass


    def show_cleaned_allowed_extensions(self):

        if self.ui.filter_ext_combo is None:
            self.ui.filter_ext_combo.clear()
        else:
            pass

        self.show_allowed_extensions()





    def show_allowed_extensions(self):
        

        allowed_ext = ["svg","ico","gif","png","jpg","jpeg"]

        #filtered_exts = config.keys()

        filtered_exts = ["svg","ico"]

        for ext in allowed_ext:
            if ext not in filtered_exts:
                self.ui.filter_ext_combo.addItem(str(ext))


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
            self.move(self.pos().x() - round(dx), self.pos().y() - round(dy) ) 
        self.old_pos = event.screenPos() 
        #self.clicked = True
        self.ui.frame_2.clicked = True

        

        return QWidget.mouseMoveEvent(self, event)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Switchium_Main_Window()

    myapp.show()
    sys.exit(app.exec_())

