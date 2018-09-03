Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
#-------------------------------------------------------------------------------
# Name: Assignment 07
# Purpose: Learn more about exception handling and Python’s pickling module, and how you use them
# Author: Jean-Baptiste
# Created: 08/25/2018
#-------------------------------------------------------------------------------

# 1. Now we are going to create a try block using Python Exception Handling.
print("++++ Welcome to the first part using Python Exception Handling ++++")
""" 1) Create a simple example of how you would use Python Exception Handling. Make sure to commet your code.
    2)Create a simple example of how you would use Python Pickling. Make sure to comment your code
"""

# Display the current data
# The file must be created first before this will work,
# (and a+ does not work here!)

objFile = None

try:
    objFile = open("/Users/jean-baptisteyamindi/Library/Preferences/PyCharmCE2018.2/scratches/Customers.txt"
"r+")  # See page 193
    print("Here is the current data:")
    print(objFile.read())

    print("Type in a Customer Id and Name you want to add to the file")
    print("(Enter 'Done' to quit!)")

    while (True):

        strUserInput = input("Enter the Id and Name (ex. 1,Bob Smith): ")
        if (strUserInput.lower() == "done"):
            break
        else:
            objFile.write(strUserInput + "\n")

    print("Excellent,this data was saved:")
    objFile.seek(0)
    print(objFile.read())
except Exception as err:
    print("Python is not happy and reported the following error: " + str(err))
finally:
    if (objFile != None):
        objFile.close()
    print("Oops, the program has stopped running ")
 #2. Now let us list data that can be saved to a file with the writelines method and read back again with the readlines method.
# Make a list
# To save it to a txt file
# it must be converted to a string
#!/usr/bin/python
Id = str(1)
Name = "John Bigman"
lstRow1 = [Id, Name]
print(lstRow1)

# output to file
objFile = open("/Users/jean-baptisteyamindi/Library/Preferences/PyCharmCE2018.2/scratches/Customers.txt", "a")
objFile.write(lstRow1[0] + "," + lstRow1[1] + "\n")
objFile.close()

objFile = open("/Users/jean-baptisteyamindi/Library/Preferences/PyCharmCE2018.2/scratches/Customers.txt", "r")

for row in objFile:
 lstFileData = row.strip().split(",")
 print(lstFileData)

objFile.close()

#3.saving Data from an object
#-- Data --
strData = None # Holds returned data
objFile = None # Handle for a text file

#--- create data classes ---
class Customer(object):
    Id = None
    Name = None

    def ToString(self):
        return str(self.Id) + "," + str(self.Name)
#End of class

# --- Use the class  ----
# Create an object
objCustomer1 = Customer()

# Write data to the object's fields
objCustomer1.Id = input("Enter an Id: ")
objCustomer1.Name = input("Enter a Name: ")

# Read data from the object's fields
strData = objCustomer1.ToString()

# Use the data
# output to file
objFile = open("/Users/jean-baptisteyamindi/Library/Preferences/PyCharmCE2018.2/scratches/Customers.txt", "a")
objFile.write(strData + "\n")
objFile.close()

# read from the file
objFile = open("/Users/jean-baptisteyamindi/Library/Preferences/PyCharmCE2018.2/scratches/Customers. txt", "r")
print(objFile.read())
objFile.close()

#4.Create a simple example a technique called Python Pickling.
print("++++ Welcome to the second part using Python Pickling ++++")

import pickle

intId = int(input("Enter an Id: "))
strName = str(input("Enter a Name: "))
lstCustomer = [intId, strName]
print(lstCustomer)

# Now we will store the data with the pickle.dump method

objFile = open("/Users/jean-baptisteyamindi/Library/Preferences/PyCharmCE2018.2/scratches/Customers.dat", "ab")
pickle.dump(lstCustomer, objFile)
objFile.close()

# Let us read the data back with the same pickle.load method
objFile = open(("/Users/jean-baptisteyamindi/Library/Preferences/PyCharmCE2018.2/scratches/Customers.dat", "rb")
objFileData = pickle.load(objFile) #Note that load() only load one row of data.
objFile.close()

#5.	Ask the user, when the program exits, if they would like
# to save/add the data to a text file called, objFileData.dat.
print("Would you like to save your new entries?")
strUserInput = str(input("Enter 'y' or 'n'"))
if(strUserInput == 'y'):
     objFile = open("Users/jean-baptisteyamindi/Desktop/Foundation_Python
     2018/Module07/Customers.dat ", " w")
    for row in tplTable:
        objFile.write(str(row[0]) + "," + str(row[1]) + "\n")
    objFile.close()
    print("Data was saved:")
else:
    print("Changes were)
Type "copyright", "credits" or "license()" for more information.
