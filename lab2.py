"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                                LAB 2
-----------------------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Extend the functionality developed in Lab 1 by creating an InventoryManager class 
               that acts as a facade for managing an inventory of items. Demonstrate the use of 
               encapsulation and the facade design pattern through practical examples.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Step 1: Import the Item class from lab1.py
from lab1 import Item

# Step 2: Define the InventoryManager class as a facade to handle the inventory operations.
# It should include methods to add, remove, update, and display items in the inventory.

class InvetoryManager:
    def __init__(self):
        self.items = []

    def add_item(self , item):
        for list_item in self.items:
            if item == list_item:
                self.items.append(item)

    def remove_item(self , item):
        for list_item in self.items:
            if item == list_item:
                self.items.remove(item)

    def update_item_(self , item , name):
        item.setName(name)  

    def update_item_price(self , item , price):
        item.setPrice(price)

    def update_item_quantity(self , item , quantity):
        item.setQuantity(quantity)

    def display_item(self , item):
        print(item.getName())
        print(item.getPrice())
        print(item.getQuantity())  
         
    def display_all(self):
        for item in self.items:
            print(item.getName())
            print(f"{item.getPrice()}$")
            print(f"{item.getQuantity()} left in stock")
            print("-------------------------------------------------")     




# Step 2: Create instances of the Item class and InventoryManager, then demonstrate their usage.
# E.g. add items to the inventory, remove items, update items, and display the inventory.

manager = InvetoryManager()

milk = Item("milk" , "234" , "7")

eggs = Item("eggs" , "4" , "7234")

manager.add_item(eggs)

manager.add_item(milk)

manager.display_all()

manager.remove_item(eggs)
manager.display_item(milk)
for i in range(12312):
    print("🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿🗿")