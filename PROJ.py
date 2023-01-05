#Importing the required modules
import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
import mysql.connector
from datetime import datetime
import math
import turtle

# Connecting to the database and creating table
db = mysql.connector.connect(user="root", passwd="Sonu2005", host="localhost")

my_cursor = db.cursor()  # getting the cursor object
my_cursor.execute("CREATE DATABASE IF NOT EXISTS Shop")  # creating the database named library

db = mysql.connector.connect(user="root", passwd="Sonu2005", host="localhost", database='Shop')
my_cursor = db.cursor()
# query to create a table products
query = "CREATE TABLE IF NOT EXISTS products (prodName VARCHAR(20), prodPrice VARCHAR(50),mfg varchar(50), exp VARCHAR(50), stock VARCHAR(50))"
my_cursor.execute(query)  # executing the query

db = mysql.connector.connect(user="root", passwd="Sonu2005", host="localhost", database='Shop')
my_cursor = db.cursor()
# query to create a table sale
query = "CREATE TABLE IF NOT EXISTS sale (custName VARCHAR(20), date VARCHAR(10), prodName VARCHAR(30),qty INTEGER, price INTEGER )"
my_cursor.execute(query)  # executing the query

# TURTLE PAGE

screen = turtle.Screen()
screenTk = screen.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", True)

a = turtle.Turtle()
a.hideturtle()

turtle.bgcolor("black")

a.penup()

a.color("White")

a.goto(-200,250)
a.write("WELCOME TO ",font=("Verdana",40, "normal"))
a.penup()
a.goto(-550,175)
a.pendown()
a.width(5)
a.write("ASSS DISCOUNT MANAGEMENT SYSTEM",font=("Castellar",40, "bold"))

a.penup()
a.goto(-600,150)
a.pendown()
a.width(5)
a.speed(100)
a.forward(1200)



a.penup()
a.goto(-600,-50)
a.pendown()

a.width(0)
a.write("LOADING",font=("Verdana",20, "normal"))

a.penup()
a.goto(-600,-70)
a.pendown()

a.width(2)
a.speed(3)
a.forward(1200)
a.speed(0)
a.penup()
a.goto(-100,-150)
a.pendown()

a.width(3)



for i in range(2):
    a.forward(200)
    a.right(90)
    a.forward(100)
    a.right(90)

a.penup()
a.goto(-100,-250)
a.write("NEXT",font=("Castellar",45, "bold"))

def button(x,y):
    if x < 100 and x > -100 and y < -150 and y > -250:
        turtle.Screen().bye()
turtle.onscreenclick(button, 1, add=True)

turtle.done()

# MAIN GUI PAGE

# Function to add the product to the database
def prodtoTable():
    # Getting the user inputs of product details from the user
    pname = prodName.get()
    price = prodPrice.get()
    mfg = mfgdate.get()
    exp = expdate.get()
    quantity = stock.get()

    # Connecting to the database
    db = mysql.connector.connect(user="root", passwd="Sonu2005", host="localhost", database='Shop')
    cursor = db.cursor()

    # query to add the product details to the table
    query = "INSERT INTO products(prodName,prodPrice,mfg,exp,stock) VALUES(%s,%s,%s,%s,%s)"
    details = (pname,price,mfg,exp,quantity)

    # Executing the query and showing the pop up message
    try:
        cursor.execute(query, details)
        db.commit()
        messagebox.showinfo('Success', "Product added successfully")

    except Exception as e:
        print("The exception is:", e)
        messagebox.showinfo("Error", "Trouble adding data into Database")

    # Getting the mfg
    cursor.execute("Select mfg from products")
    myresult = cursor.fetchall()
    l = len(myresult)
    mfgtuple = myresult[l - 1]
    mfglist = list(mfgtuple)

    mfglistfirst = mfglist[0]
    mfgdatestring = str(mfglistfirst)

    mfgdate_object = datetime.strptime(mfgdatestring, '%d-%m-%Y').date()

    # Getting the exp
    cursor.execute("Select exp from products")
    myresult = cursor.fetchall()
    l = len(myresult)
    exptuple = myresult[l - 1]
    explist = list(exptuple)

    explistfirst = explist[0]
    expdatestring = str(explistfirst)

    expdate_object = datetime.strptime(expdatestring, '%d-%m-%Y').date()

    delta = expdate_object-mfgdate_object
    a = (delta.days)/30
    productlife = math.floor(a)


    # Getting the mrp
    cursor.execute("Select prodprice from products")
    myresult = cursor.fetchall()
    l = len(myresult)
    pricetuple = myresult[l-1]
    pricelist = list(pricetuple)

    pricelistfirst = pricelist[0]
    priceint = int(pricelistfirst)

    #Getting the stock
    cursor.execute("Select stock from products")
    myresult = cursor.fetchall()
    l=len(myresult)
    stocktuple = myresult[l-1]
    stocklist=list(stocktuple)

    stocklistfirst = stocklist[0]
    stockint=int(stocklistfirst)

    #Connecting to the main database
    my_cursor.execute("Create table if not exists inventory(PRODUCT_NAME varchar(20),MRP int,MFG date,EXP date,STOCK int,PRODUCT_LIFE int)")
    db = mysql.connector.connect(user="root", passwd="Sonu2005", host="localhost", database='Shop')
    cursor = db.cursor()

    #Inserting the values
    sql = "Insert into inventory(PRODUCT_NAME, MRP, MFG, EXP, STOCK, PRODUCT_LIFE) VALUES(%s,%s,%s,%s,%s,%s)"
    val = (pname,priceint,mfgdate_object,expdate_object,stockint,productlife)
    cursor.execute(sql,val)
    db.commit()


    wn.destroy()


# Function to get details of the product to be added
def addProd():
    global prodName, prodPrice, mfgdate, expdate, stock, Canvas1, wn

    # Creating the window
    wn = tkinter.Tk()
    wn.title("ASSS Shop Management System")
    wn.configure(bg='mint cream')
    wn.minsize(width=500, height=500)
    wn.attributes('-fullscreen', True)
    Canvas1 = Canvas(wn)
    Canvas1.config(bg='LightBlue1')
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(wn, bg='LightBlue1', bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="Add a Product", fg='grey19', font=('Courier', 15, 'bold'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(wn)
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # Getting Date
    lable1 = Label(labelFrame, text="Date : ", fg='black')
    lable1.place(relx=0.05, rely=0.3, relheight=0.08)

    date = Entry(labelFrame)
    date.place(relx=0.3, rely=0.3, relwidth=0.62, relheight=0.08)

    # Product Name
    lable1 = Label(labelFrame, text="Product Name : ", fg='black')
    lable1.place(relx=0.05, rely=0.1, relheight=0.08)

    prodName = Entry(labelFrame)
    prodName.place(relx=0.3, rely=0.1, relwidth=0.62, relheight=0.08)

    # Product Price
    lable2 = Label(labelFrame, text="Product Price : ", fg='black')
    lable2.place(relx=0.05, rely=0.2, relheight=0.08)

    prodPrice = Entry(labelFrame)
    prodPrice.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # Getting MFG Date
    label3 = Label(labelFrame, text="MFG-Date : ", fg="black")
    label3.place(relx=0.05, rely=0.3, relheight=0.08)

    mfgdate = Entry(labelFrame)
    mfgdate.place(relx=0.3, rely=0.3, relwidth=0.62, relheight=0.08)

    # Getting EXP Date
    lable4 = Label(labelFrame, text="EXP-Date : ", fg='black')
    lable4.place(relx=0.05, rely=0.4, relheight=0.08)

    expdate = Entry(labelFrame)
    expdate.place(relx=0.3, rely=0.4, relwidth=0.62, relheight=0.08)

    # Getting the stock
    lable5 = Label(labelFrame, text="Stock : ", fg='black')
    lable5.place(relx=0.05, rely=0.5, relheight=0.08)

    stock = Entry(labelFrame)
    stock.place(relx=0.3, rely=0.5, relwidth=0.62, relheight=0.08)


    # Add Button
    Btn = Button(wn, text="ADD", bg='#d1ccc0', fg='black', command=prodtoTable)
    Btn.place(relx=0.28, rely=0.85, relwidth=0.18, relheight=0.08)

    Quit = Button(wn, text="Quit", bg='#f7f1e3', fg='black', command=wn.destroy)
    Quit.place(relx=0.53, rely=0.85, relwidth=0.18, relheight=0.08)

    wn.mainloop()


# Function to remove the product from the database
def removeProd():
    # Getting the product name from the user to be removed
    name = prodName.get()
    name = name.lower()

    # Connecting to the database
    db = mysql.connector.connect(user="root", passwd="Sonu2005", host="localhost", database='Shop')
    cursor = db.cursor()

    # Query to delete the respective product from the database
    query = "DELETE from products where LOWER(prodName) = '" + name + "'"
    # Executing the query and showing the message box
    try:
        cursor.execute(query)
        db.commit()
        # cur.execute(deleteIssue)
        # con.commit()

        messagebox.showinfo('Success', "Product Record Deleted Successfully")

    except Exception as e:
        print("The exception is:", e)
        messagebox.showinfo("Please check Product Name")

    wn.destroy()


# Function to get product details from the user to be deleted
def delProd():
    global prodName, Canvas1, wn
    # Creating a window
    wn = tkinter.Tk()
    wn.title("ASSS Shop Management System")
    wn.configure(bg='mint cream')
    wn.minsize(width=500, height=500)
    wn.geometry("700x600")

    Canvas1 = Canvas(wn)
    Canvas1.config(bg="misty rose")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(wn, bg="misty rose", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="Delete Product", fg='grey19', font=('Courier', 15, 'bold'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(wn)
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Product Name to Delete
    lable = Label(labelFrame, text="Product Name : ", fg='black')
    lable.place(relx=0.05, rely=0.5)

    prodName = Entry(labelFrame)
    prodName.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Delete Button
    Btn = Button(wn, text="DELETE", bg='#d1ccc0', fg='black', command=removeProd)
    Btn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    Quit = Button(wn, text="Quit", bg='#f7f1e3', fg='black', command=wn.destroy)
    Quit.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    wn.mainloop()


# Function to show all the products in the database
def viewProds():
    global wn
    # Creating the window to show the products details
    wn = tkinter.Tk()
    wn.title("ASSS Shop Management System")
    wn.configure(bg='mint cream')
    wn.minsize(width=500, height=500)
    wn.geometry("700x600")

    Canvas1 = Canvas(wn)
    Canvas1.config(bg="old lace")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(wn, bg='old lace', bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Products", fg='black', font=('Courier', 15, 'bold'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(wn)
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    y = 0.25

    # Connecting to database
    db = mysql.connector.connect(user="root", passwd="Sonu2005", host="localhost", database='Shop')
    cursor = db.cursor()
    # query to select all products from the table
    query = 'SELECT * FROM products'

    Label(labelFrame, text="%-35s%-35s%-35s%-35s%-35s" % ("PRODUCT","PRICE","MFG","EXP","STOCK"), font=('calibri', 11, 'bold'),
          fg='black').place(relx=0.07, rely=0.1)
    Label(labelFrame, text="--------------------------------------------------------------------------------------------------------------------------",
          fg='black').place(relx=0.05, rely=0.2)
    # Executing the query and showing the products details
    try:
        cursor.execute(query)
        res = cursor.fetchall()

        for i in res:
            Label(labelFrame, text="%-45s%-35s%-35s%-35s%-40s" % (i[0], i[1], i[2], i[3], i[4]), fg='black').place(relx=0.07, rely=y)
            y += 0.1
    except Exception as e:
        print("The exception is:", e)
        messagebox.showinfo("Failed to fetch files from database")

    Quit = Button(wn, text="Quit", bg='#f7f1e3', fg='black', command=wn.destroy)
    Quit.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    wn.mainloop()

# Function to close the window
def update():
    
    global wn, newprodName, newprodPrice
    # Creating the window to show the products details
    wn = tkinter.Tk()
    wn.title("ASSS Shop Management System")
    wn.configure(bg='mint cream')
    wn.minsize(width=500, height=500)
    wn.geometry("700x600")

    Canvas1 = Canvas(wn)
    Canvas1.config(bg="old lace")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(wn, bg='old lace', bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Update Stock", fg='black', font=('Courier', 15, 'bold'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(wn)
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    y = 0.25

     # Product Name
    lable1 = Label(labelFrame, text="Product Name : ", fg='black')
    lable1.place(relx=0.05, rely=0.1, relheight=0.08)

    newprodName = Entry(labelFrame)
    newprodName.place(relx=0.3, rely=0.1, relwidth=0.62, relheight=0.08)

    # Product Price
    lable2 = Label(labelFrame, text="Product Price : ", fg='black')
    lable2.place(relx=0.05, rely=0.2, relheight=0.08)

    newprodPrice = Entry(labelFrame)
    newprodPrice.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # Update Button
    Btn = Button(wn, text="UPDATE", bg='#d1ccc0', fg='black', command = updateprice)
    Btn.place(relx=0.28, rely=0.85, relwidth=0.18, relheight=0.08)

    Quit = Button(wn, text="Quit", bg='#f7f1e3', fg='black', command=wn.destroy)
    Quit.place(relx=0.53, rely=0.85, relwidth=0.18, relheight=0.08)

    wn.mainloop()



# Function to generate the bill
def bill():
    # Creating a window
    wn = tkinter.Tk()
    wn.title("ASSS Shop Management System")
    wn.configure(bg='lavender blush2')
    wn.minsize(width=500, height=500)
    wn.geometry("700x600")

    

    wn.mainloop()


def updateprice():
    # Connecting to database
    db = mysql.connector.connect(user="root", passwd="Sonu2005", host="localhost", database='Shop')
    cursor = db.cursor()

    # Getting the values
    newpname = newprodName.get()
    newprice = newprodPrice.get()

    #Inserting the values
    sql = "UPDATE PRODUCTS SET prodPrice= %s WHERE prodname= %s"
    val = (newprice, newpname)
    try:
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo('Success', "Price changed successfully")

    except Exception as e:
        print("The exception is:", e)
        messagebox.showinfo("Error", "Trouble updating price")

    # Getting the mrp
    sql = "Select prodprice from products where prodName = %s"
    val = newpname
    cursor.execute(sql, val)
    myresult = cursor.fetchall()
    print(myresult)




# Function to take the inputs form the user to generate bill
def newCust():
    global wn, name1, name2, name3, date, custName
    # Creating a window
    wn = tkinter.Tk()
    wn.title("ASSS Shop Management System")
    wn.configure(bg='lavender blush2')
    wn.minsize(width=500, height=500)
    wn.geometry("700x600")

    

    wn.mainloop()

def discount():
    global wn, name1, name2, name3, date, custName
    # Creating a window
    wn = tkinter.Tk()
    wn.title("ASSS Shop Management System")
    wn.configure(bg='lavender blush2')
    wn.minsize(width=500, height=500)
    wn.geometry("700x600")

    

    wn.mainloop()




#Creating the main window
wn = tkinter.Tk()
wn.title("ASSS Shop Management System")
wn.configure(bg='#ff3300')

wn.attributes('-fullscreen', True)
headingFrame1 = Frame(wn,bg="#66ccff",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="I DECIDED TO BECOME A BUSINESSMAN \n BECAUSE THE THING I AM GOOD AT IS BUSINESS....", fg='grey19',bg = "#ffff00", font=('Courier',15,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

#Button to add a new product
frame_add = Frame(wn, width=200, height=200)
frame_add.pack()
frame_add.place(anchor='center', relx=0.25,rely=0.425)

#Load an image in the script
img= (Image.open("product-add-to-cart-e1438362099361.png"))

#Resize the Image using resize method
resized_image_add= img.resize((175,175), Image.ANTIALIAS)
new_image_add= ImageTk.PhotoImage(resized_image_add)

# Create a Label Widget to display the text or Image
label = Label(frame_add, image = new_image_add)
label.pack()

btn1 = Button(wn,text="Add a Product",bg='#8cff66', fg='black', width=20,height=2, command=addProd)
btn1['font'] = font.Font( size=12)
btn1.place(relx=0.18,rely=0.55)

#Button to delete a product
frame_del = Frame(wn, width=200, height=200)
frame_del.pack()
frame_del.place(anchor='center', relx=0.5,rely=0.425)

#Load an image in the script
img= (Image.open("remove-cart-icon-delete-shopping-cart-well-organized-fully-editable-remove-cart-icon-delete-shopping-cart-any-167546275.jpg"))

#Resize the Image using resize method
resized_image_del= img.resize((175,175), Image.ANTIALIAS)
new_image_del= ImageTk.PhotoImage(resized_image_del)

# Create a Label Widget to display the text or Image
label = Label(frame_del, image = new_image_del)
label.pack()

btn2 = Button(wn,text="Delete a Product",bg='#66ff33', fg='black',width=20,height=2,command=delProd)
btn2['font'] = font.Font( size=12)
btn2.place(relx=0.43,rely=0.55)

#Button to view all products
frame_view = Frame(wn, width=200, height=200)
frame_view.pack()
frame_view.place(anchor='center', relx=0.75,rely=0.425)

#Load an image in the script
img= (Image.open("isolated-shopping-cart-with-products-design-vector-30793897.jpg"))

#Resize the Image using resize method
resized_image_view= img.resize((175,175), Image.ANTIALIAS)
new_image_view= ImageTk.PhotoImage(resized_image_view)

# Create a Label Widget to display the text or Image
label = Label(frame_view, image = new_image_view)
label.pack()
btn3 = Button(wn,text="View Products",bg='#39e600', fg='black',width=20,height=2,command=viewProds)
btn3['font'] = font.Font( size=12)
btn3.place(relx=0.68,rely=0.55)

#Button to add a new sale and generate bill
frame_sale = Frame(wn, width=200, height=200)
frame_sale.pack()
frame_sale.place(anchor='center', relx=0.25,rely=0.8)

#Load an image in the script
img= (Image.open("499-4992295_customer-first-icon-png-download-new-member-icon.png"))

#Resize the Image using resize method
resized_image_sale= img.resize((175,175), Image.ANTIALIAS)
new_image_sale= ImageTk.PhotoImage(resized_image_sale)

# Create a Label Widget to display the text or Image
label = Label(frame_sale, image = new_image_sale)
label.pack()

btn4 = Button(wn,text="New Customer",bg='#33cc00', fg='black', width=20,height=2,command = newCust)
btn4['font'] = font.Font( size=12)
btn4.place(relx=0.18,rely=0.925)


#Button to VIEW DISCOUNT
frame_dis = Frame(wn, width=200, height=200)
frame_dis.pack()
frame_dis.place(anchor='center', relx=0.5,rely=0.8)

#Load an image in the script
img= (Image.open("images.png"))

#Resize the Image using resize method
resized_image_dis= img.resize((175,175), Image.ANTIALIAS)
new_image_dis= ImageTk.PhotoImage(resized_image_dis)

# Create a Label Widget to display the text or Image
label = Label(frame_dis, image = new_image_dis)
label.pack()

btn5 = Button(wn,text="View Discount",bg='#00cc00', fg='black', width=20,height=2, command=discount)
btn5['font'] = font.Font( size=12)
btn5.place(relx=0.43,rely=0.925)

#Button to update the mrp of a product
frame_exit = Frame(wn, width=200, height=200)
frame_exit.pack()
frame_exit.place(anchor='center', relx=0.75,rely=0.8)

#Load an image in the script
img= (Image.open("kisspng-computer-icons-check-mark-icon-design-quit-5b3dd1d57dfe49.1894119415307780695161.jpg"))

#Resize the Image using resize method
resized_image_exit= img.resize((175,175), Image.ANTIALIAS)
new_image_exit= ImageTk.PhotoImage(resized_image_exit)

# Create a Label Widget to display the text or Image
label = Label(frame_exit, image = new_image_exit)
label.pack()

btn6 = Button(wn,text="UPDATE",bg='#00cc00', fg='black', width=20,height=2, command=update)
btn6['font'] = font.Font( size=12)
btn6.place(relx=0.68,rely=0.925)

# Button to exit the main project
frame_exit = Frame(wn, width=50, height=50)
frame_exit.pack()
frame_exit.place(anchor='center', relx=0.9,rely=0.09)

#Load an image in the script
img= (Image.open("kisspng-computer-icons-check-mark-icon-design-quit-5b3dd1d57dfe49.1894119415307780695161.jpg"))

#Resize the Image using resize method
resized_image_exit= img.resize((50,50), Image.ANTIALIAS)
new_image_exit= ImageTk.PhotoImage(resized_image_exit)

# Create a Label Widget to display the text or Image
label = Label(frame_exit, image = new_image_exit)
label.pack()

btn6 = Button(wn,text="UPDATE",bg='#00cc00', fg='black', width=10,height=2, command=update)
btn6['font'] = font.Font( size=5)
btn6.place(relx=0.875,rely=0.12)




wn.mainloop()
