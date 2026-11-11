def main() -> None:
    """Ask for a fraction and print E, F or the percentage."""
    while True:
        fraction = input("Fraction: ").strip()
        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            percentage = round(x / y * 100)
        except (ValueError, ZeroDivisionError):
            continue
        if x > y or x < 0:
            continue
        if percentage <= 1:
            print("E")
        elif percentage >= 99:
            print("F")
        else:
            print(f"{percentage}%")
        break


if __name__ == "__main__":
    main()