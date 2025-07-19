#Module: Write
'''
Objectives:
    - To generate a unique receipt for each order in a text file
'''

#Importing datetime
import datetime

#Creating a function to generate receipt for sell in text file
def sell_invoice(cname, transactions, ship_P):
    date = datetime.datetime.now()
    #generating a unique name for each receipt using customer name and datetime (for uniqueness)
    bill_name = "sell_" + str(cname) + date.strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
    filewrite = open (bill_name, "w")
    
    #Writing the receipt in the text file
    filewrite.write ("------------BRJ FURNITURE------------\n")
    filewrite.write ("Customer's name: " + cname + "\n")
    filewrite.write ("Date: " + date.strftime("%Y-%m-%d_%H-%M-%S") + "\n")
    filewrite.write ("--" * 20 + "\n")
    total = 0
    vat_P = 0
    total_P = 0
    
    for t in transactions:
        filewrite.write ("Item ID: " + t[0] + "\n")
        filewrite.write ("Manufacturer name: " + t[1] + "\n")
        filewrite.write ("Item name: " + t[2] + "\n")
        filewrite.write ("Quantity: " + str(t[3]) + "\n")
        filewrite.write ("Total: $" + str(t[4]) + "\n")
        filewrite.write ("--" * 20 + "\n")
        total += t[4]

    #Performing calculations and printing     
    vat_P = total* 13/100
    total_P = total + vat_P + ship_P
    filewrite.write ("Vat Price: $" + str(vat_P) + "\n")
    filewrite.write ("Shipping cost: $" + str(ship_P) + "\n")
    filewrite.write ("Final total: $" + str(total_P) + "\n")

#Creating a function to generate receipt for orders in text file
def order_invoice(ename, orders):
    date = datetime.datetime.now()
    #generating a unique name for each receipt using employee name and datetime (for uniqueness)
    bill_name = "order_" + str(ename) + date.strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
    filewrite = open (bill_name, "w")

    filewrite.write ("------------BRJ FURNITURE------------\n")
    filewrite.write ("Employee's name: " + ename + "\n")
    filewrite.write ("Date: " + date.strftime("%Y-%m-%d_%H-%M-%S") + "\n")
    filewrite.write ("--" * 20 + "\n")
    total_P = 0

    #Printing the receipt with calculated values
    for order in orders:
        filewrite.write ("Item ID: " + order[0] + "\n")
        filewrite.write ("Manufacturer: " + order[1] + "\n")
        filewrite.write ("Item Name: " + order[2] + "\n")
        filewrite.write ("Quantity: " + str(order[3]) + "\n")
        filewrite.write ("Total: $" + str(order[4]) + "\n") 
        filewrite.write ("--" * 20 + "\n")
        total_P += int (order[4])
        
    filewrite.write ("Final total: $" + str(total_P) + "\n")

