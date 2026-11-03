def safe_int(text: str) -> int | None:
    """Return text as an int. If it is not a whole number, return None."""
    try:
        return int(text)
    except ValueError:
        return None

    
def safe_divide(a: float, b: float) -> float | None:
    """Return `a / b`. If `b` is zero, return `None`."""
    try:
        return a / b
    except ZeroDivisionError:
        return None


def first_item(items: list[str]) -> str | None:
    """Return the first item. If the list is empty, return `None`."""
    try:
        return items[0]
    except IndexError:
        return None


def main() -> None:
    assert safe_int("42") == 42
    assert safe_int("-7") == -7
    assert safe_int("abc") is None
    assert safe_int("3.5") is None
    assert safe_int("") is None
    assert safe_divide(10, 4) == 2.5
    assert safe_divide(10, 0) is None
    assert first_item(["a", "b"]) == "a"
    assert first_item([]) is None
    print("All checks passed")


if __name__ == "__main__":
    main()