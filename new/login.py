import sys

import tkinter as tk
from tkinter import messagebox  # import this to fix messagebox error
import sqlite3
import mapviewer

# initialize
def create_table():
    with sqlite3.connect("userinfo.db") as db:
        sql = """create table Userinfo
            (UserID integer,
            Username text,
            Password text,
            Map text,
            primary key(UserID))"""
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
def create_currentuser_table():
    try:            
        with sqlite3.connect("Userinfo.db") as db:
            cursor = db.cursor()
            sql = "DROP TABLE Current;"
            cursor.execute(sql)
    except:
        pass
    with sqlite3.connect("userinfo.db") as db:
        sql = """create table Current
            (Username text,
            Map text)
            """
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()

    

def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    with sqlite3.connect("userinfo.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("select UserID, Username, Password, Map from Userinfo where Username=?",(usr_name,))
        userinfo = cursor.fetchone()
        db.commit()
    if userinfo is None:
        is_sign_up = tk.messagebox.askyesno('Welcome',
               'You have not signed up yet. Sign up today?')
        if is_sign_up:
            usr_sign_up()
    else:
        if usr_pwd == userinfo[2]:
            tk.messagebox.showinfo(title='Welcome', message=usr_name)            
            with sqlite3.connect("userinfo.db") as db:
                cursor = db.cursor()
                sql = "insert into Current (Username, Map) values (?,?)"
                values=(userinfo[1], userinfo[3])
                cursor.execute(sql,values)
                db.commit()
            window.destroy()
            mapviewer.main()
        else:
            tk.messagebox.showerror(message='Error, your password is wrong, try again.')

def select_all_users():
    with sqlite3.connect("userinfo.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from Userinfo order by UserID")
        users = cursor.fetchall()
        db.commit()
        return users
    
def usr_sign_up():
    def sign_to_Python():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
        with sqlite3.connect("userinfo.db") as db:
            if np != npf:
                tk.messagebox.showerror('Error', 'Password and confirm password must be the same!')
            elif np==npf:
                with sqlite3.connect("userinfo.db") as db:
                    cursor = db.cursor()
                    cursor.execute("PRAGMA foreign_keys = ON")
                    cursor.execute("select UserID, Username, Password, Map from Userinfo where Username=?",(nn,))
                    userinfo = cursor.fetchone()
                    db.commit()
                if userinfo == None:
                    with sqlite3.connect("userinfo.db") as db:
                        cursor = db.cursor()
                        cursor.execute("PRAGMA foreign_keys = ON")
                        sql = "insert into Userinfo (UserID, Username, Password, Map) values (?,?,?,?)"
                        users=select_all_users()
                        values=(len(users)+1, nn, np, "")
                        cursor.execute(sql,values)
                        db.commit()
                    tk.messagebox.showinfo('Welcome', 'You have successfully signed up!')
                else:
                    tk.messagebox.showerror('Error', 'The user has already signed up!')
                window_sign_up.destroy()

            
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('Sign up window')

    new_name = tk.StringVar()
    new_name.set('example@python.com')
    tk.Label(window_sign_up, text='User name: ').place(x=10, y= 10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150, y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password: ').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm password: ').place(x=10, y= 90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=150, y=90)

    btn_comfirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_Python)
    btn_comfirm_sign_up.place(x=150, y=130)


    

try:
    create_table()
except:
    pass


try:
    create_currentuser_table()
except:
    pass

window = tk.Tk()
window.title('Welcome to underground path finder')
window.geometry('450x300')

# welcome image
canvas = tk.Canvas(window, height=200, width=500)
image_file = tk.PhotoImage(file='welcome.gif')
image = canvas.create_image(0,0, anchor='nw', image=image_file)
canvas.pack(side='top')

# user information
tk.Label(window, text='User name: ').place(x=50, y= 150)
tk.Label(window, text='Password: ').place(x=50, y= 190)

var_usr_name = tk.StringVar()
var_usr_name.set('example@python.com')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=150)
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=190)
# login and sign up button
btn_login = tk.Button(window, text='Login', command=usr_login)
btn_login.place(x=170, y=230)
btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=270, y=230)

window.mainloop()


