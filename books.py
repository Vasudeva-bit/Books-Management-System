from tkinter import *
import pandas as pd
from app import interface as app
import main


class viewBooks():
    def __init__(self):
        self.root = app().window()
        self.window()

    def ad(self):
        bookNo = int(self.add.get(1.0, "end-1c"))
        status = 1 + int(self.books_df.loc[self.books_df['Book Number'] == bookNo, 'Book Status'])
        w = Message(self.root, text=f"The Status of the book is update to {status}\t\t\t\n", width="670")
        w.place(x=12, y=320)
        self.books_df['Book Status'] = status


    def delet(self):
        bookNo = int(self.delete.get(1.0, "end-1c"))
        status = int(self.books_df.loc[self.books_df['Book Number'] == bookNo, 'Book Status']) - 1
        if(status < 0): status = 0
        w = Message(self.root, text=f"The Status of the book is update to {status}\t\t\t\n", width="670")
        w.place(x=12, y=320)
        self.books_df['Book Status'] = status

    def view(self):
        bookNo = int(self.delete.get(1.0, "end-1c"))
        name = str(self.books_df.loc[self.books_df['Book Number'] == bookNo, 'Book Name'].iloc[0])
        desc = str(self.books_df.loc[self.books_df['Book Number'] == bookNo, 'Book Description'].iloc[0])
        field = str(self.books_df.loc[self.books_df['Book Number'] == bookNo, 'Field'].iloc[0])
        w = Message(self.root, text=f"The Title is {name}. It belongs to {field}\n{desc}", width="670")
        w.place(x=12, y=320)

    def issue(self):
        bookNo = int(self.issu.get(1.0, "end-1c"))
        status = int(self.books_df.loc[self.books_df['Book Number'] == bookNo, 'Book Status']) - 1
        if(status < 0): status = 0
        w = Message(self.root, text=f"The Status of the book is update to {status}\t\t\t\n", width="670")
        w.place(x=12, y=320)
        self.books_df['Book Status'] = status

    def retun(self):
        pass
        bookNo = int(self.ret.get(1.0, "end-1c"))
        status = 1 + int(self.books_df.loc[self.books_df['Book Number'] == bookNo, 'Book Status'])
        w = Message(self.root, text=f"The Status of the book is update to {status}\t\t\t\n", width="670")
        w.place(x=12, y=320)
        self.books_df['Book Status'] = status

    def home(self):
        self.root.destroy()
        main.main().window()

    def window(self):
        self.books_df = pd.read_csv('Books Data.csv')
        w = Label(self.root, text="Welcome to Book Transactions",
                  bg='skyblue', justify='center')
        w.pack(fill=X)

        w = Message(self.root, text="Welcome to book transactions window, dedicated only for books related operations such as add, return, issue, delete, view etc. Feel free to check out various options facilitated by our software. Any changes to the books store need to done in this window only. All the changes are reflected in the database timely.", width="670")
        w.place(x=12, y=30)

        w = Label(self.root, text="Enter the Book No to add to store")
        w.place(x=15, y=120)
        self.add = Text(self.root, height=1, width=22)
        self.add.place(x=250, y=120)
        add = Button(self.root, text="Add",
                     bg="light green", command=self.ad, width=20)
        add.place(x=450, y=119)

        w = Label(self.root, text="Enter the Book No to delete from store")
        w.place(x=15, y=160)
        self.delete = Text(self.root, height=1, width=22)
        self.delete.place(x=250, y=160)
        delet = Button(self.root, text="Delete",
                     bg="light green", command=self.delet, width=20)
        delet.place(x=450, y=159)

        w = Label(self.root, text="Enter the Book No to return to store")
        w.place(x=15, y=200)
        self.ret = Text(self.root, height=1, width=22)
        self.ret.place(x=250, y=200)
        ret = Button(self.root, text="Return",
                     bg="light green", command=self.retun, width=20)
        ret.place(x=450, y=199)

        w = Label(self.root, text="Enter the Book No to issue to user")
        w.place(x=15, y=240)
        self.issu = Text(self.root, height=1, width=22)
        self.issu.place(x=250, y=240)
        issu = Button(self.root, text="Issue",
                     bg="light green", command=self.issue, width=20)
        issu.place(x=450, y=239)

        w = Label(self.root, text="Enter the Book No to view details")
        w.place(x=15, y=240)
        self.vie = Text(self.root, height=1, width=22)
        self.vie.place(x=250, y=240)
        vie = Button(self.root, text="View",
                     bg="light green", command=self.view, width=20)
        vie.place(x=450, y=239)

        w = Message(self.root, text="Thanks for exploring various operations, go to home here!", width="670")
        w.place(x=10, y=265)

        home = Button(self.root, text="Home", bg="light green", command=self.home)
        home.place(x=15, y=290)

        self.root.mainloop()


if __name__ == "__main__":
    ob = viewBooks()
