def to_number(text: str) -> int:
    try:
        return int(text)
    except ValueError:
        print("not a number")
        return -1

a = to_number("42")
b = to_number("abc")
print(a)
print(b)
print(10/0)
print("done")