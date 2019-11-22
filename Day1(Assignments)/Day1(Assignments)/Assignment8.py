def sort_By_FirstElement(list_tuples):
    return(sorted(list_tuples,key = lambda x:x[0]))
def sort_By_SecondElement(list_tuples):
    return(sorted(list_tuples,key = lambda x:x[1]))
def sort_By_LastElement(list_tuples):
    return(sorted(list_tuples,key = lambda x:x[2]))
def mahesh():
    n = int(input("Enter Number of Elements :"))
    list_tuple = []
    for i in range(n):
        elements = []
        print("Enter Numbers For",i+1,"Tuple")
        for i in range(3):
            elements.append(int(input("Enter Number :")))
        list_tuple.append(tuple(elements))
    print("Sort By 1st Element :",sort_By_FirstElement(list_tuple))
    print("Sort By 2nd Element :",sort_By_SecondElement(list_tuple))
    print("Sort By Last Element :",sort_By_LastElement(list_tuple))

if __name__ == "__main__" :
    mahesh()
        
