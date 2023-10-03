from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from BookNode import BookList, BookNode
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *

# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase = "db"
bgr = "Mor.jpg"

button_color = "white"
text_color = "black"
buttonwidth = 0.45
buttonheight = 0.1

fontstyle = "SVN-Appleberry"
fontsize = 13
fonttype = "normal"


con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("Library")
root.minsize(width=700, height=500)
root.geometry("600x500")

# Take n greater than 0.25 and less than 5
same = True
n = 0.75

# Adding a background image
background_image = Image.open(bgr)
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth * n)
if same:
    newImageSizeHeight = int(imageSizeHeight * n)
else:
    newImageSizeHeight = int(imageSizeHeight / n)


def resize_and_center_image(event):
    new_width = event.width
    new_height = event.height
    original_width = background_image.width
    original_height = background_image.height
    original_ratio = original_width / original_height
    if new_width > new_height * original_ratio:
        resized_width = new_width
        resized_height = int(new_width / original_ratio)
    else:
        resized_height = new_height
        resized_width = int(new_height * original_ratio)
    image = background_image.resize((resized_width, resized_height), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    Canvas1.itemconfig(image_on_canvas, image=photo)
    Canvas1.image = photo
    x = (new_width - resized_width) // 2
    y = (new_height - resized_height) // 2
    Canvas1.coords(image_on_canvas, x, y)
    Canvas1.itemconfig(image_on_canvas, anchor="nw")


background_image = Image.open(bgr)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
image_on_canvas = Canvas1.create_image(0, 0, image=img, anchor="nw")
Canvas1.bind("<Configure>", resize_and_center_image)
Canvas1.config(bg="white")
Canvas1.pack(expand=True, fill=BOTH)
background_image = background_image.resize((800,600), Image.LANCZOS)
img = ImageTk.PhotoImage(background_image)

headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.15)

headingLabel = Label(headingFrame1, text="Welcome to \n DataFlair Library", bg=button_color, fg=text_color, font=('SVN-Nexa Rust Sans Black', 13))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

btn1 = Button(root, text="Add Book Details",font=(fontstyle, fontsize, fonttype), bg=button_color, fg=text_color, command=addBook)
btn1.place(relx=0.28, rely=0.4, relwidth=buttonwidth, relheight=buttonheight)

btn2 = Button(root, text="Delete Book",font=(fontstyle, fontsize, fonttype), bg=button_color, fg=text_color, command=delete)
btn2.place(relx=0.28, rely=0.5, relwidth=buttonwidth, relheight=buttonheight)

btn3 = Button(root, text="View Book List",font=(fontstyle, fontsize, fonttype), bg=button_color, fg=text_color, command=View)
btn3.place(relx=0.28, rely=0.6, relwidth=buttonwidth, relheight=buttonheight)

btn4 = Button(root, text="Issue Book to Student",font=(fontstyle, fontsize, fonttype), bg=button_color, fg=text_color, command=issueBook)
btn4.place(relx=0.28, rely=0.7, relwidth=buttonwidth, relheight=buttonheight)

btn5 = Button(root, text="Return Book",font=(fontstyle, fontsize, fonttype), bg=button_color, fg=text_color, command=returnBook)
btn5.place(relx=0.28, rely=0.8, relwidth=buttonwidth, relheight=buttonheight)

btn6 = Button(root, text="Quit",font=(fontstyle, fontsize, fonttype), bg=button_color, fg=text_color, command=root.destroy)
btn6.place(relx=0.8, rely=0.9, relwidth=0.18, relheight=0.08)

root.mainloop()
