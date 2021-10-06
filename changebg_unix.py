



import json
import os
from Switchium.which_distro import distro
from Switchium.platform_info import stdout_control

gnome = "gsettings set org.gnome.desktop.background picture-uri " # + add path justi

cinnamon = "org.cinnamon.desktop.background picture-uri 'path'" # add path with  fstring  replacing 'path'

kde= " qdbus org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript \"var allDesktops = desktops();print (allDesktops);for (i=0;i<allDesktops.length;i++) {d = allDesktops[i];d.wallpaperPlugin = 'org.kde.image';d.currentConfigGroup = Array('Wallpaper', 'org.kde.image', 'General');d.writeConfig('Image', 'file:///home/zero/Pictures/Wallpapers/wallpaper.png')}\""




kde = ""

xfce = ""




with open('Switchium/_paperDetails_update.json',) as f:
    data = json.load(f)


active_profile = data["active_profile"]
last_wallpaper = data["last_wallpaper"]
path = data[active_profile]["file_path"]

username = stdout_control("whoami")

path = path.split(username)[1]

def change_wallpaper(distro,path,stng):
    
    if distro == "gnome":
        os.system(stng+"~/"+path)
        

distro_name = distro()


change_wallpaper(distro_name,path,gnome)



