

from Switchium.update_data import *

dummy_data = {
	"mode": "",
    "file_path": "",
    "set_time": "",
    "instant_skip":" "
}


def RAW_DATA():
    with open("Switchium/_paperDetails_update.json") as f:
        data = json.load(f)

    return data
