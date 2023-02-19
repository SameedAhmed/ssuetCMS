lista = ["Sameed","Aiman","Nabeera","Maaz","Ayaan"]
surname = ["Ahmed","Siddiqui","Hussain","Jawaid","Fatima"]
print ("\t\"Welcome To CMS Portal\"")
import login
user = login.username.get()
pass_word = login.password.get()
if user=="ssuet22" and pass_word=="admin":
    import Intro
    x = Intro.name.get()
    s = Intro.surname.get()
    while True:
        if x in lista and s in surname:
            print("Student's Name:",x)
            #Sameed Ahmed Data
            if x=="Sameed":
                w = str(input("\nDo you want to calculate the GPA of the student?"))
                gpa = w.lower()
                if gpa=="yes":
                    import gpa_calculator
                    s = str(input("\nDo you want to calculate the attendance of the student?"))
                    att = s.lower()
                    if att=="yes":
                        import Attendance_Calculator
                        r = str(input("\nDo you want to generate a qrcode in order to download all these documents?"))
                        qr = r.lower()
                        if qr=="yes":
                            from qr_code import Sameed
                            Sameed()
                            import qrcode_generate
                            break
                        elif qr!="yes":
                            print("Thank You!")
                            break
                    elif att!="yes":
                      print("Thank You!")
                      break
                elif gpa!="yes":
                    print("Thank You!")
                    break
                
            #Aiman Fatima Data
            elif x=="Aiman":
                h = str(input("\nDo you want to calculate the GPA of the student?"))
                gpa = h.lower()
                if gpa=="yes":
                    import gpa_calculator
                    s = str(input("\nDo you want to calculate the attendance of the student?"))
                    att = s.lower()
                    if att=="yes":
                        import Attendance_Calculator
                        r = str(input("\nDo you want to generate a qrcode in order to download all these documents?"))
                        qr = r.lower()
                        if qr=="yes":
                            from qr_code import Aiman
                            Aiman()
                            import qrcode_generate
                            break
                        elif qr!="yes":
                            print("Thank You!")
                            break
                    elif att!="yes":
                      print("Thank You!")
                      break
                elif gpa!="yes":
                    print("Thank You!")
                    break
            
            #Nabeera Siddiqui Data
            elif x=="Nabeera":
                k = str(input("\nDo you want to calculate the GPA of the student?"))
                gpa = k.lower()
                if gpa=="yes":
                    import gpa_calculator
                    s = str(input("\nDo you want to calculate the attendance of the student?"))
                    att = s.lower()
                    if att=="yes":
                        import Attendance_Calculator
                        r = str(input("\nDo you want to generate a qrcode in order to download all these documents?"))
                        qr = r.lower()
                        if qr =="yes":
                            from qr_code import nabeera
                            nabeera()
                            from PIL import Image
                            img = Image.open("qrcode.png")
                            img.show()
                            break
                        elif qr!="yes":
                            print("Thank You!")
                            break
                    elif att!="yes":
                      print("Thank You!")
                      break
                elif gpa!="yes":
                    print("Thank You!")
                    break
            
            #MAAZ HUSSAIN DATA
            elif x=="Maaz":
                q = str(input("\nDo you want to calculate the GPA of the student?"))
                gpa = q.lower()
                if gpa=="yes":
                    import gpa_calculator
                    s = str(input("\nDo you want to calculate the attendance of the student?"))
                    att = s.lower()
                    if att=="yes":
                        import Attendance_Calculator
                        r = str(input("\nDo you want to generate a qrcode in order to download all these documents?"))
                        qr = r.lower()
                        if qr=="yes":
                            from qr_code import Maaz
                            Maaz()
                            import qrcode_generate
                            break
                        elif qr!="yes":
                            print("Thank You!")
                            break
                    elif att!="yes":
                      print("Thank You!")
                      break
                elif gpa!="yes":
                    print("Thank You!")
                    break
            
            #AYAAN JAWAID DATA
            elif x=="Ayaan":
                t = str(input("\nDo you want to calculate the GPA of the student?"))
                gpa = t.lower()
                if gpa=="yes":
                    import gpa_calculator
                    s = str(input("\nDo you want to calculate the attendance of the student?"))
                    att = s.lower()
                    if att=="yes":
                        import Attendance_Calculator
                        r = str(input("\nDo you want to generate a qrcode in order to download all these documents?"))
                        qr = r.lower()
                        if qr=="yes":
                            from qr_code import Ayaan
                            Ayaan()
                            import qrcode_generate
                            break
                        elif qr!="yes":
                            print("Thank You!")
                            break
                    elif att!="yes":
                      print("Thank You!")
                      break
                elif gpa!="yes":
                    print("Thank You!")
                    break
        #Not IN       
        elif x not in lista:
            d=str(input("\nDo you want to add this student?"))
            add = d.lower()
            if add=="yes":
                lista.append(x)
                o = int(input("Enter the roll # of student:"))
                roll_no.append(o)
                break
            elif add!="yes":
                break
else:
    import Invalid
    
import Program_Over            

