num=int(input("Enter Number of Elements:"))
for i in range(1,num):
    if ((i%3)==0):
        if ((i%5)==0):
            print(i,"Fizz Buzz")
        else:
            print(i,"Fizz")
    elif ((i%5)==0):
        print(i,"Buzz")
    else:
        print(i)
