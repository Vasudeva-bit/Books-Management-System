from tkinter import *
import mysql.connector as mysc
from tkinter import messagebox
import app

def viewBooks():
 
    global id
    def __init__(self):
        self.root = app().self.root()

    def window(self):
        Label(self.root,width="300",height="2", text="View Books", bg="green yellow",fg="black").pack()
    
        db = mysc.connect(host ="localhost",user = "root",password = 'root',database='bms')
        cursor = db.cursor()
    
        Squery= "select * from books;"
        print(Squery)
    
        try:
            cursor.execute(Squery)
            # db.commit()
            L = Label(self.root, text = "%-10s%-20s%-20s%-20s"%('BID','Title','Author','Available'))
            L.place(x=220,y=60)
    
            L = Label(self.root, text = "----------------------------------------------------------------")
            L.place(x=185,y=75)
    
            x=4
            for i in cursor:
                L = Label(self.root, text = "%-10s%-20s%-20s%-20s"%(i[0],i[1],i[2],i[3]))
                L.place(x=220,y=100)
                x+=1   
    
        except:
            messagebox.showinfo("Error","Cannot Fetch data.")
        
        print("view")


    def add_db(self):
    
        global id
        global title
        global author
    
        bid=id.get()
        btitle=title.get()
        bauthor=author.get()
        
        db = mysc.connect(host ="localhost",user = "root",password = 'Root',database='bms')
        cursor = db.cursor()
        
        print(bid,end='--')
        print(btitle,end='--')
        print(bauthor,end='--')
        print("add")
    
        sqlquery= "insert into books values('" + bid +"','"+btitle+"','"+bauthor+"','YES');"
        print(sqlquery)
    
        try:
            cursor.execute(sqlquery)
            db.commit()
            messagebox.showinfo('Success',"Book added Successfully")
        except:
            messagebox.showinfo("Error","Cannot add given book data into Database")
        
        self.root.destroy()
    
    def addBooks(self):
    
        global id
        global title
        global author
    
        self.root=Tk()
        self.root.title('Add Books')
        self.root.geometry('500x400+500+100')
    
        Label(self.root,width="300",height="2", text="Add Books", bg="green yellow",fg="black").pack()
    
        #----------id-------------------
    
        L = Label(self.root, text = "Enter Book id: ")
        L.place(x=120,y=60)
    
        L = Label(self.root, text = "   ")
        L.place(x=210,y=60)
    
        id=Entry(self.root,width=15)
        id.place(x=210,y=60)
    
        #----------title-------------------
    
        L = Label(self.root, text = "Enter Title: ")
        L.place(x=120,y=100)
    
        L = Label(self.root, text = "   ")
        L.place(x=210,y=100)
    
        title=Entry(self.root,width=15)
        title.place(x=210,y=100)
    
        #----------author-------------------
    
        L = Label(self.root, text = "Enter Author: ")
        L.place(x=120,y=140)
    
        L = Label(self.root, text = "   ")
        L.place(x=210,y=140)
    
        author=Entry(self.root,width=15)
        author.place(x=210,y=140)
        
        submitbtn=Button(self.root,text="Submit",command=add_db,bg="lawn green",font = ('arial', 15, 'bold'))
        submitbtn.place(x=200,y=200)
            
        print("add")

    
    def delete_db(self):
    
        global id
    
        bid=id.get()
        
        db = mysc.connect(host ="localhost",user = "root",password = 'Root',database='bms')
        cursor = db.cursor()
        
        print(bid,end='--')
        print("delete")
    
        sqlquery= "delete from books where bid='"+bid+"';"
        print(sqlquery)
    
        try:
            cursor.execute(sqlquery)
            db.commit()
            messagebox.showinfo('Success',"Book deleted Successfully")
        except:
            messagebox.showinfo("Error","Book with given id does not exist")
        
        self.root.destroy()
    
    def deleteBooks(self):
    
        global id
    
        self.root=Tk()
        self.root.title('Delete Books')
        self.root.geometry('500x300+500+100')
    
        Label(self.root,width="300",height="2", text="Delete Books", bg="green yellow",fg="black").pack()
        
        L = Label(self.root, text = "Enter Book id: ")
        L.place(x=130,y=80)
    
        L = Label(self.root, text = "   ")
        L.place(x=220,y=80)
    
        id=Entry(self.root,width=20)
        id.place(x=220,y=80)
    
        submitbtn=Button(self.root,text="Submit",command=delete_db,bg="lawn green",font = ('arial', 15, 'bold'))
        submitbtn.place(x=200,y=130)
            
        print("delete")
        pass

    def issue_db():
    
        global id
        global StudentName
    
        bid=id.get()
        bStudentName=StudentName.get()
    
        db = mysc.connect(host ="localhost",user = "root",password = 'Root',database='bms')
        cursor = db.cursor()
        
        print(bid,end='--')
        print(bStudentName,end='--')
        print("issue")
    
        try:
            checkavailability=" select * from books where available='YES';"
            print(checkavailability)
            cursor.execute(checkavailability)
    
            flag=0
    
            for i in cursor:
                print(i[0])
                if(i[0]==bid):
                    flag=1
                    break;
            
            if flag==1:     
                updatequery="update books set available='NO' where bid='"+bid +"';"
                print(updatequery)
                cursor.execute(updatequery)
                db.commit()
    
                sqlquery= "insert into issue values('" + bid +"','" +bStudentName+"' );"
                print(sqlquery)
    
                cursor.execute(sqlquery)
                db.commit()
    
                messagebox.showinfo('Success',"Book issued Successfully")
            else:
                messagebox.showinfo("Error","Required Book is not available")
        except:
            messagebox.showinfo("Error","Cannot issue given book ")
        
    def issueBooks(self):
    
        global id
        global StudentName
    
        self.root=Tk()
        self.root.title('Issue Books')
        self.root.geometry('500x300+500+100')
    
        Label(self.root,width="300",height="2", text="Issue Books", bg="green yellow",fg="black").pack()
        
        L = Label(self.root, text = "Enter Book id: ")
        L.place(x=140,y=70)
    
        L = Label(self.root, text = "   ")
        L.place(x=260,y=70)
    
        id=Entry(self.root,width=15)
        id.place(x=260,y=70)
        
        L = Label(self.root,text = "Enter StudentName: ")
        L.place(x=140,y=110)
    
        L = Label(self.root, text = "   ")
        L.place(x=260,y=110)
    
        StudentName=Entry(self.root,width=15)
        StudentName.place(x=260,y=110)
        
        submitbtn=Button(self.root,text="Submit",command=issue_db,bg="lawn green",font = ('arial', 15, 'bold'))
        submitbtn.place(x=220,y=180)
            
        print("issue")

    def return_db():
        bid=id.get()
    
        db = mysc.connect(host ="localhost",user = "root",password = 'Root',database='bms')
        cursor = db.cursor()
        
        print(bid,end='--')
        print("return")
    
        try:
            checkavailability=" select * from books where available='NO';"
            print(checkavailability)
            cursor.execute(checkavailability)
    
            flag=0
    
            for i in cursor:
                print(i[0])
                if(i[0]==bid):
                    flag=1
                    break
            
            if flag==1:     
                updatequery="update books set available='YES' where bid='"+bid +"';"
                print(updatequery)
                cursor.execute(updatequery)
                db.commit()
    
                sqlquery= "delete from issue where bid='" + bid +"';"
                print(sqlquery)
    
                cursor.execute(sqlquery)
                db.commit()
    
                messagebox.showinfo('Success',"Book returned Successfully")
            else:
                messagebox.showinfo("Error","Invalid Book id")
        except:
            messagebox.showinfo("Error","Cannot return given book ")
        
    def returnBooks(self):
        self.root=Tk()
        self.root.title('Return Books')
        self.root.geometry('500x300+500+100')
    
        Label(self.root,width="300",height="2", text="Return Books", bg="green yellow",fg="black").pack()
    
        L = Label(self.root, text = "Enter Book id: ")
        L.place(x=130,y=80)
    
        L = Label(self.root, text = "   ")
        L.place(x=220,y=80)
    
        id=Entry(self.root,width=20)
        id.place(x=220,y=80)
    
        
        submitbtn=Button(self.root,text="Submit",command=return_db,bg="lawn green",font = ('arial', 15, 'bold'))
        submitbtn.place(x=200,y=130)
            
        print("return")