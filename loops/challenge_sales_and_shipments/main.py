# Products and their current stock
products = [["Apples", 10], ["Bananas", 8]]

# Units sold today (same order as products)
units_sold = [3, 5]

for product in range(len(products)):
    products[product][1] = products[product][1] - units_sold[product]
    print("Final stock levels:", products)
