from tkinter import *
import mysql.connector as mysc

class interface:
    def __init__(self) :
        (self.gheight, self.gwidth) = (600, 700)
        self.dbcon = mysc.connect(host="localhost", user="root",
            password="root", database="bms")
        
    def window(self):
        root = Tk()
        root.geometry(str(self.gwidth)+"x"+str(self.gheight))
        root.title("Book Management System")
        root.resizable(False, False)
        return root