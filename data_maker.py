
import glob
import os
from pprint import pprint
import CoreUtils as cu

def directory_scrapper(selected_file_path):
	allowed_extensions= ['/*.jpg', '/*.png']
	file_paths = []
	
	for ext in allowed_extensions:
		files = glob.glob(selected_file_path+ext)
		file_paths.extend(files)
	
	for f in range(len(file_paths)):
		file_paths[f] = os.path.abspath(file_paths[f])

	return file_paths




#selected_file_path = input("path : ")


data= {
			"mode": "single",
			"file_name": "horahora.jpg",
			"file_size": "129KB",
			"file_path": "hora",
			"set_time": 10,
			"instant_skip": True
	}


def POST_data(selected_file_path,data):

	check_directory = os.path.isdir(selected_file_path)

	if check_directory:
		file_paths = directory_scrapper(selected_file_path)
		data["mode"] = "multiple"
		data["file_path"] = file_paths
	else:
		data["file_path"] = os.path.abspath(selected_file_path)
	
	return data






	