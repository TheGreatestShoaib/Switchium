
import json 
import os
import glob


def dump_json(json_obj,file):
	with open(file,"w") as f:
		json.dump(json_obj,f)


data_file = open("_paperDetails.json","r").read()
data = json.load(data_file)
data_file.close()


print(data)