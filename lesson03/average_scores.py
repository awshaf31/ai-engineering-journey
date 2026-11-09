def average(scores: list[float]) -> float:
    """Return the average. If the list is empty, raise ValueError."""
    if not scores:
        raise ValueError("list is empty")
    total = 0.0
    for n in scores:
        total += n
    result = total / len(scores)
    return result


def parse_score(text: str) -> float | None:
    """Return the score as a float if the text is a number from 0 to 100."""
    try:
        score = float(text)
        if 0 <= score <= 100:
            return score
        return None
    except ValueError:
        return None


def main() -> None:
    """Ask for 3 valid scores and print the average."""
    scores = []
    while len(scores) < 3:
        text = input("Score: ")
        score = parse_score(text)
        if score is None:
            print("Please enter a number from 0 to 100")
        else:
            scores.append(score)
    result = average(scores)
    print("Average:", f"{result:.1f}")


if __name__ == "__main__":
    main()
