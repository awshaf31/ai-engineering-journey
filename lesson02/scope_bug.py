def add_tax(price: float) -> float:
    tax = price * 0.1
    return price + tax

result = add_tax(100.0)
print(result)

