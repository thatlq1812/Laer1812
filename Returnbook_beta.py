from tkinter import *
import pymysql
from BookNode import BookList

mypass = "root"
mydatabase="db" 

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

book_list = BookList()

def returnn():

  bid = bookInfo1.get()

  book_list.remove(bid)

  cur.execute("DELETE FROM books_issued WHERE bid=%s", bid)

  con.commit()
  root.destroy()


def returnBook():

  global bookInfo1,SubmitBtn,quitBtn,Canvas1,con,cur,root,labelFrame, lb1

  root = Tk()
  root.title("Library")
  root.minsize(width=400,height=400)
  root.geometry("600x500")

  Canvas1 = Canvas(root)
  Canvas1.config(bg="#006B38")
  Canvas1.pack(expand=True,fill=BOTH)

  headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
  headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

  headingLabel = Label(headingFrame1, text="Return Book", bg='black', fg='white', font=('Courier',15)) 
  headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

  labelFrame = Frame(root,bg='black')
  labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

  lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
  lb1.place(relx=0.05,rely=0.5)

  bookInfo1 = Entry(labelFrame)
  bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)

  SubmitBtn = Button(root,text="Return",bg='#d1ccc0', fg='black',command=returnn)
  SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

  quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
  quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

  root.mainloop()

book_list = BookList()
returnBook(book_list)