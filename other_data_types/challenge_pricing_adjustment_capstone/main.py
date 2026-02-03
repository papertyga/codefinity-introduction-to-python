#1
grocery_inventory = {"Milk":("Dairy", 3.50, 8),
                     "Eggs":("Dairy", 5.50, 30),
                    "Bread":("Bakery", 2.99, 15)
}
#2
if grocery_inventory["Eggs"][1] > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory["Eggs"] = ("Dairy", 4.50, 30)
#3
grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print(f"Inventory after adding Tomatoes: {grocery_inventory}")

#4
if grocery_inventory["Milk"][2] < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory["Milk"] = ("Dairy", 3.50, 28)

print("Updated inventory:", grocery_inventory)