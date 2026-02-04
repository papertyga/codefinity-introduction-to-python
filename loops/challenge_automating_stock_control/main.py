# Grocery store inventory:
# "Item": [current stock, target stock level, restock amount]
inventory = {
    "Bread": [30, 50, 10],
    "Eggs": [120, 200, 40],
    "Milk": [60, 100, 20],
    "Apples": [15, 50, 15]
}

print("Restocking started")

# Write your code here
for item in inventory:
    print("Restocking", item)
    while inventory[item][0] < inventory[item][1]:
        inventory[item][0] >= inventory[item][1]
        inventory[item][0] = inventory[item][0] + inventory[item][2]

    


print("Restocking completed")