n=int(input("Enter Number Of Elements :"))
l=[]
odd,even,prime=0,0,0
for i in range(n):
    l.append(int(input("Enter Number :")))
for i in l :
    if(i%2==0):
        even+=1
    else:
        odd+=1
    if i > 1:
        for j in range(2,i):
            if(i % j) == 0:
                break
        else:
            prime += 1
print("Even Numbers Present in List :",even)
print("Odd Numbers  Present in List:",odd)
print("Prime Numbers Present in List:",prime)
print("Largest Number :",max(l))
print("Smallest Number :",min(l))

