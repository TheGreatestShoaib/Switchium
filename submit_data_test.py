import CoreUtils as Cu
import data_maker

path = "wallpapers/arch.png"

profile_name = "new__test22"
dumpable_data = data_maker.POST_data(path, data_maker.data )


cu.dump_data(profile_name,dumpable_data)