import sqlite3
import time
    
def create_table(db_name,table_name,sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("select name from sqlite_master where name=?",(table_name,))
        result=cursor.fetchall()
        keep_table=True
        if len(result) == 1:
            response = input("The table {0} already exists, do you wish to recreate it (y/n): ".format(table_name))
            if response == "y":
                keep_table=False
                print ("the {0} table will be recreated - all existing data will be lost".format(table_name))
                cursor.execute("drop table if exists {0}".format(table_name))
                db.commit()
            else:
                print ("The existing table was kept.")
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit()

def create_product_table():
    sql = """create table Product
             (ProductID integer,
             ProductName text,
             Price real,
             Stocklevel integer,
             Category text,
             NumberofSold integer,
             Primary Key(ProductID),
             Foreign Key(ProductTypeID) references
                        ProductType(ProductTypeID))
                        )"""
    create_table(db_name,"Product",sql)

def create_customer_table():
    sql = """create table Customer
             (CustomerID integer,
             CustomerName text,
             PhoneNumber integer,
             NumberofBought integer
             )"""
    create_table(db_name,"Customer",sql)

def ordering_table():
    sql = """create table Ordering
            (OrderingID integer,
            CustomerID interger,
            ProductID integer,
            DataTime text
        """
    create_table(db_name,"Ordering",sql)

def insert_product_data(values):
    with sqlite3.connect("Chirstmas_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        sql = "insert into Product (ProductID, ProductName, Price, Stocklevel, Category, NumberofSold) values (?,?,?,?,?,?)"
        cursor.execute(sql,values)
        db.commit()
        
def insert_customer_data(values):
    with sqlite3.connect("Chirstmas_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        sql = "insert into Customer (CustomerID, CustomerName, PhoneNumber, NumberofBought) values (?,?,?)"
        cursor.execute(sql,values)
        db.commit()

def insert_ordering_data(values):
    with sqlite3.connect("Chirstmas_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        sql = "insert into Ordering (OrderingID, CustomerID, ProductID, Datetime) values (?,?,?,?)"
        cursor.execute(sql,values)
        db.commit()


def update_product(data):
    with sqlite3.connect("Chirstmas_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        sql = "update Product set ProductName=?, Price=?, Stocklevel=?, Category=?, NumberofSold=? where ProductID=?"
        cursor.execute(sql,data)
        db.commit()
        
def update_customer(data):
    with sqlite3.connect("Chirstmas_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        sql = "update Customer set CustomerName=?, PhoneNumber=?,NumberofBought=? where CustomerID=?"
        cursor.execute(sql,data)
        db.commit()
        
def delete_product(data):
    with sqlite3.connect("Chirstmas_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        sql = "delete from Product where ProductName=?"
        cursor.execute(sql,data)
        db.commit()
        
def delete_customer(data):
    with sqlite3.connect("Chirstmas_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        sql = "delete from customer where CustomerName=?"
        cursor.execute(sql,data)
        db.commit()
        
def select_all_products():
    with sqlite3.connect("Chirstmas_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("select * from Product order by ProductID")
        products = cursor.fetchall()
        return products


def select_all_customers():
    with sqlite3.connect("Chirstmas_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from Customer order by CustomerID")
        customers = cursor.fetchall()
        return customers

def select_all_orderings():
    with sqlite3.connect("Chirstmas_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from Ordering order by OrderingID")
        orders = cursor.fetchall()
        return orders

def select_product(productid):
    with sqlite3.connect("Chirstmas_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("select ProductName, Price, Stocklevel, Category, NumberofSold from Product where ProductID=?",(productid,))
        products = cursor.fetchone()
        return products
    
def select_customer(customerid):
    with sqlite3.connect("Chirstmas_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("select CustomerName, PhoneNumber, Numberofbought from Customer where CustomerID=?",(customerid,))
        customers = cursor.fetchone()
        return customers
    
def select_customername(customername):
    with sqlite3.connect("Chirstmas_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("select CustomerID, PhoneNumber from Customer where CustomerName=?",(customername,))
        customers = cursor.fetchone()
        return customers
    
def select_ordering(customerid):
    with sqlite3.connect("Chirstmas_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("select ProductID, Datetime from Ordering where CustomerID=?",(customerid,))
        customers = cursor.fetchall()
        return customers

    
def top5products():
    with sqlite3.connect("Chirstmas_shop.db") as db:
        cursor = db.cursor()        
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("select * from Product order by NumberofSold DESC")
        customers = cursor.fetchall()
        return customers

def top5customers():
    with sqlite3.connect("Chirstmas_shop.db") as db:
        cursor = db.cursor()        
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("select * from Customer order by NumberofBought DESC")
        customers = cursor.fetchall()
        return customers


'''
SELECT Name, Price
FROM Product
WHERE Price > ? AND ProductID > ?
ORDER BY Name ASC, Price DESC
'''


def printmanagermenu():
    print ("---------Welcome festive shop.---------")
    print ("---------Christmas is coming.---------")
    print ()
    print ("---------Menu for MANAGER---------")
    print ()
    print ("Check and manage Products")
    print ("  1.(Re)Create Product Table")
    print ("  2.Add new Product")
    print ("  3.Check or Edit existing product")
    print ("  4.Delete existing product")
    print ("  5.Search for Top 5 products")
    print ()
    print ("Check and manage Customers")
    print ("  6.(Re)Create Customer Table")
    print ("  7.Add new Customer")
    print ("  8.Check or Edit existing Customer")
    print ("  9.Delete existing customer")
    print ("  10.Search for Customer and Order History")
    print ("  11.Search for Top 5 customers")
    print ()
    print ("  0.Exit")
    print ()

def printcustomermenu():
    print ("---------Welcome festive shop.---------")
    print ("---------Christmas is coming.---------")
    print ()
    print ("---------Menu for CUSTOMER---------")
    print ()
    print ("Check and manage Products")
    print ("  1.Check my information and history")
    print ("  2.View and purchase products")
    print ("  3.Search for Top 5 products")
    print ()
    print ("  0.Exit")
    print ()
    
if __name__ == '__main__':
    print ("Log in as Customer please input [C]")
    print ("Log in as Manager  please input [M]")
    login=input()
    if login[0]=="M" or login[0]=="m":
        while True:
            printmanagermenu()
            x=int(input("Please select an option: "))
            if x==1:
                db_name = "Chirstmas_shop.db"
                create_product_table()
            elif x==2:
                products = select_all_products()
                name=input ("Please enter name of new product: ")
                print ("ProductID is ",len(products)+1)
                productid = len(products) + 1
                price=eval(input("Please enter Price of "+name))
                stocklevel=int(input("Please enter Stocklevel of "+name))
                category=input("Please enter Category of "+name)
                sold=int(input("Please enter Number of Sold of"+name))
                product = (productid,name,price,stocklevel,category,sold)
                insert_product_data(product)
            elif x==3:
                
                products = select_all_products()
                numrows = int(len(products))
                print ()
                print ("ProductID       Name               Price       Stocklevel         Category")
                for i in range(numrows):
                    row = products[i]
                    print ("    ",row[0],end="")
                    for k in range (0,7-len(str(row[0]))):
                        print (" ",end="")
                    print (row[1],end="")
                    for k in range (0,18-len(str(row[1]))):
                        print (" ",end="")
                    print ("    ",row[2],end="   ")
                    for k in range (0,7-len(str(row[2]))):
                        print (" ",end="")
                    print ("    ",row[3],end=" ")
                    for k in range (0,3-len(str(row[3]))):
                        print (" ",end="")
                    print ("    ",row[4])
                    print ()
                
                f=input("Do you want to Edit product? (y/n)")
                if f[0]=="Y" or f[0]=="y":
                    productid=int(input("Please input the ID of product you want to change: "))
                    name=input ("Please enter the new name of product: ")
                    price=eval(input("Please enter Price of "+name))
                    stocklevel=int(input("Please enter Stocklevel of "+name))
                    category=input("Please enter Category of "+name)
                    
                    sold=int(input("Please enter Number of Sold of"+name))
                    data = (name,price,stocklevel,category,sold,productid)
                    
                    update_product(data)
    
                
            elif x==4:
                data=(input("Please enter the name of product you want delete: "),)
                delete_product(data)
            elif x==5:
                
                products = top5products()
                print ()
                print ("ProductID       Name            NumberofSold")
                for i in range(0,5):
                    row = products[i]
                    print ("    ",row[0],end="")
                    for k in range (0,7-len(str(row[0]))):
                        print (" ",end="")
                    print (row[1],end="")
                    for k in range (0,18-len(str(row[1]))):
                        print (" ",end="")
                    for k in range (0,7-len(str(row[5]))):
                        print (" ",end="")
                    print ("   ",row[5],end="    ")
                    if int(row[3])<5:
                        print("NOTICE The stock level less than 5",end="")
                    print ()
                
            elif x==6:
                db_name = "Chirstmas_shop.db"
                create_customer_table()
            elif x==7:
                customers = select_all_customers()
                name=input ("Please enter name of new customer: ")
                print ("CustomerID is ",len(customers)+1)
                customerid = len(customers) + 1
                customerphober=input("Please enter phone number of "+name)
                customer = (customerid,name,customerphober)
                insert_customer_data(customer)
            elif x==8:
                customers = select_all_customers()
                numrows = int(len(customers))
                print ()
                print ("CustomerID            Name        Customer Phonenumber")
                for i in range(numrows):
                    row = customers[i]
                    print ("    ",row[0],end="")
                    for k in range (0,17-len(str(row[0]))):
                        print (" ",end="")
                    print (row[1],end="")
                    for k in range (0,8-len(str(row[1]))):
                        print (" ",end="")
                    print ("    ",row[2],end="   ")
                    
                    print ()
                
                f=input("Do you want to Edit Customer? (y/n)")
                if f[0]=="Y" or f[0]=="y":
                    customerid=int(input("Please input the ID of customer you want to change: "))
                    name=input ("Please enter the new name of customer: ")
                    customerphober=input("Please enter Phone number of "+name)

                    data = (name,customerphober,customerid)
                    
                    update_customer(data)
            elif x==9:
                data=(input("Please enter the name of customer you want delete: "),)
                delete_customer(data)
            elif x==10:
                customers = select_all_customers()
                numrows = int(len(customers))
                print ()
                print ("CustomerID            Name        Customer Phonenumber")
                for i in range(numrows):
                    row = customers[i]
                    print ("    ",row[0],end="")
                    for k in range (0,17-len(str(row[0]))):
                        print (" ",end="")
                    print (row[1],end="")
                    for k in range (0,8-len(str(row[1]))):
                        print (" ",end="")
                    print ("    ",row[2],end="   ")
                    print ()    
                print ()
                customerid=int(input("Please enter the id you want to check"))
                customers=select_customer(customerid)
                print ()
                print ("CustomerID            Name        Customer Phonenumber")
                print ("    ",customerid,end="")
                for k in range (0,7-len(str(customerid))):
                    print ("  ",end="")
                print (customers[0],end="")
                for k in range (0,18-len(str(customers[0]))):
                    print (" ",end="")
                for k in range (0,7-len(str(customers[1]))):
                    print (" ",end="")
                print ("  ",customers[1],end=" ")
                print ()
                print ()
                print ("Datatime             ProductID       ProductName")
                orders=(select_ordering(customerid))
                numrows=int(len(orders))
                for i in range(numrows):
                    row = orders[i]
                    print (row[1],end="")
                    for k in range (0,20-len(str(row[1]))): 
                        print (" ",end="")
                    print ("   ",row[0],end="            ")
                    name=(select_product(int(row[0])))
                    print (name[0])
                    print()
                print ()
                print ()
            elif x==11:
                customers = top5customers()
                print ()
                print ("CustomerID        Name        NumberofBought       Money spent      Profit generated")
                for i in range(0,5):
                    s=0
                    row = customers[i]
                    print ("    ",row[0],end="")
                    for k in range (0,7-len(str(row[0]))):
                        print ("  ",end="")
                    print (row[1],end="")
                    for k in range (0,8-len(str(row[1]))):
                        print (" ",end="")
                    for k in range (0,7-len(str(row[3]))):
                        print (" ",end="")
                    print ("  ",row[3],end=" ")
                    

                    orders=(select_ordering(row[0]))
                    numrows=int(len(orders))
                    for j in range(numrows):
                        rowj = orders[j]
                        a=select_product(int(rowj[0]))
                        s=s+int(a[1])  
                    print ("             ",s,end="")
                    for k in range (0,7-len(str(s))):
                        print (" ",end="")
                    print ("          ",s*0.1,end="")
                    print ()

            elif x==0:
                break
            
            input("Press any to continue")
            print()
    elif login[0]=="C" or login[0]=="c":
        
        name=input("Please input your name to log in")

        customer=select_customername(name)
        if customer==None:  
            print ("You are a new user. Please answer questions to register.")
            customers = select_all_customers()
            print ("CustomerID is ",len(customers)+1)
            customerid = len(customers) + 1
            customerphober=input("Please enter phone number of "+name)
            customer = (customerid,name,customerphober)
            insert_customer_data(customer)
        
        while True:
            printcustomermenu()
            x=int(input("Please select an option: "))
            if x==1:
                customers = select_all_customers()
                customer=select_customername(name)
                customerid=int(customer[0])
                customers=select_customer(customerid)
                print ()
                print ("CustomerID           Name        Customer Phonenumber")
                print ("    ",customerid,end="")
                for k in range (0,7-len(str(customerid))):
                    print ("  ",end="")
                print (" ",customers[0],end="")
                for k in range (0,18-len(str(customers[0]))):
                    print (" ",end="")
                for k in range (0,7-len(str(customers[1]))):
                    print (" ",end="")
                print ("  ",customers[1],end=" ")
                print ()
                print ()
                print ("                 My Order History")
                print ("Datatime             ProductID       ProductName")
                orders=(select_ordering(customerid))
                numrows=int(len(orders))
                for i in range(numrows):
                    row = orders[i]
                    print (row[1],end="")
                    for k in range (0,20-len(str(row[1]))): 
                        print (" ",end="")
                    print ("   ",row[0],end="            ")
                    name=(select_product(int(row[0])))
                    print (name[0])
                    print()
                print ()
                print ()
            elif x==2:
                products = select_all_products()
                numrows = int(len(products))
                print ()
                print ("ProductID       Name               Price       Stocklevel         Category")
                for i in range(numrows):
                    row = products[i]
                    print ("    ",row[0],end="")
                    for k in range (0,7-len(str(row[0]))):
                        print (" ",end="")
                    print (row[1],end="")
                    for k in range (0,18-len(str(row[1]))):
                        print (" ",end="")
                    print ("    ",row[2],end="   ")
                    for k in range (0,7-len(str(row[2]))):
                        print (" ",end="")
                    print ("    ",row[3],end=" ")
                    for k in range (0,3-len(str(row[3]))):
                        print (" ",end="")
                    print ("    ",row[4])
                    print ()

                productid=int(input("Please input the id of product you want to buy, enter 0 to finish and pay."))
                while productid!=0:
                    orders=select_all_orderings()
                    datetime=time.strftime('%H:%M:%S %d-%m-%Y',time.localtime(time.time()))
                    value=(len(orders)+1, customer[0], productid, datetime)
                    insert_ordering_data(value)

                    product=(select_product(productid))
                    data=(product[0], product[1], int(product[2])-1, product[3], int(product[4])+1,productid)           
                    update_product(data)

                    customers = select_all_customers()
                    customer=select_customername(name)
                    customerid=int(customer[0])
                    customer=(select_customer(customerid))
                    print (customer)
                    cdata=(customer[0], customer[1], int(customer[2])+1,customerid)           
                    update_customer(cdata)
                    productid=int(input())                
            elif x==3:
                products = top5products()
                print ()
                print ("ProductID       Name            NumberofSold")
                for i in range(0,5):
                    row = products[i]
                    print ("    ",row[0],end="")
                    for k in range (0,7-len(str(row[0]))):
                        print (" ",end="")
                    print (row[1],end="")
                    for k in range (0,18-len(str(row[1]))):
                        print (" ",end="")
                    for k in range (0,7-len(str(row[5]))):
                        print (" ",end="")
                    print ("   ",row[5],end="    ")
                    print ()
            elif x==0:
                break
            input("Press any to continue")
            print()

         
