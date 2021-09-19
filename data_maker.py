
import glob
import os
from pprint import pprint
import CoreUtils as cu




#selected_file_path = input("path : ")


data= {
			"mode": "single",
			"file_name": "horahora.jpg",
			"file_size": "129KB",
			"file_path": "hora",
			"set_time": 10,
			"instant_skip": True
	}



dirs = ['D:/py_codes/Ashen Transistor/changebg.py', 'D:/py_codes/Ashen Transistor/damnit.py', 'D:/py_codes/Ashen Transistor/data_maker.py', 'D:/py_codes/Ashen Transistor/get_date.py']

def POST_data(selected_file_path,data,interval):
	#check_directory = len(selected_file_path) <= 1

	if not len(selected_file_path) <= 1:
		file_paths = selected_file_path
		data["mode"] = "multiple"
		data["file_path"] = file_paths
		data["set_time"] = interval
	else:
		data["file_path"] = selected_file_path[0]
		data["set_time"] = interval
	
	return data






	