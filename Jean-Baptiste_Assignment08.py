Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> #---------------------------------------------------------------------------
# Name: Assignment 08
# Purpose: Learn more about learn about creating and using classes, and how you use them
# Author: Jean-Baptiste
# Created: 09/01/2018
#-------------------------------------------------------------------------------
"""1) Create and test a new Python file using the following code
   2)Create one or more classes to store and process Product data using the code previous code First, I copy and paste and modify the code"""
#This the first part about Creating and testing a new Python file using the following code
# open the file
#Data
objFile = None #File Handle
strUserInput = None #A string which holds user input

#Processing
def WriteProductUserInput(File):
  try:
    print("Type in a Product Id, Name, and Price you want to add to the file")
    print("(Enter 'Exit' to quit!)")
    while(True):
      strUserInput = input("Enter the Id, Name, and Price (ex. 1,ProductA,9.99): ")
      if(strUserInput.lower() == "exit"): break
      else: File.write(strUserInput + "\n")
  except Exception as e:
    print("Error: " + str(e))

def ReadAllFileData(File, Message="Contents of File"):
  try:
    print(Message)
    File.seek(0)
    print(File.read())
  except Exception as e:
    print("Error: " + str(e))

#Input/Output

def main():
    try:
        objFile = open("Products.txt", "r+")
        ReadAllFileData(objFile, "Here is the current data:")
        WriteProductUserInput(objFile)
        ReadAllFileData(objFile, "Here is this data was saved:")
    except FileNotFoundError as e:
        print("Error: " + str(e) + "\n Please check the file name")
    except Exception as e:
        print("Error: " + str(e))
    finally:
        if (objFile != None): objFile.close()
    if __name__ == "__main__":
        main()
""" This is the second part creating  one or more classes to store and process Product data using the code previous code """
# a) I used Fields, Constructors, Attributes, Properties, and Method for this class to store and process Product data
        # --- Make the class ---
# Constructor
def __initProduct__(self, ProductId = " ", ProductName = " ", ProductPrice = " "):


# Attributes
    self.__ProductIdProductId = ProductId
    self.__ProductName = ProductName
    self.__ProductPrice = ProductPrice


# --Properties--
# ProductId
@property  # (getter or accessor)
def ProductId(self):
    return self.__ProductId


@ProductId.setter  # (setter or mutator)
def ProductId(self, Value):
    if (Value != None):
        print("Type in a Product Id you want to add to the file")
    elif(Value <= 0):
        print("Type in a positive number of Product Id you want to add to the file")
    else:
        self.__ProductId = Value
    objFile.close()


# --Properties--
# ProductName
@property  # (getter or accessor)
def ProductName(self):
    return self.__ProductName


@ProductName.setter  # (setter or mutator)
def ProductName(self, Value):
 if (Value != None):
        print("Type in a Product Name you want to add to the file")
 else:
    self.__ProductName = Value
 objFile.close()


# --Properties--
# ProductPrice
@property  # (getter or accessor)
def ProductPrice(self):
    return self.__ProductPrice


@ProductPrice.setter  # (setter or mutator)
def ProductPrice(self, Value):
    if (Value != None):
        self.__ProductPrice = Value
        print("Type in a Product Price you want to add to the file")
    else:
        print("(Enter 'Exit' to quit!)")
    objFile.close()

# --- Make the class ---
class Product(object):
        # Fields
    ProductId = ""
    ProductName = ""
    ProductPrice = ""

    def ToString(self):
        return self.ProductId + "," + self.ProductName + "," + self.ProductPrice
    # End of class


# --- Use the class ----
# by making an object!
objP1 =Product()
objP1.ProductId = "123"
objP1.ProductName = "Ice Cream"
objP1.ProductPrice = "$4"


objP2 =Product()
objP2.ProductId = "124"
objP2.ProductName = "Chocolate"
objP2.ProductPrice = "$6"


objP3 = Product()
objP3.ProductId = "125"
objP3.ProductName = "Pizza"
objP3.ProductPrice = "$6.55"

print("ProductId,ProductName,ProductPrice ")
print(objP1.ToString())
print("----------------------------------")
print(objP2.ToString())
print("----------------------------------")
print(objP3.ToString())
print("----------------------------------")
print("Would you like to add more product?")
print("(Enter 'Exit' to quit!)")
print("(Enter 'S' to save!)")
objFile.close()
#--End of class--

# b) In this second example I used the method called private to the object or class for internal processing and security reason only
# to store and process Product data.
        # --- Make the class ---
# Constructor
def __initProduct__(self, ProductId = " ", ProductName = " ", ProductPrice = " "):


# Attributes
    self.__ProductIdProductId = ProductId
    self.__ProductName = ProductName
    self.__ProductPrice = ProductPrice


# --Properties--
# ProductId
@property  # (getter or accessor)
def ProductId(self):
    return self.__ProductId


@ProductId.setter  # (setter or mutator)
def ProductId(self, Value):
    if (Value != None):
        print("Type in a Product Id you want to add to the file")
    elif(Value <= 0):
        print("Type in a positive number of Product Id you want to add to the file")
    else:
        self.__ProductId = Value
    objFile.close()


# --Properties--
# ProductName
@property  # (getter or accessor)
def ProductName(self):
    return self.__ProductName


@ProductName.setter  # (setter or mutator)
def ProductName(self, Value):
 if (Value != None):
        print("Type in a Product Name you want to add to the file")
 else:
    self.__ProductName = Value
 objFile.close()


# --Properties--
# ProductPrice
@property  # (getter or accessor)
def ProductPrice(self):
    return self.__ProductPrice


@ProductPrice.setter  # (setter or mutator)
def ProductPrice(self, Value):
    if (Value != None):
        self.__ProductPrice = Value
        print("Type in a Product Price you want to add to the file")
    else:
        print("(Enter 'Exit' to quit!)")
    objFile.close()

# --- Make the class ---
class Product(object):
        # Fields
    ProductId = ""
    ProductName = ""
    ProductPrice = ""

    def ToString(self):
        return self.ProductId + "," + self.ProductName + "," + self.ProductPrice
    # End of class


# --- Use the class ----
# by making an object!
objP1 =Product()
objP1.ProductId = "123"
objP1.ProductName = "Ice Cream"
objP1.ProductPrice = "$4"


objP2 =Product()
objP2.ProductId = "124"
objP2.ProductName = "Chocolate"
objP2.ProductPrice = "$6"


objP3 = Product()
objP3.ProductId = "125"
objP3.ProductName = "Pizza"
objP3.ProductPrice = "$6.55"

print("ProductId,ProductName,ProductPrice ")
print(objP1.ToString())
print("----------------------------------")
print(objP2.ToString())
print("----------------------------------")
print(objP3.ToString())
print("----------------------------------")
print("Would you like to add more product?")
print("(Enter 'Exit' to quit!)")
print("(Enter 'S' to save!)")
objFile.close()
#--End of class--


# c) In this last method This second example of Method is called Inheritance method One that has the ability to inherit code from a parent class.
# This method has the ability to inherit code from a parent class.This is known as extending the parent class through the mechanism of inheritance
# for this class to store and process Product data.

class Product(Item):
    """ Class for Product data """

    # --Fields--
    # --Constructor--
    def __init__(self, Id=""):
        # Attributes
        self.__Id = Id

    def __init__(self, Name=""):
        # Attributes
        self.__Name = Name

    def __init__(self, Price=""):
        # Attributes
        self.__Price = Price

    # --Properties--
    # Id
    @property  # getter(accessor)
    def Id(self):
        return self.__Id

    @Id.setter  # (mutator)
    def Id(self, Value):
        self.__Id = Value

    # Name
    @property  # getter(accessor)
    def Name(self):
        return self.__Name

    @Name.setter  # (mutator)
    def Name(self, Value):
        self.__Name = Value

    # Price
    @property  # getter(accessor)
    def Price(self):
        return self.__Price

    @Price.setter  # (mutator)
    def Price(self, Value):
        self.__Price = Value

    # --Methods--
    def ToString(self):  # This overrides the original method (it's polymorphic)
        """Explictly returns field data"""
        strData = super().ToString()
        return str(self.Id) + ',' + strData + str(self.Name) + ',' + strData + str(self.Price) + ',' + strData

    def __str__(self):  # This overrides the original method as well
        """Implictly returns field data"""
        strData = super().__str__()
        return str(self.Id) + ',' + strData + str(self.Name) + ',' + strData + str(self.Price) + ',' + strData
    # --End of Class --


# --- Use the class ----
# by making an object!
print("ProductId,ProductName,ProductPrice ")
print("----------------------------------")

objP1 = Product()
objP1.Id = "126"
objP1.Name = "Milk"
objP1.Price = "$1.99"
print(objP2.ToString())
print(objP1)
print("----------------------------------")

objP2 = Product()
objP2.Id = "127"
objP2.Name = "Green Tea"
objP2.Price = "$0.99"
print(objP2.ToString())
print(objP2)
print("----------------------------------")

objP3 = Product()
objP3.Id = "128"
objP3.Name = "Banana"
objP3.Price = "$0.69"
print(objP3.ToString())
print(objP3)
print("----------------------------------")

print("Would you like to add more product?")
print("(Enter 'Exit' to quit!)")
print("(Enter 'S' to save!)")
objFile.close()
# --End of class--
