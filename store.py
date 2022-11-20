from tkinter import *
from app import interface as app
import login
import books
import needHelp
import store

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

    def needHelp(self):
        self.root.destroy()
        needHelp.Help().window()

    def store(self):
        self.root.destroy()
        store.account().window()

    def books(self):
        self.root.destroy()
        books.viewBooks().window()

    def window(self):
        w = Label(self.root, text="Explore the store more!",
                  bg='skyblue', justify='center')
        w.pack(fill=X)

        w = Message(self.root, text="Interestded in the store, why wait, just login or register", width="500")
        w.place(x=20, y=20)

        login = Button(self.root, text="Login", bg='light green', command=self.login)
        login.place(x=320, y=20)

        w = Label(self.root, text="Book Name")
        w.place(x=20, y=60)

        w = Text(self.root, height=1, width=15)
        w.place(x=150, y=60)

        w = Label(self.root, text="Book Number")
        w.place(x=20, y=100)

        w = Text(self.root, height=1, width=15)
        w.place(x=150, y=100)

        w = Label(self.root, text="Field of the Book")
        w.place(x=20, y=140)

        w = Text(self.root, height=1, width=15)
        w.place(x=150, y=140)

        books = Button(self.root, text="Search", bg="light green", command=self.books)
        books.place(x=25, y=170)

        w = Message(self.root, text="Interested to view to store, click here to explore it!", width="500")
        w.place(x=20, y=200)
        store = Button(self.root, text="Store", bg='light green', command=self.store)
        store.place(x=320, y=200)

        w = Message(self.root, text="To perform any transactions on books! Check here.", width="500")
        w.place(x=20, y=250)
        books = Button(self.root, text="Books", bg='light green', command=self.books)
        books.place(x=320, y=250)

        report = Button(self.root, text="Need Help/Report", bg="light green", command=self.needHelp)
        report.place(x=25, y=int(0.90*(app().gheight)))
        self.root.mainloop()

if __name__ == "__main__":
    account()