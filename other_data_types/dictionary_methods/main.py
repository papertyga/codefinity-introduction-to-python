grocery_inventory = {
    "Milk:": (113, "Dairy"),
    "Eggs": (116, "Dairy"),
    "Bread": (117, "Bakery"),
    "Apples": (141, "Produce")
}
bread_details = grocery_inventory["Bread"]
grocery_inventory.update({"Cookies": (143, "Bakery")})
grocery_inventory.pop("Eggs")

# Retrieve the details for "Bread" and save to bread_details

print("Details of Bread:", bread_details)

# Add a new item "Cookies"
print("Inventory after adding Cookies:", grocery_inventory)

# Remove the item "Eggs"
print("Inventory after removing Eggs:", grocery_inventory)
