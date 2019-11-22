n=int(input("Enter Number Of Elements :"))
l2=[]
l3=[]
l4=[]
for i in range(n):
    l2.append(int(input("Enter Number :")))
median=int(input("Enter Median Value :"))
l2.sort()
for i in l2:
    if(i<median):
        l3.append(i)
    elif(i>median):
        l4.append(i)
print(l3)
print(l4)
