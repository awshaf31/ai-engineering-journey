def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Length check.
    if not (2 <= len(s) <= 6):
        return False

    # Starting Letter check.
    if not s[0:2].isalpha():
        return False

    # Check punctuation marks.
    if not s.isalnum():
        return False
    # Number placement & leading zero checks.
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == '0':
                return False
            for j in range(i, len(s)):
                if not s[j].isdigit():
                    return False
            break

    return True

if __name__ == "__main__":
    main()
