from LinkedList import *
import pymysql

mypass = "Mahehehe5ml" #use your own password
mydatabase="db" #The database name

con = pymysql.connect (host="localhost",user="LAPTOPCUI",password=mypass,database=mydatabase)
cur = con.cursor() #cur -> cursor

bookTable = "books"

getBooks = "select * from " + bookTable
bookList = LinkedList()
cur.execute(getBooks)
con.commit()
for i in cur:
    book = Book(i[0], i[1], i[2], i[3])
    bookList.addBook(book)
bookList.traverse()