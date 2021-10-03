
#from CoreUtils.platform_info import ult_screensize

from PIL import Image, ImageDraw
import uuid


def create_solid_wallpaper(screensize,rgb_value):
    img = Image.new('RGB',screensize, rgb_value)
    path = f"temp/{uuid.uuid4()}.png"
    img.save(path)
    return path 
    




