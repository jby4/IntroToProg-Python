#-------------------------------------------------#
# Project: Python programming
# Name: Assignment 05
# Title: Working with Dictionaries
# Purpose: Learn more
# Author: Jean-Baptiste Yamindi
# Created: 08/12/2018
#https://www.tutorialspoint.com/python/python_dictionary.htm
#-------------------------------------------------#

#-- Data information--#
# declare variables and constants
# objFile = An object that represents a file
# strData = A row of text data from the file
# dicRow = A row of data separated into elements of a dictionary {Task,Priority}
# lstTable = A dictionary that acts as a 'table' of rows
# strMenu = A menu of user options
# strChoice = Capture the user option selection

#-- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

#-- Processing: 7 steps --#
# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.

# Step 2
# Display a menu of choices to the user

# Step 3
# Display all todo items to user

# Step 4
# Add a new item to the list/Table

# Step 5
# Remove a new item to the list/Table

# Step 6
# Save tasks to the ToDo.txt file

# Step 7
# Exit program
#-------------------------------

# Step 1 - Load data from a file
# When the program starts, load each "row" of data 
# in "ToDo.txt" into a python Dictionary.
# Add the each dictionary "row" to a python list "table"

NewFile = open("/Users/jean-baptisteyamindi/Desktop/Foundation_Python2018/Module05/Todo.txt", "r")
strData = NewFile.readline()
dicRow = {(strData.split(":")[0]).strip(), (strData.split(":")[1]).strip()} # divide the data into 2 elements
lstTable = [dicRow]
for line in NewFile:
strData=line
dicRow = {(strData.split(":")[0]).strip(), (strData.split(":")[1]).strip()}
lstTable += [dicRow]
print(lstTable)
NewFile.close
 

# Step 2 - Display a menu of choices to the user
while(True):
    print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    
strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print(strChoice) #adding a new line

    # Step 3 -Show the current items in the table
if (strChoice.strip() == '1'):
        continue
    # Step 4 - Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        continue
    # Step 5 - Remove a new item to the list/Table
    elif(strChoice == '3'):
        continue
    # Step 6 - Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        continue
elif (strChoice == '5'):
print(“Oops there 4 options from 1 to 4 “,”\n”) #adding a new line
strExitFile.lower()=str(input(enter ‘q’ to exit the program))
NewFile.close()
    
#3. Ask the user to Add or Remove tasks from the list using numbered of Menu Options:
#1) Show current data
while(True):
print(dictRow)
  if(dictRow.lower())== "done"):
break
#2. Add a new item
dictRow.append(strData)
print(dictRow)
if(dictRow.append(strData))== "done"):
break
#3. Remove an existing item 
dictRow.remove(strData)
print(dictRow)
if(dictRow. remove(strData))== "done"):
break
4) Save Data to File
print("Would you like to save your data to File?")
strUserInput = str(input("Enter 'y' or 'n'"))
if(strUserInput == 'y'):
    objFile = open("C:\\_Todo.txt", "w")
    for row in tplTable:
        objFile.write(str(row[0]) + "," + str(row[1]) + "\n")
    objFile.close()
    print("Data was saved:")
  else:
strValue = str(input("Enter a Value: "))
# 5) Exit Program
print("Would you like to exit this progrom?")
strUserExitInput = str(input("Enter ‘exit’ to quite or ‘no’ to continue"))
if(strUserExitInput.lower() == 'exit'):
break
    print("thanks for being our user and see you next time")
if(strUserExitInput.lower() == 'no'):
continue
print("please enjoy your Menu options")
else:
print(“You should type “exit ” to exit or “no” to continue”)
strUserInput = str(input("Enter 'y' or 'n'"))
if(strUserInput == 'y'):
   




