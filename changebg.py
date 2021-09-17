import CoreUtils as cu
import time
import ctypes
import time

def change(path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)

data = cu.find_key()

profile = data["active_profile"]
paper_plot = data[profile]["mode"]

def change_wallpaper():
	active_profile = data["active_profile"]
	if data[active_profile]["mode"] != "single":
		wallpaper_path = data[active_profile]["file_path"]
		interval = data[active_profile]["set_time"]
		for wallpaper in wallpaper_path:
			time.sleep(interval)
			change(wallpaper)


def change_single_wallpaper():
	active_profile = data["active_profile"]
	path = data[active_profile]["file_path"]
	change(path)