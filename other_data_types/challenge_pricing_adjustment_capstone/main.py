grocery_inventory = {"Milk": ("Dairy", 3.50, 8), 
                     "Eggs": ("Dairy", 5.50, 30), 
                     "Bread": ("Bakery", 2.99, 15), 
                     "Apples": ("Produce", 1.50, 50)}
eggs_tuple = grocery_inventory.get("Eggs")
eggs_price = eggs_tuple[1]
if eggs_price > 5:
   print("Eggs are too expensive, reducing the price by $1.")
   new_price = eggs_price - 1
   grocery_inventory["Eggs"] = (eggs_tuple[0], new_price, eggs_tuple[2])
else:
 print("The price of Eggs is reasonable.")
#print(new_price)
grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes:", grocery_inventory)
milk_tuple = grocery_inventory.get("Milk") 
milk_stock = milk_tuple[2]
if milk_stock < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    new_stock = milk_stock + 20
    grocery_inventory["Milk"] = (milk_tuple[0], milk_tuple[1], new_stock)
else:
    print("Milk has sufficient stock.")
print(new_stock)
apple_tuple = grocery_inventory.get("Apples")
apple_price = apple_tuple[1]
if apple_price > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")
else:
    print("The price of Apples is reasonable")
print("Updated inventory:", grocery_inventory)