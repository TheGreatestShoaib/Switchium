
import time
import json
from pprint import pprint

with open("_paperDetails.json") as f:
	data = json.load(f)


pprint(data["profile2"]["file_path"])

inp = input("select profile: ")


if data[inp]["mode"] == "multiple":
	for x in data[inp]["file_path"]:
		print(x)
		time.sleep(1)
else:
	pass