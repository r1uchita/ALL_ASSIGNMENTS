import mysql.connector as mc
#1.create connection....
conn=mc.connect(host="localhost", user="root", password ="", database='librarydb')
print("Connection Done Successfully.....")

#2.create cursor...
cursor=conn.cursor()

#3.Executing Query....
def _display_database():
    cursor.execute("show databases ")
    records=cursor.fetchall()
    for row in records:
        print(row)
#_display_database()

def _student_details():
    print("\nStudent Informatiuon:")
    cursor.execute("select * from `student`")
    records = cursor.fetchall()
    for row in records:
        print(row)
        #Function Calling
#_student_details()

#Static
def _Available_SubBooks():
    cursor.execute("SELECT * FROM `book` NATURAL JOIN `title`WHERE title LIKE('%java%')")

    records = cursor.fetchall()
    for row in records:
        print(row)
#_Available_SubBooks()

#Dynamic
def _search_subBooks(s):
    sub=s
    cursor.execute("SELECT * FROM `book` NATURAL JOIN `title`WHERE title LIKE '%"+sub+"%'")
    records = cursor.fetchall()
    for row in records:
        print(row)
#_search_subBooks('c')

def _getfinedetails():
    cursor.execute("SELECT fname,lname,(datediff(CURRENT_DATE, issuedate)-7)*50 "
                   "AS Late_Fine FROM `issue` NATURAL JOIN `student`  WHERE (datediff(CURRENT_DATE,issuedate)>7)")

    records = cursor.fetchall()
    for row in records:
        print(row)
_getfinedetails()
