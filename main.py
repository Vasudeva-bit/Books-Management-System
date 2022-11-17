# from email import message
from tkinter import *
import app
import login
from PIL import Image, ImageTk


class main:
    def __init__(self):
        self.root = app.interface().window()

    def update(self):
        self.root.destroy()
        login.log().window()
        self.database()

    def window(self):
        w = Label(width=700, height=2,
                  bg="skyblue", fg="black")
        w.place(x=0, y=0)
        w = Label(self.root, text="Welcome to Book Management System",
                  bg="skyblue", fg="black", font=5)
        w.place(x=175, y=1/2)
        w = Message(self.root,
                    text="Welcome to our Book Management Application, we provide you best books for every age group and mood.\nBut before that it is important for you to log in to our application.", 
                    width=680)
        w.place(x=10, y=40)

        # book cover pages trending now (format: three columns, 2 rows)
        image = Image.open("bookShelf.jpeg")
        image = ImageTk.PhotoImage(image)
        w = Label(image=image)
        w.image = image
        w.place(x=0, y=75)
        
        login = Button(self.root, text="Login", bg="light green", command=self.update)
        login.place(x=325, y=75)

        w = Message(self.root, text="Suggestions/Feedback", width="500")
        w.place(x=10, y=490)
        w = Button(self.root, text="Help?", width=10, bg="light green", height=1)
        w.place(x=200, y=490)
        w = Message(self.root, text="CEOs: Suraj , Vasudeva , Anand", width="500")
        w.place(x=10, y=530)
        w = Button(self.root, text="Contact", width=10, bg="light green", height=1)
        w.place(x=200, y=530)

        # w = Button(self.root, text="Books", width=15, height=2, bg="lawn green")
        # w.place(x=20, y=450)
        # w = Button(self.root, text="Store", width=15, height=2, bg="lawn green")
        # w.place(x=100, y=450)

        self.root.mainloop()


if __name__ == "__main__":
    main().window()

# first things first:
# 1. fix the size of window to a standard dimensions height: 400 and width 300
# 2. reduce the size of the self.root window into the standard size and align with the rest of the pages
# 3. confine to similar kinda of coding practices
