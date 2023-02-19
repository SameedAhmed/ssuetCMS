def call_result(label_result,n1,n2,n3):
    num1 = int(n1.get())
    num2 = int(n2.get())
    num3 = int(n3.get())
    result = (num2/num1)*100
    label_result.config(text="Attendance percentage: %.2f" % result)
    return