#Module: Main
'''
Objective:
    - The run module
    - To ask user their choices and call functions from other modules accordingly
'''
#import all the necessary modules
import read
import operations

#Creating a function to ask 
def main():
    while True:
        print ("---" * 26)
        print ("\t\t\tWelcome to BRJ Furniture")
        print ("---" * 26)
        opt = input ("What would you like to do? \n 1. View Furnitures \n 2. Buy Furniture \n 3. Order from Manufacturer \n 4. Exit \n  --> ")

        if (opt == "1"):
            read.fo()
    
        elif (opt == "2"):
            operations.sell()
            
        elif (opt == "3"):
            operations.order()

        elif (opt == "4"):
            print ("Exiting...")
            break
       
        else:
            print("Please enter valid option")
main()
