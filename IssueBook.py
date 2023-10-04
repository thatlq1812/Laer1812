from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
from LinkedList import LinkedList
from GlobalData import Datastorage


book_list = LinkedList()


def issue():
    bid = inf1.get()
    issued_to = inf2.get()

    if not bid or not issued_to:
        messagebox.showwarning("Invalid Input", "Please ensure all fields are filled.")
        return

    storage = Datastorage()
    myhost = storage.g_host
    myuser = storage.g_username
    mypass = storage.g_password
    mydatabase = storage.g_database
    con = pymysql.connect(host=myhost, user=myuser, password=mypass, database=mydatabase)
    cur = con.cursor()

    try:
        cur.execute("SELECT status FROM books WHERE bid = %s", (bid,))
        result = cur.fetchone()
        if result is None:
            messagebox.showinfo("Failed", "No book found with ID {}".format(bid))
            con.rollback()
        elif result[0] == 'issued':
            messagebox.showinfo("Failed", "Book with ID {} is already issued".format(bid))
            con.rollback()
        else:
            cur.execute("UPDATE books SET status = 'issued' WHERE bid = %s", (bid,))
            cur.execute("INSERT INTO books_issued (bid, issuedto) VALUES (%s, %s)", (bid, issued_to))
            messagebox.showinfo('Success', "Book issued successfully")
            con.commit()
    except pymysql.MySQLError as e:
        messagebox.showinfo("Error", f"An error occurred: {str(e)}")
        con.rollback()
    finally:
        con.close()
    root.destroy()


def issueBook():
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status

    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2)

    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62)

    # Issued To Student name 
    lb2 = Label(labelFrame,text="Issued To : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.4)

    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3,rely=0.4, relwidth=0.62)

    # Issue Button
    issueBtn = Button(root,text="Issue",bg='#d1ccc0', fg='black',command=issue)
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

    quitBtn = Button(root,text="Quit",bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    root.mainloop()
