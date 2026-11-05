def get_price(prices: dict[str, float], item: str) -> float | None:
    """Return the price. If the item is not in the dictionary, return None."""
    if item not in prices:
        return None
    return prices[item]


def cart_total(prices: dict[str, float], cart: list[str]) -> float:
    """Add the price of every item in the cart. Skip items that have no price."""
    total = 0.0
    for item in cart:
        if item in prices:
            total = total + prices[item]
    return total


def cheapest(prices: dict[str, float]) -> str:
    """Return the name of the cheapest item. If the dictionary is empty, raise ValueError."""
    if not prices:
        raise ValueError("dictionary is empty")
    best_price = float("inf")
    best_name = ""
    for name, price in prices.items():
        if price < best_price:
            best_price = price
            best_name = name
    return best_name


def main() -> None:
    prices = {"apple": 2.5, "pear": 3.0, "milk": 1.5}
    assert get_price(prices, "apple") == 2.5
    assert get_price(prices, "kiwi") is None
    assert get_price(prices, "milk") == 1.5
    assert cart_total(prices, ["apple", "milk", "apple"]) == 6.5
    assert cart_total(prices, ["kiwi"]) == 0.0
    assert cart_total(prices, []) == 0.0
    assert cheapest(prices) == "milk"
    assert cheapest({"milk": 1.5, "apple": 2.5}) == "milk"
    try:
        cheapest({})
    except ValueError:
        pass
    else:
        raise AssertionError("cheapest({}) should raise ValueError")
    print("All checks passed")


if __name__ == "__main__":
    main()