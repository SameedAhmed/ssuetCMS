from tkinter import *
from functools import partial

def qrgenerator():
	from PIL import Image
	img = Image.open("qrcode.png")
	img.show()
	return

#window
tkWindow = Tk()  
tkWindow.geometry('350x350')  
tkWindow.title('CMS generate')
photo = PhotoImage(file = "ssuet1.png")
#LAbel 01
lbl=Label(tkWindow, image = photo).pack(side=TOP, pady= 10)

welcomeLabel = Label(tkWindow, text="QR Generator",fg="blue",font="Arial")
welcomeLabel.place(x=110, y=180)
#question label and text entry box
questionLabel = Label(tkWindow, text="Do you want to generate a QR Code?")
questionLabel.place(x=70, y=220)

#click label and click entry box
clickLabel = Label(tkWindow,text="Click on the generate button below :)")
clickLabel.place(x=70, y=240)

#generate button
generateButton = Button(tkWindow, text="Generate",bg="#A020F0",fg="white", command=qrgenerator)
generateButton.place(x=140, y=280)

tkWindow.mainloop()

