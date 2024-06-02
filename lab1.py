"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                                LAB 1
-----------------------------------------------------------------------------------------------
- File Name: lab1.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create a class named Item that represents a generic item in an inventory system.
               Implement encapsulation using private attributes and public getters and setters.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Step 1: Define the Item class with initialisation that uses setters for name, price, and quantity.
# Instead of directly setting private attributes in the __init__ method, use the class's own setters
# We will define the setters in later steps to add validation to the setting of these attributes.
# Step 2: Implement a getter for the name attribute.
# This method should simply return the value of the private _name attribute.
# Step 3: Implement a setter for the name attribute.
# This method should check if the provided value is a string before setting the _name attribute.
# If the value is not a string, it should raise a ValueError.
# Step 4: Implement a getter for the price attribute.
# This method should return the price formatted as a string with two decimal places.
# Step 5: Implement a setter for the price attribute.
# This method should check if the provided value is a non-negative number before setting the _price attribute.
# If the value is negative, it should raise a ValueError.
# Step 6: Implement a getter for the quantity attribute.
# This method should simply return the value of the private _quantity attribute.
# Step 7: Implement a setter for the quantity attribute.
# This method should check if the provided value is a non-negative integer before setting the _quantity attribute.
# If the value is negative, it should raise a ValueError.
# Step 8: Create instances of the Item class and demonstrate the use of getters and setters.
# For example, create a new Item and attempt to set its attributes with both valid and invalid values.
# Print the outputs using the getters to show how the data is managed internally.

class Item:
    def __init__ (self , name , price , quantity):
        self._name = name
        self._price = price
        self._quantity = quantity

    def getName(self):
        return self._name
    
    def getPrice(self):
        return self._price
    
    def getQuantity(self):
        return self._quantity

    def setName(self , nameUpdate):
        if nameUpdate == "":
            raise ValueError("name must not be empty")
        self._name = nameUpdate

    def setPrice(self , priceUpdate):
        if priceUpdate <= 0:
            raise ValueError("price must be a positive number")
        self._price = priceUpdate

    def setQuantity(self , quantityUpdate):
        if quantityUpdate < 0:
            raise ValueError("price must be a positive number or zero")
        self._name = quantityUpdate


item234823948 = Item("item234823948" , "234" , "7")

item234823948.setName("thingymabob")

print(item234823948.getName())
print(item234823948.getPrice())
print(item234823948.getQuantity())

