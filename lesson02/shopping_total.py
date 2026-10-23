def total_cost(price: float, quantity: int) -> float:
    """Return the total cost of buying quantity items at price each."""
    return price * quantity



def main() -> None:
        """Ask for 3 items and print the grand total."""
        grand_total = 0.0
        for _ in range(3):
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))
            grand_total = grand_total + total_cost(price, quantity)
    
        print("Grand total:", grand_total)


if __name__ == "__main__":
    main()
