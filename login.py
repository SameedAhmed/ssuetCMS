from tkinter import *
from functools import partial

def validateLogin():
	print("username entered :", username.get())
	print("password entered :", password.get())
	return

#window
tkWindow = Tk()  
tkWindow.geometry('360x330')  
tkWindow.title('CMS Login')
photo = PhotoImage(file = "ssuet1.png")
#LAbel 01
lbl=Label(tkWindow, image = photo).pack(side=TOP, pady= 10)

welcomeLabel = Label(tkWindow, text="Portal Sign-in",fg="green",font="Arial")
welcomeLabel.place(x=150, y=180)
#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name")
usernameLabel.place(x=70, y=210)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username, bd=5)
usernameEntry.place(x=150, y=210)

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password")
passwordLabel.place(x=70, y=240)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*', bd=5)
passwordEntry.place(x=150, y=240)

#validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login",bg="#A020F0",fg="white", command=validateLogin)
loginButton.place(x=190, y=270)

tkWindow.mainloop()
