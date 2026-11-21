import sys


def get_name(argv: list[str]) -> str:
    """Return the name from the command line."""
    if len(argv) < 2:
        raise ValueError("Too few arguments")
    if len(argv) > 2:
        raise ValueError("Too many arguments")
    return argv[1]


def main() -> None:
    """Reads the name, handles errors, and prints the greeting."""
    try:
        name = get_name(sys.argv)
    except ValueError as error:
        sys.exit(str(error))
    print("Hello,", name)


if __name__ == "__main__":
    main()