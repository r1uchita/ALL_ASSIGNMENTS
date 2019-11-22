m1=int(input("Enter Subject1 Marks:"))
m2=int(input("Enter Subject2 Marks:"))
m3=int(input("Enter Subject3 Marks:"))
if(m1>=40 and m2>=40 and m3>=40):
    per=(m1+m2+m3)/3
    print("Student Pass with",per,"%")
else:
    if m1<40 and m2>=40 and m3>=40:
        if m1>=32:
            print("Pass With Grace Marks")
    elif m1>=40 and m2<40 and m3>=40:
        if m2>=32:
            print("Pass With Grace Marks")
    elif m1>=40 and m2>=40 and m3<40:
        if m3>=32:
            print("Pass With Grace Marks")
    else:
        print("Fail")
        
        
