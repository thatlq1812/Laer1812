from GlobalData import Datastorage
import pymysql
from tkinter import messagebox

class Book():
    def __init__(self, bid, title, author, status):
        self.bid = bid
        self.title = title
        self.author = author
        self.status = status

    def __str__(self):
        print(f'{self.bid} - {self.title} - {self.author} - {self.status}')


class Issue():
    def __init__(self,bid,issuedto):
        self.bid = bid
        self.issuedto = issuedto


class Node:
    def __init__(self, value: Book):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        storage = Datastorage()
        self.con = pymysql.connect(
            host=storage.g_host,
            user=storage.g_username,
            password=storage.g_password,
        )
        self.load_issued_books_from_db()

    def isEmpty(self):
        if self.head:
            return False
        else:
            return True

    def addBook(self, book):
        node = Node(book)
        if self.searchBook(book.bid) < 0:
            if self.isEmpty():
                self.head = node
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.next = node

    def searchBook(self, bid):
        """
        :param bid: book id
        :return: If book found, return the book's index in the linked list. Return -1 otherwise.
        """
        if self.isEmpty():
            return -1
        else:
            temp = self.head
            i = 0
            while temp:
                i += 1
                if temp.value.bid == bid:
                    return i
                temp = temp.next
            return -1

    def deleteBook(self, bid):
        """
        :param bid: book id
        :return: data of the book deleted
        """
        if self.isEmpty():
            return None
        else:
            if self.head.value.bid == bid:
                value = self.head.v
                self.head = self.head.next
                if self.isEmpty():
                    return value
                return value
            else:
                temp = self.head
                while temp.next:
                    if temp.next.value.bid == bid:
                        value = temp.next.value
                        temp.next = temp.next.next
                        return value
                    temp = temp.next
                return None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def traverse(self):
        temp = self.head
        while temp:
            temp.value.__str__()
            temp = temp.next

    def load_issued_books_from_db(self):
        try:
            con = pymysql.connect(host=self.con.host, user=self.con.user, password=self.con.password,database="db")
            cur = con.cursor()
            cur.execute("SELECT * FROM books_issued")
            for row in cur.fetchall():
                bid, issuedto = row
                temp = self.head
                while temp:
                    if temp.value.bid == bid:
                        temp.value.status = 'issued'
                        break
                    temp = temp.next
            con.close()
        except pymysql.MySQLError as e:
            messagebox.showinfo('Error', f"An error occurred while loading issued books: {str(e)}")

    def issue_book(self, bid, issuedto):
        temp = self.head
        while temp:
            if temp.value.bid == bid and temp.value.status == 'avail':
                temp.value.status = 'issued'

                try:
                    con = pymysql.connect(host=self.con.host, user=self.con.user, password=self.con.password, database="db")
                    cur = con.cursor()
                    cur = con.cursor()
                    cur.execute("UPDATE books SET status ='issued' WHERE bid = %s", bid)
                    cur.execute("INSERT INTO books_issued (bid, issuedto) VALUES (%s, %s)", (bid, issuedto))
                    con.commit()
                    con.close()
                    messagebox.showinfo('Success', "Book issued successfully")
                    return True
                except pymysql.MySQLError as e:
                    messagebox.showinfo('Error', f"An error occurred: {str(e)}")
                    con.rollback()
                    con.close()
                    return False
            temp = temp.next
        messagebox.showinfo('Error', "Book not found or not available")
        return False

    def return_book(self, bid):
        temp = self.head
        while temp:
            if temp.value.bid == bid and temp.value.status == 'issued':
                temp.value.status = 'avail'

                try:
                    storage = Datastorage()
                    myhost = storage.g_host
                    myuser = storage.g_username
                    mypass = storage.g_password
                    mydatabase = storage.g_database
                    con = pymysql.connect(host=myhost, user=myuser, password=mypass, database=mydatabase)
                    cur = con.cursor()
                    cur.execute("UPDATE books SET status ='avail' WHERE bid = %s", bid)
                    cur.execute("DELETE FROM books_issued WHERE bid = %s", bid)
                    con.commit()
                    con.close()
                    messagebox.showinfo('Success', "Book returned successfully")
                    return True
                except pymysql.MySQLError as e:
                    messagebox.showinfo('Error', f"An error occurred: {str(e)}")
                    con.rollback()
                    con.close()
                    return False
            temp = temp.next
        messagebox.showinfo('Error', "Book not found or not issued")
        return False


book1 = Book(3, 'haha', 'ngoc chau', 'avail')
book2 = Book(4, 'ha', 'chau', 'avail')
book3 = Book(5, 'haa', 'ngoc', 'avail')
booklist = LinkedList()
booklist.addBook(book1)
booklist.addBook(book2)
booklist.addBook(book3)
# print(booklist.searchBook(7))
booklist.deleteBook(bid=5)

# booklist.traverse()
