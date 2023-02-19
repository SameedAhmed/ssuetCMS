def call_result2(label_result2,n1,n2,n3):
    num1 = int(n1.get())
    num2 = int(n2.get())
    num3 = int(n3.get())
    bunk = num1-num2-num3
    '''if (bunk +num2 >=num1):
        bunk= ( num1-num2)'''
    label_result2.config(text="No of classes that can be bunked: %d" % bunk)
    return