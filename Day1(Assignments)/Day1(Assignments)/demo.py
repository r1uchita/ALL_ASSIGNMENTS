import mysql.connector as mc
#1.create connection....
conn=mc.connect(host="localhost", user="root", password ="", database='librarydb')
print("Connection Done Successfully.....")

#2.create cursor...
cursor=conn.cursor()

#3.Executing Query....
'''
def _display_database():
    cursor.execute("show databases ")
    records=cursor.fetchall()
    for row in records:
        print(row)
_display_database()

def _student_details():
    print("\nStudent Informatiuon:")
    cursor.execute("select * from `student`")
    records = cursor.fetchall()
    for row in records:
        print(row)
        #Function Calling
_student_details()'''


def _Available_SubBooks():
    cursor.execute("SELECT * FROM `book` NATURAL JOIN `title`WHERE title LIKE('%java%')")

    records = cursor.fetchall()
    for row in records:
        print(row)
_Available_SubBooks()

