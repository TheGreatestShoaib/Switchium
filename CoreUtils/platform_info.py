
from subprocess import Popen, PIPE
import platform


unix_screen_size = "xrandr | grep '*' | cut -d' ' -f 4"


# def stdout_control(cmd):
# 	output = Popen(cmd,shell=True, stdout=PIPE).communicate()[0]
# 	return output.decode().strip()



def win_screensize():
	import ctypes
	user32 = ctypes.windll.user32
	screensize =  ( user32.GetSystemMetrics(0), user32.GetSystemMetrics(1) )
	return screensize




def unix_screensize(cmd):
	raw_size = Popen(cmd,shell=True, stdout=PIPE).communicate()[0].decode().strip()
	size = raw_size.split("x")

	return (size[0],size[1])


def ult_screensize():
	if platform.system() == "Linux":
		return unix_screensize(unix_screen_size)

	return win_screensize()

