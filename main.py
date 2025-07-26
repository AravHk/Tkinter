import tkinter
from tkinter import messagebox
#pack,place and grid
#label.pack()
#label.grid(row = 0,column = 0)
window = tkinter.Tk()
window.title("Login form")
window.geometry('340x440')
window.configure(bg = '#333333')

def login():
    username = "JohnDoe"
    password = "JohnDoe123$"
    if username_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo(title = "Login Success",message = "Successfully logged in")
    else:
        messagebox.showerror(title = "Login Failed",message = "Invalid Username or Password")
frame = tkinter.Frame(bg = '#333333')

#creating widgets
login_label = tkinter.Label(frame ,text = 'Login',bg = '#333333',fg = 'yellow',font = ('ApercuExtraBold',30))
username_label = tkinter.Label(frame,text = 'Username',bg = '#333333',fg = '#FFFFFF',font = ('ApercuExtraBold',16))
password_label = tkinter.Label(frame,text = 'Password',bg = '#333333',fg = '#FFFFFF',font = ('ApercuExtraBold',16))
username_entry = tkinter.Entry(frame,font = ('ApercuExtraBold',16))
password_entry = tkinter.Entry(frame,show = '*',font = ('ApercuExtraBold',16))
login_btn = tkinter.Button(frame,text = 'Login',bg = 'yellow',fg = '#333333',font = ('ApercuExtraBold',16),command = login)

#placing widgets
login_label.grid(row = 0,column = 0,columnspan = 2,sticky = "news",pady =40)
username_label.grid(row = 1,column = 0 , pady = 20)
username_entry.grid(row = 1,column = 1)
password_label.grid(row = 2,column = 0,pady = 20)
password_entry.grid(row = 2,column = 1)
login_btn.grid(row = 3,column = 0,columnspan =2,pady = 30)
frame.pack()
window.mainloop()


