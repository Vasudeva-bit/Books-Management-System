from tkinter import *
from app import interface as app
import store
import login


class reg:
    def __init__(self):
        self.root = app().window()
        self.window()

    def update(self):
        if self.database():
            self.root.destroy()
            login.log().window()

    def database(self):
        self.user = self.user.get(1.0, "end-1c")
        self.passcode = self.passcode.get(1.0, "end-1c")
        self.name = self.name.get(1.0, "end-1c")
        self.email = self.email.get(1.0, "end-1c")
        self.phone = self.phone.get(1.0, "end-1c")

        dbcon = app().dbcon
        if(self.user == "" or self.passcode == "" or self.name == "" or self.email == "" or self.phone == "") :
            return False
        # print(self.dbcon)
        cursor = dbcon.cursor()
        # INSERT INTO table_name (column1, column2, column3, ...) VALUES (value1, value2, value3, ...);
        Squery = "INSERT INTO CREDENTAILS VALUES(\'"+ str(self.name) + "\', \'" + str(self.email) + "\', \'" + str(self.phone) + "\', \'" + str(self.user) + "\', \'" + str(self.passcode) + "\');"
        print(Squery)
        cursor.execute(Squery)
        dbcon.commit()
        cursor.execute("SELECT * FROM CREDENTAILS")
        # result = cursor.fetchall()
        # print(result)
        return True

    def validate(self):
        flag = True
        return flag

    def window(self):
        w = Label(self.root, text="Sign up your Account!",
                  bg='skyblue', justify='center')
        w.pack(fill=X)

        w = Label(self.root, text="Enter Full Name")
        w.place(x=20, y=60)

        self.name = Text(self.root, height=1, width=15)
        self.name.place(x=150, y=60)

        w = Label(self.root, text="Enter your Email-ID")
        w.place(x=20, y=100)

        self.email = Text(self.root, height=1, width=15)
        self.email.place(x=150, y=100)

        w = Label(self.root, text="Enter Phone number")
        w.place(x=20, y=140)

        self.phone = Text(self.root, height=1, width=15)
        self.phone.place(x=150, y=140)

        w = Label(self.root, text="Re-enter your Email-ID")
        w.place(x=20, y=180)

        self.reemail = Text(self.root, height=1, width=15)
        self.reemail.place(x=150, y=180)

        w = Label(self.root, text="Set Username")
        w.place(x=20, y=220)

        self.user = Text(self.root, height=1, width=15)
        self.user.place(x=150, y=220)

        w = Label(self.root, text="Enter your Password")
        w.place(x=20, y=260)

        self.passcode = Text(self.root, height=1, width=15)
        self.passcode.place(x=150, y=260)

        w = Label(self.root, text="Retype your Password")
        w.place(x=20, y=300)

        self.repasscode = Text(self.root, height=1, width=15)
        self.repasscode.place(x=150, y=300)

        flag = self.validate()

        register = Button(self.root, text="Sign Up",
                          bg="light green", command= self.update if flag else None)
        register.place(x=20, y=330)

        report = Button(self.root, text="Need Help/Report", bg="light green")
        report.place(x=20, y=int(0.90*(app().gheight)))
        self.root.mainloop()


if __name__ == "__main__":
    ob = reg()
