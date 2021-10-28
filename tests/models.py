
import sqlite3


def create_user(username):
    conn = sqlite3.connect("lst_users.db")
    c = conn.cursor()
    
    c.execute("""CREATE TABLE new_usr (
            wallpaper text
    )""")


    conn.commit()
    conn.close()



create_user("new_user")

