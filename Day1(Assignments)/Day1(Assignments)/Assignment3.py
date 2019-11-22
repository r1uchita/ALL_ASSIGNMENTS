def dictionary(list):
    dict = {}
    for item in list :
        if(item in dict):
            dict[item] = dict[item] + 1
        else :
            dict[item] = 1
    print("List Of Dictionary :",dict)
def list_of_list(list):
    list2 = []
    for item in list:
        l2 = []
        l2.append(item)
        l2.append(list.count(item))
        list2.append(l2)
    list_set = set(map(tuple,list2))
    list_list = []
    for i in list_set :
        result = []
        for t in i: 
            result.append(t)
        list_list.append(result)
    print("List Of List :",list_list)
def list_of_tuple(list):
    list2 = []
    for item in list:
        l2 = []
        l2.append(item)
        l2.append(list.count(item))
        list2.append(l2)
    set_tuple = set(map(tuple,list2))
    list_tuple = []
    for i in set_tuple :
        list_tuple.append(i)
    print("List Of Tuples :",list_tuple)
if __name__ == "__main__":
    n = int(input("Enter Numbers Of Elements :"))
    l = []
    for i in range(n):
        l.append(int(input("Enter Number :")))
    while(1):
        print("1 : List Of Dictionary " )
        print("2 : List Of List")
        print("3 : List Of Tuple")
        print("4 : Exit")
        ch = int(input("Enter Your Choice :"))
        if(ch == 1):
            dictionary(l)
        elif(ch == 2):
            list_of_list(l)
        elif(ch == 3):
            list_of_tuple(l)
        elif(ch == 4):
            break

