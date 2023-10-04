from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
from GlobalData import Datastorage
from LinkedList import LinkedList


book_list = LinkedList()


def return_book():
    bid = bookInfo1.get()
    if not bid:
        messagebox.showwarning("Invalid Input", "Please ensure the Book ID field is filled.")
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
            messagebox.showinfo("Failed",message= "No book found with ID {}".format(bid))
            con.rollback()
        elif result[0] == 'avail':
            messagebox.showinfo("Failed",message="Book with ID {} is not issued".format(bid))
            con.rollback()
        else:
            cur.execute("UPDATE books SET status = 'avail' WHERE bid = %s", (bid,))
            cur.execute("DELETE FROM books_issued WHERE bid = %s", (bid,))
            messagebox.showinfo('Success', "Book returned successfully")
            con.commit()
    except pymysql.MySQLError as e:
        messagebox.showinfo("Error", f"An error occurred: {str(e)}")
        con.rollback()
    finally:
        con.close()
    root.destroy()


def returnBook(): 
    
    global bookInfo1,SubmitBtn,quitBtn,Canvas1,con,cur,root,labelFrame,lb1
    
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
        
    # Book ID to Delete
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    # Submit Button
    SubmitBtn = Button(root,text="Return",bg='#d1ccc0', fg='black',command=return_book)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
