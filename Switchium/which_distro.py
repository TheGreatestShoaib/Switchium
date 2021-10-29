

import os


session_name = os.environ['XDG_CURRENT_DESKTOP']


#print(session_name)


gnome = ['gnome','nome',"GNOME"]
kde = ['kde-plasma','kde','plasma']
xfce = ['xfce4','xfce','xubuntu']
cinnamon = ["cinnamon","X-Cinnamon"]


def distro():
    
    if session_name in gnome:
        return 'gnome'
    
    elif session_name in kde:
        return 'kde'
    
    elif session_name in cinnamon:
        return 'cinnamon'
    
    elif session_name in xfce:
        return 'xfce'

    return None



