from tkinter import *

tkWindow = Tk()  
tkWindow.geometry('400x140')  
tkWindow.title('Alert!')

#label = Label(tkWindow, text="The Username and Password you entered is Invalid!", font="Arial")
#label.place(x=50,y=50)

label = Label(tkWindow, text="The Program is Over!, Thanks for your time", font="calibri")
label.place(x=50,y=30)

button = Button(tkWindow, text="Quit",height=1, width=5,fg="white",bg="blue",font="Arial", command=quit)
button.place(x=170,y=70)

tkWindow.mainloop()
