#Module: Read
'''
Objective:
    - To open a text file and display it
    - To store the data of file in 2d list
'''

#Creating a function to open the text file and display its content
def fo():
    try:
        fileopen = open("BRJ Furniture.txt", "r")
        print ("Item ID, Name of Manufacturer, Product Name, Quantity, Price")
        print(fileopen.read())
        fileopen.close()
    #Throwing an exception for when it cannot find the file
    except:
        print ("File not Found!")

#Creating a function to store the data in a 2d list
def listt():
    fileopen = open("BRJ Furniture.txt", "r")
    two_d = []
    for data in fileopen:
        '''Removing "\n" and " " (space) to make it easy to compare values'''
        x = data.replace("\n", "")
        two_d.append(x.split(","))
    return two_d


