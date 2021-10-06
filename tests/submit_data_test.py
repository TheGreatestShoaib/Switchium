import CoreUtils as Cu
import data_maker

path = "wallpapers"

profile_name = "dir_test"
dumpable_data = data_maker.POST_data(path, data_maker.data )


Cu.dump_data(profile_name,dumpable_data)