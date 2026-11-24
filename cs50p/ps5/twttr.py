def main() -> None:
    word = input("Input: ")
    shortened = shorten(word)
    print(f"Output: {shortened}")


def shorten(word: str) -> str:
    """Return word with all vowels (upper and lower case) removed."""
    vowels = ['A','E','I','O','U','a','e','i','o','u']
    no_vowels = ""
    for letter in word:
        if letter in vowels:
            continue
        else:
            no_vowels += letter
    return no_vowels


if __name__ == "__main__":
    main()