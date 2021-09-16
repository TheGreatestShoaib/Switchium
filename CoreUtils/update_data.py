

import json


def find_key(profile_name=None,key_name=None):
        with open("CoreUtils/_paperDetails_update.json") as f:
                data = json.load(f)

        if profile_name is not None and key_name is not None:
                return data[profile_name][key_name]
        elif profile_name is not None:
                return data[profile_name]


        return data







def dump_data(key_name,entry_data):
        with open("CoreUtils/_paperDetails_update.json") as f:
                data = json.load(f)

        data[key_name] = entry_data

        with open("CoreUtils/_paperDetails_update.json","w") as f:
        	json.dump(data,f,indent=2)

