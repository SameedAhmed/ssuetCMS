import tkinter as tk
from functools import partial
import attendance
import bunk

root = tk.Tk()
root.geometry('400x200+90+100')
root.title('Attendance Calculator')
 
number1 = tk.StringVar()
number2 = tk.StringVar()
number3 = tk.StringVar()
 
labelTitle = tk.Label(root, text="Attendance Calculator").grid(row=0, column=1)
labelNum1 = tk.Label(root, text="Enter total no. of Classes").grid(row=1, column=0)
labelNum2 = tk.Label(root, text="Enter number of classes Attended").grid(row=2, column=0)
labelNum3 = tk.Label(root, text="Enter number of Leaves").grid(row=3, column=0)
labelResult = tk.Label(root)
labelResult.grid(row=5, column=1)
labelResult2 = tk.Label(root)
labelResult2.grid(row=7, column=1)
 
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=1)
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=1)
entryNum3 = tk.Entry(root, textvariable=number3).grid(row=3, column=1)
attendance.call_result = partial(attendance.call_result, labelResult, number1, number2,number3)
bunk.call_result2 = partial(bunk.call_result2, labelResult2, number1, number2,number3)
buttonCal = tk.Button(root, text="Calculate Attendance",fg="white",bg="#A020F0",command=attendance.call_result).grid(row=5, column=0)
buttonCal1 = tk.Button(root, text="Calculate Bunks",fg="white",bg="#A020F0",command=bunk.call_result2).grid(row=7, column=0)
root.mainloop()