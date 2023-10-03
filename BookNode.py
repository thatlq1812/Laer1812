from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox


class BookNode:
    def __init__(self, bid, title, author, status):
        self.bid = bid
        self.title = title
        self.author = author
        self.status = status
        self.next = None


class BookList:
    def __init__(self):
        self.head = None

    def add_book(self, bid, title, author, status):
        new_book = BookNode(bid, title, author, status)
        new_book.next = self.head
        self.head = new_book
        con = pymysql.connect(host="localhost", user="root", password="root", database="db")
        cur = con.cursor()

        temp = self.head
        try:
            # Check if book already exists
            cur.execute("SELECT * FROM books WHERE bid = %s", (temp.bid,))
            if cur.fetchone() is None:
                # If not, insert new book
                cur.execute("INSERT INTO books (bid, title, author, status) VALUES (%s, %s, %s, %s)",
                            (temp.bid, temp.title, temp.author, temp.status))
                messagebox.showinfo('Success', "Book added successfully")
                con.commit()
            else:
                messagebox.showinfo(title="Failed", message="Book with ID {temp.bid} already exists in the database.")
                con.rollback()
        except pymysql.MySQLError as e:
            messagebox.showinfo(f"Error: {str(e)}")
            con.rollback()
        con.close()

    def del_from_db(self, del_bid):
        con = pymysql.connect(host="localhost", user="root", password="root", database="db")
        cur = con.cursor()

        if True:
            cur.execute(query="SELECT * FROM books WHERE bid = %s", args=del_bid)
            if cur.fetchone() is not None:
                cur.execute(query="DELETE FROM books WHERE bid = %s", args=del_bid)
                messagebox.showinfo(title="Success", message="The book has been deleted!")
                con.commit()
            else:
                cur.execute(query="SELECT * FROM books_issued WHERE bid = %s", args=del_bid)
                if cur.fetchone() is not None:
                    cur.execute(query="DELETE FROM books WHERE bid = %s", args=del_bid)
                    messagebox.showinfo(title="Success", message="The book has been deleted!")
                    con.commit()
                else:
                    messagebox.showinfo(title="Failed", message="That bid does not exist")
                    con.rollback()
        con.close()

    def book_issue(self, iss_bid, iss_name):
        con = pymysql.connect(host="localhost", user="root", password="root", database="db")
        cur = con.cursor()

        if True:
            cur.execute("SELECT * FROM books WHERE bid = %s AND status = 'avail'", iss_bid)
            if cur.fetchone() is not None:
                cur.execute("UPDATE books SET status ='issued' WHERE bid = %s", iss_bid)
                cur.execute("INSERT INTO books_issued (bid, issuedto) VALUES (%s, %s)", (iss_bid, iss_name))
                messagebox.showinfo("Success", "Book Issued Successfully!")
                con.commit()
            else:
                cur.execute("SELECT * FROM books WHERE bid = %s AND status = 'issued'", iss_bid)
                if cur.fetchone() is not None:
                    messagebox.showinfo("Failed", "Book Already Issued")
                else:
                    messagebox.showinfo("Failed", "Book Not Found")
                con.rollback()
        con.close()


    def book_return(self, res_bid):
        con = pymysql.connect(host="localhost", user="root", password="root", database="db")
        cur = con.cursor()

        if True:
            cur.execute("SELECT * FROM books_issued WHERE bid = %s", res_bid)
            if cur.fetchone() is not None:
                cur.execute("UPDATE books SET status ='avail' WHERE bid = %s", res_bid)
                cur.execute("DELETE FROM books_issued WHERE bid = %s", res_bid)
                messagebox.showinfo("Success", "Book Return Successfully!")
                con.commit()
            else:
                cur.execute("SELECT * FROM books WHERE bid = %s AND status = 'avail'", res_bid)
                if cur.fetchone() is not None:
                    messagebox.showinfo("Failed", "Book Already Avail")
                else:
                    messagebox.showinfo("Failed", "Book Not Found")
                con.rollback()
        con.close()
