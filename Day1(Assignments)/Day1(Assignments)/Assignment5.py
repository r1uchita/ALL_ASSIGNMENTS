num=int(input("Enter Number Of Elements :"))
l1=[]
for i in range(num):
    l1.append(int(input("Enter Radius :")))
for i in  l1:
    print(i,"Radius =",i*i*3.14)
