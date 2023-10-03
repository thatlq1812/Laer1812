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
mybook = storage.g_book
con = pymysql.connect(host=myhost, user=myuser, password=mypass, database=mydatabase)
cur = con.cursor()


def View():

    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Books", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.3

    Label(labelFrame, text="%-10s%-60s%-30s%-20s"%('BID','Title','Author','Status'),bg='black',fg='white', anchor='w').place(relx=0.07,rely=0.1, relwidth=0.9)
    Label(labelFrame, text="----------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.07,rely=0.2, relwidth=0.9)
    getBooks = "select * from "+mybook
    try:
        cur.execute(getBooks)
        book_list = LinkedList()
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-10s%-60s%-30s%-20s" %(i[0],i[1],i[2],i[3]),bg='black',fg='white', anchor='w').place(relx=0.07,rely=y, relwidth=0.9)
            y += 0.06
    except:
        messagebox.showinfo("Failed to fetch files from database")

    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)

    root.mainloop()
