from tkinter import *
import webbrowser

def display():
    print("Students Name:",name.get())
    if name.get() == "Sameed":
        profile = Label(tkWindow, text="Student's Profile",fg="blue",font="Arial")
        profile.place(x=90, y=320)
        lbl = Label(tkWindow, text="Student's Roll No :")
        lbl.place(x=50, y=350)
        roll_n = Label(tkWindow, text="2022F-BSE-128")
        roll_n.place(x=200, y=350)
        lbl4 = Label(tkWindow, text="Student's Father name :")
        lbl4.place(x=50, y=370)
        fname = Label(tkWindow, text="Imran Ahmed")
        fname.place(x=200, y=370)
        lbl2 = Label(tkWindow, text="Student's Batch Year")
        lbl2.place(x=50, y=390)
        batch_n = Label(tkWindow, text="2022-Fall")
        batch_n.place(x=200, y=390)
        lbl3 = Label(tkWindow, text="Status:")
        lbl3.place(x=50, y=410)
        status = Label(tkWindow, text="Active")
        status.place(x=200, y=410)
        def Sameedpdf():
            webbrowser.open_new(r'file:///C:/Users/sonu%20computers/Desktop/PFUND%20LAB/1st%20Semester%20Project(CMS)/Admit(sam).pdf')
            
        #Aiman
    elif name.get() == "Aiman":
        profile = Label(tkWindow, text="Student's Profile",fg="blue",font="Arial")
        profile.place(x=90, y=320)
        lbl = Label(tkWindow, text="Student's Roll No :")
        lbl.place(x=50, y=350)
        roll_n = Label(tkWindow, text="2022F-BSE-127")
        roll_n.place(x=200, y=350)
        lbl4 = Label(tkWindow, text="Student's Father name :")
        lbl4.place(x=50, y=370)
        fname = Label(tkWindow, text="Imran Ahmed")
        fname.place(x=200, y=370)
        lbl2 = Label(tkWindow, text="Student's Batch Year")
        lbl2.place(x=50, y=390)
        batch_n = Label(tkWindow, text="2022-Fall")
        batch_n.place(x=200, y=390)
        lbl3 = Label(tkWindow, text="Status:")
        lbl3.place(x=50, y=410)
        status = Label(tkWindow, text="Active")
        status.place(x=200, y=410)
        def Aimanpdf():
            webbrowser.open_new(r'file:///C:/Users/sonu%20computers/Desktop/PFUND%20LAB/1st%20Semester%20Project(CMS)/Admit(Aim).pdf')
        #Maaz
    elif name.get() == "Maaz":
        profile = Label(tkWindow, text="Student's Profile",fg="blue",font="Arial")
        profile.place(x=90, y=320)
        lbl = Label(tkWindow, text="Student's Roll No :")
        lbl.place(x=50, y=350)
        roll_n = Label(tkWindow, text="2022F-BSE-111")
        roll_n.place(x=200, y=350)
        lbl4 = Label(tkWindow, text="Student's Father name :")
        lbl4.place(x=50, y=370)
        fname = Label(tkWindow, text="Hussain")
        fname.place(x=200, y=370)
        lbl2 = Label(tkWindow, text="Student's Batch Year")
        lbl2.place(x=50, y=390)
        batch_n = Label(tkWindow, text="2022-Fall")
        batch_n.place(x=200, y=390)
        lbl3 = Label(tkWindow, text="Status:")
        lbl3.place(x=50, y=410)
        status = Label(tkWindow, text="Active")
        status.place(x=200, y=410)
        def Maazpdf():
            webbrowser.open_new(r'file:///C:/Users/sonu%20computers/Desktop/PFUND%20LAB/1st%20Semester%20Project(CMS)/Admit(Maaz).pdf')
        #Ayaan
    elif name.get() == "Ayaan":
        profile = Label(tkWindow, text="Student's Profile",fg="blue",font="Arial")
        profile.place(x=90, y=320)
        lbl = Label(tkWindow, text="Student's Roll No :")
        lbl.place(x=50, y=350)
        roll_n = Label(tkWindow, text="2022F-BSE-118")
        roll_n.place(x=200, y=350)
        lbl4 = Label(tkWindow, text="Student's Father name :")
        lbl4.place(x=50, y=370)
        fname = Label(tkWindow, text="Jawaid")
        fname.place(x=200, y=370)
        lbl2 = Label(tkWindow, text="Student's Batch Year")
        lbl2.place(x=50, y=390)
        batch_n = Label(tkWindow, text="2022-Fall")
        batch_n.place(x=200, y=390)
        lbl3 = Label(tkWindow, text="Status:")
        lbl3.place(x=50, y=410)
        status = Label(tkWindow, text="In-Active")
        status.place(x=200, y=410)
        def Ayaanpdf():
            webbrowser.open_new(r'file:///C:/Users/sonu%20computers/Desktop/PFUND%20LAB/1st%20Semester%20Project(CMS)/Admit(ayaan).pdf')
        #Nabeera
    elif name.get() == "Nabeera":
        profile = Label(tkWindow, text="Student's Profile",fg="blue",font="Arial")
        profile.place(x=90, y=320)
        lbl = Label(tkWindow, text="Student's Roll No :")
        lbl.place(x=50, y=350)
        roll_n = Label(tkWindow, text="2022F-BSE-301")
        roll_n.place(x=200, y=350)
        lbl4 = Label(tkWindow, text="Student's Father name :")
        lbl4.place(x=50, y=370)
        fname = Label(tkWindow, text="Siddiqui")
        fname.place(x=200, y=370)
        lbl2 = Label(tkWindow, text="Student's Batch Year")
        lbl2.place(x=50, y=390)
        batch_n = Label(tkWindow, text="2022-Fall")
        batch_n.place(x=200, y=390)
        lbl3 = Label(tkWindow, text="Status:")
        lbl3.place(x=50, y=410)
        status = Label(tkWindow, text="In-Active")
        status.place(x=200, y=410)
        def Nabeerapdf():
            webbrowser.open_new(r'file:///C:/Users/sonu%20computers/Desktop/PFUND%20LAB/1st%20Semester%20Project(CMS)/Admit(nab).pdf')
            
    if name.get()=="Sameed":        
        pdfButton = Button(tkWindow, text="Print Admit Card",fg="white",bg="#A020F0", command=Sameedpdf)
        pdfButton.place(x=115, y=435)
    elif name.get()=="Aiman":        
        pdfButton = Button(tkWindow, text="Print Admit Card",fg="white",bg="#A020F0", command=Aimanpdf)
        pdfButton.place(x=115, y=435)
    elif name.get()=="Maaz":        
        pdfButton = Button(tkWindow, text="Print Admit Card",fg="white",bg="#A020F0", command=Maazpdf)
        pdfButton.place(x=115, y=435)
    elif name.get()=="Ayaan":        
        pdfButton = Button(tkWindow, text="Print Admit Card",fg="white",bg="#A020F0", command=Ayaanpdf)
        pdfButton.place(x=115, y=435)
    elif name.get()=="Nabeera":        
        pdfButton = Button(tkWindow, text="Print Admit Card",fg="white",bg="#A020F0", command=Nabeerapdf)
        pdfButton.place(x=115, y=435)
    return
#window
tkWindow = Tk()  
tkWindow.geometry('350x530')  
tkWindow.title('Welcome')
photo = PhotoImage(file = "ssuet1.png")

#LAbel 01
lbl=Label(tkWindow, image = photo).pack(side=TOP, pady= 10)

welcomeLabel = Label(tkWindow, text="Welcome to CMS Portal",fg="green",font="Arial")
welcomeLabel.place(x=60, y=180)

#name label and text entry box
nameLabel = Label(tkWindow, text="Enter Student's Name :")
nameLabel.place(x=30, y=220)
name = StringVar()
nameEntry = Entry(tkWindow, textvariable=name, bd=5)
nameEntry.place(x=180, y=220)

#surname label and password entry box
surnameLabel = Label(tkWindow,text="Enter Student's surname :")
surnameLabel.place(x=30, y=250)
surname = StringVar()
fnameEntry = Entry(tkWindow, textvariable=surname, bd=5)
fnameEntry.place(x=180, y=250)

#login button
submitButton = Button(tkWindow, text="Submit",fg="white",bg="#A020F0", command=display)
submitButton.place(x=220, y=280)

tkWindow.mainloop()


