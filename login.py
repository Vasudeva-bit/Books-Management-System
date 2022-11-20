from tkinter import *
from app import interface as app
import store
import register
import needHelp 

class log:
    def __init__(self):
        self.root = app().window()
        self.data = {'self.user':"self.passcode"}
        self.user = None
        self.passcode = None
        self.window()

    def verify_account(self):
        # Connecting to the SQL connector
        result = self.database()
        if(result == self.passcode):
            return True
        else:
            return False

    def update(self):
        self.user = self.user.get(1.0, "end-1c")
        self.passcode = self.passcode.get(1.0, "end-1c")
        print(self.user, self.passcode)
        self.data[self.user] = self.passcode
        if(self.verify_account()) :
            self.root.destroy()
            store.account().window()
        else:
            self.root.destroy()
            log()

    def needHelp(self):
        self.root.destroy()
        needHelp.Help().window()

    def database(self):
        dbcon = app().dbcon
        cursor = dbcon.cursor()
        Squery = "SELECT * FROM CREDENTAILS WHERE ID = \'"+ str(self.user) + "\';"
        print(Squery)
        cursor.execute(Squery)
        result = cursor.fetchall()[0][-1]
        print(result)
        return result

    def register(self) :
        self.root.destroy()
        register.reg().window()

    def window(self):
        w = Label(self.root, text="Login into your Account!",
                  bg='skyblue', justify='center')
        w.pack(fill=X)

        w = Label(self.root, text="Username")
        w.place(x=20, y=60)

        self.user = Text(self.root, height=1, width=15)
        self.user.place(x=150, y=60)

        w = Label(self.root, text="Password")
        w.place(x=20, y=100)

        self.passcode = Text(self.root, height=1, width=15)
        self.passcode.place(x=150, y=100)

        login = Button(self.root, text="Login", bg="light green", command=self.update)
        login.place(x=20, y=125)

        w = Label(self.root, text="Don't have account, create one")
        w.place(x=20, y=150)
        register = Button(self.root, text="Register", bg="light green", command=self.register)
        register.place(x=200, y=148)

        report = Button(self.root, text="Need Help/Report", bg="light green", command=self.needHelp)
        report.place(x=20, y=int(0.90*(app().gheight)))
        self.root.mainloop()

if __name__ == "__main__":
    ob = log()