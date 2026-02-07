def apply_discount(price, discount=0.10):
    discounted_price = price * (1 - discount)
    return discounted_price

default_discount_price = apply_discount(100)
print(f"Price after applying the default discount: ${default_discount_price}.")

