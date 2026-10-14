

def greet(name:str) -> str:
    """Return a welcome message for the given name."""
    return f"Hello, {name}! Welcome to AI engineering."

def main() -> None :
    name = input ("What is your name?")
    message = greet(name)
    print(message)

if __name__ == "__main__":
    main()