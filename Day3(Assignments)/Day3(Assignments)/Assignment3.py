import math
print("-------------------Simple Calculator------------------")
while(True):
    print("\n1.Addition\t2.Subtraction\t3.Multiplication\n4.Division\t5.Modulus\t6.Square Root of Number")
    ch=int(input("\nEnter Your Choice::"))
    n1=int(input("\nEnter First Number::"))
    n2=int(input("\nEnter Second Number::"))
    
    if(ch==1):
        print("\nAddition of 2 Numbers::",(n1+n2))
        print("-----------------------------------------------------------------------")
    elif(ch==2):
        print("\nSubtraction of 2 Numbers::",(n1-n2))
        print("-----------------------------------------------------------------------")
    elif(ch==3):
        print("\nMultiplication of 2 Numbers::",(n1*n2))
        print("-----------------------------------------------------------------------")
    elif(ch==4):
        print("\nDivision of 2 Numbers::",(n1/n2))
        print("-----------------------------------------------------------------------")
    elif(ch==5):
         print("\nModulus of 2 Numbers::",(n1%n2))
         print("-----------------------------------------------------------------------")
    elif(ch==6):
        print("\nSquare Root of Number:",math.sqrt(n1))
        print("-----------------------------------------------------------------------")
    elif(ch==7):
        break        
    else:
        print("\nInvalid Choice,Enter Correct Choice!!!")
