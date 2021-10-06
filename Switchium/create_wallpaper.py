
#from CoreUtils.platform_info import ult_screensize

from PIL import Image, ImageDraw
import uuid

#path = ""


def create_solid_wallpaper(screensize,rgb_value):
    img = Image.new('RGBA',screensize, rgb_value)
    path = f"temp/{uuid.uuid4()}.png"
    img.save(path)
    return path 
    

def overlay_wallpaper(main_wallpaper,rgb_value):
   

    background = Image.open(main_wallpaper)

    width,height = background.size

    overylayed_paper = create_solid_wallpaper((width,height),rgb_value)
    
    foreground = Image.open(overylayed_paper)
   
    path = f"temp/{uuid.uuid4()}.png"
    
    background.paste(foreground, (0, 0), foreground)
    background.save(path)

    return path

