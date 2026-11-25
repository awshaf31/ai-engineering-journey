def main() -> None:
    greeting = input("Greeting: ")
    cash = value(greeting)
    print(f"${cash}")


def value(greeting: str) -> int:
    greeting = greeting.strip().lower()
    if greeting.startswith("hello"):
        return 0
    if greeting.startswith("h"):
        return 20
    return 100


if __name__ == "__main__":
    main()
