s = input("Enter String :").split(" ")
keywords = []
methods = []
for i in s :
    if i =="if" or i == "else" or i == "return" or i == "break":
        if i not in keywords :
            keywords.append(i)
    elif i == "print" or i == "input" or i == "len" :
        if i not in methods :
            methods.append(i)
print("KeyWords = ",keywords)
print("Methods = ",methods)
dict = {}
for item in s :
    if(item in dict):
        dict[item] = dict[item] + 1
    else :
        dict[item] = 1
print("Frequency :",dict)
