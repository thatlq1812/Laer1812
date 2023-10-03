from LinkedList import *
import pymysql
from GlobalData import Datastorage

storage = Datastorage()
myhost = storage.g_host
myuser = storage.g_username
mypass = storage.g_password
mydatabase = storage.g_database
mybook = storage.g_book
con = pymysql.connect(host=myhost, user=myuser, password=mypass, database=mydatabase)
cur = con.cursor()

getBooks = "select * from " + mybook
bookList = LinkedList()
cur.execute(getBooks)
con.commit()
for i in cur:
    book = Book(i[0], i[1], i[2], i[3])
    bookList.addBook(book)
bookList.traverse()