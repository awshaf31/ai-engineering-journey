MONTHS = [ 
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def month_number(name: str) -> int | None:
    """Return the month number (1 to 12), or None if the name is not a month."""
    try:
        return MONTHS.index(name) + 1
    except ValueError:
        return None


def main() -> None:
    """Ask for a date and print it as YYYY-MM-DD."""
    while True:
        text = input("Date: ").strip()
        try:
            if "/" in text:
                month_text, day_text, year_text = text.split("/")
                month = int(month_text)
                day = int(day_text)
            else:
                month_name, day_text, year_text = text.split(" ")
                if not day_text.endswith(","):
                    continue
                month = month_number(month_name)
                day = int(day_text.removesuffix(","))
            year = int(year_text)
        except ValueError:
            continue

        if month is None or not 1 <= month <= 12 or not 1 <= day <= 31:
            continue
        print(f"{year}-{month:02}-{day:02}")
        break


if __name__ == "__main__":
    main()