prices = [29.99, 45.50, 12.75, 38.20]

# Write your code here
discount_factor =[0.9, 0.8, 0.85, 0.95]
for cost in range(len(prices)):
    prices[cost] = prices[cost] * discount_factor[cost]
    print(f"Updated price for item {cost}: ${prices[cost]:.2f}")