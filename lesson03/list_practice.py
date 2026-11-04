def sum_list(numbers: list[int]) -> int:
    """Add all the numbers."""
    total = 0
    for n in numbers:
        total += n
    return total


def evens(numbers: list[int]) -> list[int]:
    """Return a new list with only the even numbers."""
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result


def count_above(numbers: list[int], limit: int) -> int:
    """Count how many numbers are bigger than limit."""
    counter = 0
    for n in numbers:
        if n > limit:
            counter += 1
    return counter


def largest(numbers: list[int]) -> int:
    """Return the biggest number. If the list is empty, raise ValueError."""
    if not numbers:
        raise ValueError("list is empty")
    biggest = numbers[0]
    for n in numbers:
        if n > biggest:
            biggest = n
    return biggest


def main() -> None:
    assert sum_list([1, 2, 3]) == 6
    assert sum_list([]) == 0
    assert evens([1, 3]) == []
    assert evens([2, 4]) == [2, 4]
    assert evens([1, 2, 3, 4]) == [2, 4]
    assert count_above([5, 1, 8, 3], 4) == 2
    assert count_above([], 4) == 0
    assert largest([3, 9, 2]) == 9
    assert largest([-5, -2, -8]) == -2
    try:
        largest([])
    except ValueError:
        pass  # good: the error happened, as we want
    else:
        raise AssertionError("largest([]) should raise ValueError")
    print("All checks passed")


if __name__ == "__main__":
    main()