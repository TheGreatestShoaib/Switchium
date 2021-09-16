
import CoreUtils as cu
import time

edata = {

        "mode": "multiple",
        "file_name": "horahora.jpg",
        "file_size": "129KB",
        "file_path": ["bruh.jpg","wallpaper.jpg","haha.jpeg"],
        "set_time": "",
        "instant_skip": False
}

cu.dump_data("test_profile",edata)

data = cu.find_key()



for prof in data.keys():
	mode_name =  cu.find_key(profile_name=prof,key_name="mode")
	if mode_name == "single":
		pass
	else:
		paths = cu.find_key(profile_name=prof,key_name="file_path")
		for path in paths:
			print(path)
			time.sleep(1)

	print()