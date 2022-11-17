from tkinter import *
from app import interface as app
import login
import books

class account:
    def __init__(self):
        self.root = app().window()
        self.window()
        self.next = None

    def login(self):
        self.root.destroy()
        login.log().window()

    def books(self):
        self.root.destroy()
        books.viewBooks().window()

    def window(self):
        w = Label(self.root, text="Explore the store more!",
                  bg='skyblue', justify='center')
        w.pack(fill=X)

        login = Button(self.root, text="Login", bg='light green', command=self.login)
        login.place(x=20, y=20)

        w = Label(self.root, text="Representing Company")
        w.place(x=20, y=60)

        w = Text(self.root, height=1, width=15)
        w.place(x=150, y=60)

        w = Label(self.root, text="Representing Books")
        w.place(x=20, y=100)

        w = Text(self.root, height=1, width=15)
        w.place(x=150, y=100)

        w = Label(self.root, text="Sub-Category B Prices")
        w.place(x=20, y=140)

        w = Text(self.root, height=1, width=15)
        w.place(x=150, y=140)

        books = Button(self.root, text="Books", bg="light green", command=self.books)
        books.place(x=20, y=160)

        report = Button(self.root, text="Need Help/Report", bg="light green")
        report.place(x=20, y=int(0.90*(app().gheight)))
        self.root.mainloop()

if __name__ == "__main__":
    account()