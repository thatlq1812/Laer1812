from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
from LinkedList import LinkedList
from GlobalData import Datastorage

# Add your own database name and password here to reflect in the code
storage = Datastorage()
myhost = storage.g_host
myuser = storage.g_username
mypass = storage.g_password
mydatabase = storage.g_database
con = pymysql.connect(host=myhost, user=myuser, password=mypass, database=mydatabase)

book_list = LinkedList()


def issue():
    bid = inf1.get()
    issueto = inf2.get()
    if not bid or not issueto:
        messagebox.showwarning("Invalid Input", "Please ensure all fields are filled.")
        return
    book_list.load_issued_books_from_db()
    book_list.issue_book(bid, issueto)
    print(bid)
    print(issueto)
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
