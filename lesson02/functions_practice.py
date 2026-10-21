
def total_cost(price: float, quantity: int) -> float:
    """Return the total cost of buying quantity items at price each."""
    return price * quantity

def discount_price(price: float, percent: float) -> float:
    """Return the price after taking percent off."""
    price_after_discount = 100 - percent
    return price * price_after_discount / 100

def is_even(n: int) -> bool:
    """Return True if the number is even,otherwise False."""
    return n % 2 == 0


def main() -> None:
    assert total_cost(2.5, 4) == 10.0
    assert total_cost(10.0, 0) == 0.0
    assert discount_price(200.0, 25) == 150.0
    assert discount_price(80.0, 50) == 40.0
    assert is_even(4) is True
    assert is_even(7) is False
    print("All checks passed")


if __name__ == "__main__":
    main()