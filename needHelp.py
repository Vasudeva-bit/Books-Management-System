import app
from tkinter import *
import main

class Help:
    def __init__(self):
        self.root = app.interface().window()

    def home(self):
        self.root.destroy()
        main.main().window()

    def window(self):
        Label(self.root, height="1",
              text="Need Help Or Report?", bg="skyblue", fg="black", width="700").pack()
        Message(self.root, text="Frequently Asked Questions", width=500,
                 font=('arial', 10, 'bold')).place(x=260, y=25)
        Message(self.root, text="This page provides answers to some of the most frequently asked BMS questions received from users, as well as answers to other common questions about our online services. The questions are divided into several topics, which you can choose from below.", width="675").place(x=15, y=45)
        Message(self.root, text="How can you list a product?",
                 font=('arial', 8, 'bold')).place(x=15, y=110)
        Message(self.root, text="Once you register/log in, go and explore our store, if you like any books perform transactions such as add a book or \n choose one from the list of available transactions", width="675").place(x=15, y=125)
        Message(self.root, text="How does a book get rejected for sale/rent?",
                width="675", font=('arial', 8, 'bold')).place(x=15, y=160)
        Message(self.root, text="A book that includes missing pages, scribbles, and torn edges is usually the one that doesn’t make the cut. Ensure before you list it on BMS", width="675").place(x=15, y=177)
        Message(self.root, text="Is it easy to become a seller?",
                width="675", font=('arial', 8, 'bold')).place(x=15, y=213)
        Message(self.root, text="Very. As easy as it is to fall in love with a book.",
                width="675").place(x=15, y=228)
        Message(self.root, text="For Reporting Any Bug or Issues",
                width="675", font=('arial', 10, 'bold')).place(x=240, y=265)
        Message(self.root, text="Anand Ubarhande : 9421903054 || anand@bms.dev \nVasudeva Kilaru : 9959826455 || vasudeva@bms.dev \nSuraj Singh : 8827894144 || suraj@bms.dev", width="675").place(x=15, y=300)

        home = Button(self.root, text="Home", bg="light green", command=self.home)
        home.place(x=15, y=355)

        self.root.mainloop()

if __name__ == "__main__":
    Help().window()
