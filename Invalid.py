from tkinter import *

tkWindow = Tk()  
tkWindow.geometry('500x150')  
tkWindow.title('Alert!')

label = Label(tkWindow, text="The Username and Password you entered is Invalid!", font="Arial")
label.place(x=60,y=30)

label = Label(tkWindow, text="The Program is Over!, Thanks for your time", font="calibri")
label.place(x=90,y=60)

button = Button(tkWindow, text="Quit",height=1, width=5,fg="white",bg="blue",font="Arial", command=quit)
button.place(x=220,y=90)

tkWindow.mainloop()