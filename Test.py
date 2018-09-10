if __name__ == "__main__":
    import DataProcessor, Customers
else:
    raise Exception("This file was not created to be imported")
objC = Customers.Customer()
objC.Id = 1
objC.FirstName = "John"
objC.LastName = "Smith"
print(objC.ToString())
Customers.CustomerList.AddCustomer(objC)
print(Customers.CustomerList.ToString())