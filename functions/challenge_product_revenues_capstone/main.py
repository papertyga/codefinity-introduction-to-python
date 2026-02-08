# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

revenue = []
for price, qty in zip(prices, quantities_sold):
    revenue.append(price * qty)
print(revenue)

revenue_per_product = list(zip(products, revenue))
revenue_per_product.sort()

for product, rev in revenue_per_product:
    print(f"{product} has total revenue of ${rev}")

def calculate_revenue(prices, quantities_sold):
    rev_list = []
    for price, qty in zip(prices, quantities_sold):
        rev_list.append(price * qty)
    return rev_list

def print_revenue(revenue_list):
    rev_list = []
    for product, rev in sorted(revenue_list):
        print(f"{product} has total revenue of ${rev}")
        print_revenue(rev_list)

