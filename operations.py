#Module: Operations
'''
Objectives:
    - To ask user information about the products they want to purchase
    - To calculate the total price of the product, including vat and shipping cost for sell
    - To update the stock of products in text file as well as in 2d list
    - To generate receipt'''

#Importing necessary modules
import read
import write
import datetime

#Extracting 2d list from read module
BRJfurniture = read.listt()

#Creating a funtion to ask information from users and performing necessary calculations
def sell():
    read.fo()
    transactions = []
    
    cname = input ("Enter your name: ")
    try:
        #Checking if cname is a string and not integer
        int(cname)
        print ("Invalid name")
        cname = input ("Enter your name: ")
    except:
        print()
        
    a = True
    while a == True:
        itemID = input ("Enter item ID: ")
        #Validating correct itemID
        if itemID not in ("1","2","3","4","5","6"):
            print ("Invalid Item ID.")
            itemID = input ("Enter item ID: ")
            
        quantity = int (input("Enter quantity: "))
        #Checking for valid quantity
        while quantity <= 0:
            print ("Invalid quantity. Please enter valid values.")
            quantity = int (input("Enter quantity: "))

        for item in BRJfurniture:
            manName = item[1]
            proName = item[2]
            
            if item[0] == itemID:
                #Checking if the desired number of stock is available or not
                while quantity > int(item[3]):
                    print("Sorry we only have " + item[3] + " stock left.")
                    quantity = int (input("Enter quantity: "))
                    
                #Calculating price of number of products entered 
                itemTotal = int(item[4].replace("$", "")) * int(quantity)
                #Storing the values in a 2D list to print receipt
                transactions.append([itemID, manName, proName, quantity, itemTotal])

                #Updating stock in 2D list
                item[3] = str(int(item[3]) - quantity)
                update = open ("BRJ Furniture.txt", "w")
                for row in BRJfurniture:
                    #And writing it in the text file
                    update.write(", ".join(row) + "\n")
                update.close()

        #Asking for multiple orders; breaks the loop if no multiple orders, else it continues the loop     
        ask = input ("Do you want to add more? Y/N: ").lower()
        if ask == "n":
            #Determining shipping cost according to customer's needs 
            ship = input ("Do you want us to ship? Y/N: ").lower()
            if ship == "y":
                place = input ("Inside valley or outside? Inside/Outside: ").lower()
                if place == "inside":
                    ship_P = 1000
                elif place == "outside":
                    ship_P = 1500
                else:
                    print ("Enter valid option")
                    
            if ship == "n":
                ship_P = 0
            #Passing the values to generate receipt
            bill = sell_bill(cname, transactions, ship_P)
            print(bill)
            a = False

#Creating a function to generate receipt for sell in shell
def sell_bill(cname, transactions, ship_P):
    #Storing the current date and time in a variable
    date = datetime.datetime.now()
    print ("------------BRJ FURNITURE------------")
    print ("Customer's name: " + cname)
    print ("Date: " + date.strftime("%Y-%m-%d_%H-%M-%S")) #printing the date in year-month-date_hour-minute-second format
    print ("--" * 20)
    total = 0
    vat_P = 0
    total_P = 0
    
    for t in transactions:
        print ("Item ID: " + t[0])
        print ("Manufacturer name: " + t[1])
        print ("Item name: " + t[2])
        print ("Quantity: " + str(t[3]))
        print ("Total: $" + str(t[4]))
        print ("--" * 20)
        total += t[4]

    #Performing calculations and printing 
    vat_P = total* 13/100
    total_P = total + vat_P + ship_P
    print ("Vat Price: $" + str(vat_P))
    print ("Shipping cost: $" + str(ship_P))
    print ("Final total: $" + str(total_P))
    #Calling funtion to generate receipt from write module
    write.sell_invoice(cname, transactions, ship_P)

def order():
    read.fo()
    orders = []
    
    ename = input ("Enter employee's name: ")
    try:
        #Checking if ename is a string and not integer
        int(ename)
        print ("Invalid name")
        ename = input ("Enter your name: ")
    except:
        print()
        
    a = True
    while a == True:
        itemID = input ("Enter item ID: ")
        #Validating correct itemID
        if itemID not in ("1","2","3","4","5","6"):
            print ("Invalid Item ID.")
            itemID = input ("Enter item ID: ")
            
        quantity = int (input("Enter quantity: "))
        #Checking for valid quantity
        while quantity <= 0:
            print ("Invalid quantity. Please enter valid values.")
            quantity = int (input("Enter quantity: "))
            
        itemTotal = 0
        for item in BRJfurniture:
            manName = item[1]
            proName = item[2]
            
            if item[0] == itemID:
                #Calculating price of number of products entered
                total = int(item[4].replace("$", "")) * int(quantity)
                #Storing the values in a 2D list to print receipt
                orders.append([itemID, manName, proName, quantity, total])

                #Updating stock in 2D list
                item[3] = str(int(item[3]) + quantity)
                update = open ("BRJ Furniture.txt", "w")
                for row in BRJfurniture:
                    #And writing it in the text file
                    update.write(", ".join(row) + "\n")
                update.close()

        #Asking for multiple orders; breaks the loop if no multiple orders, else it continues the loop        
        ask = input ("Do you want to add more? Y/N: ").lower()
        if ask == "n":
            #Passing the values to generate receipt
            bill = order_bill(ename, orders)
            print(bill)
            a = False
            
#Creating a function to generate receipt for orders in shell
def order_bill(ename, orders):
    #Storing the current date and time in a variable
    date = datetime.datetime.now()
    print ("------------BRJ FURNITURE------------")
    print ("Employee's name: " + ename)
    print ("Date: " + date.strftime("%Y-%m-%d_%H-%M-%S"))
    print ("--" * 20)
    total_P = 0
    
    for order in orders:
        print ("Item ID: " + order[0])
        print ("Manufacturer: " + order[1])
        print ("Item Name: " + order[2])
        print ("Quantity: " + str(order[3]))
        print ("Total: $" + str(order[4])) 
        print ("--" * 20)
        total_P += int (order[4])
        
    print ("Final total: $" + str(total_P))
    #Calling funtion to generate receipt from write module
    write.order_invoice(ename, orders)

    
            
    

