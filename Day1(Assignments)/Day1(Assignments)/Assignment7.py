n = int(input("Enter Number of records :"))
list_records = []
for i in range(n):
    data = input("Enter StudentID BookID IssueDate(DD-MM-YY) :").split()
    list_records.append(data)
while(1):
    print("1 :By BookID")
    print("2 :By StudentID")
    print("3 :By IssueDate")
    print("4 :Exit")
    ch = int(input("Enter Choice :"))
    if(ch == 1):
        book_id = input("Enter BookID :")
        for i in list_records :
            if book_id in i :
                print("StudentID = ",i[0],"IssueDate = ",i[2])
    elif (ch == 2) :
        stud_id = input("Enter StudentID :")
        for i in list_records :
            if stud_id in i :
                print("BookID = ",i[1])
    elif(ch == 3):
        issuseDate = input("Enter IssueDate(DD-MM-YY) :")
        for i in list_records :
            if issuseDate in i :
                print("StudentID",i[0],"BookID = ",i[1])
    elif(ch == 4):
        break
    else :
        print("Please Enter Correct Choice !!!")
