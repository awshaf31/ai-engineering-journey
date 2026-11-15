def main() -> None:
    """Count grocery items and print them in alphabetical order."""
    grocery_items = {}

    while True:
        try:
            item = input().strip().upper()
        except EOFError:
            break

        if not item:
            continue

        grocery_items[item] = grocery_items.get(item, 0) + 1

    print()
    for name in sorted(grocery_items):
        print(grocery_items[name], name)


if __name__ == "__main__":
    main()