
import os
from Switchium.which_distro import distro
from Switchium.platform_info import stdout_control

#useless commands

#gnome = "gsettings set org.gnome.desktop.background picture-uri " # + add path justi
#cinnamon = "org.cinnamon.desktop.background picture-uri 'path'" # add path with  fstring  replacing 'path'
#kde= " qdbus org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript \"var allDesktops = desktops();print (allDesktops);for (i=0;i<allDesktops.length;i++) {d = allDesktops[i];d.wallpaperPlugin = 'org.kde.image';d.currentConfigGroup = Array('Wallpaper', 'org.kde.image', 'General');d.writeConfig('Image', 'file:///home/zero/Pictures/Wallpapers/wallpaper.png')}\""
#xfce = "xfconf-query --channel xfce4-desktop --property /backdrop/screen0/monitor0/image-path --set "
# username = stdout_control("whoami")
#dconf write "/org/gnome/desktop/background/picture-uri" "'file:///home/shoaib/py_codes/switchium/wallpapers/arch.png'"
#path = f"'{'file://'+os.path.abspath('Wallpapers/arch.png')}'"




path = 'file://'+os.path.abspath('wallpapers/arch.png')

def change_wallpaper(distro,path):
    
    if distro == "gnome":    
        gnome_wp_chng_cmd = f"dconf write \"/org/gnome/desktop/background/picture-uri\" \"'{path}'\""
        print(gnome_wp_chng_cmd)
        os.system(gnome_wp_chng_cmd)

    if distro == "kde":
        kde_wp_chng_cmd = "qdbus org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript \"var allDesktops = desktops();print (allDesktops);for (i=0;i<allDesktops.length;i++) {d = allDesktops[i];d.wallpaperPlugin = 'org.kde.image';d.currentConfigGroup = Array('Wallpaper', 'org.kde.image', 'General');d.writeConfig('Image', '"+path+"')}\""
        os.system(kde_wp_chng_cmd)
    
    if distro == "xfce":
        xfce = f"xfconf-query --channel xfce4-desktop --property /backdrop/screen0/monitor0/image-path --set {path}"
        os.system(xfce_wp_chng_cmd)
 
    if distro == "cinnamon":
        cinnamon = f"org.cinnamon.desktop.background picture-uri {path}"
        os.system(cinnamon_wp_chng_cmd)

        




