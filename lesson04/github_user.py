import requests
import sys

from greet_args import get_name


def parse_user(data: dict) -> str | None:
    """Return login name, number of public repos. handle missing data."""
    name = data.get("name") or "no name"
    try:
        return f'{data["login"]}: {name}, {data["public_repos"]} public repos'
    except KeyError:
        return None


def fetch_user(username: str) -> dict | None:
    """Get one username from the API.Return None if anything goes wrong."""
    try:
        response = requests.get(f"https://api.github.com/users/{username}", timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return None


def main() -> None:
    try:
        username = get_name(sys.argv)
    except ValueError as error:
        sys.exit(str(error))
    data = fetch_user(username)
    if data is None:
        print("Could not get that user")
        return
    line = parse_user(data)
    if line is None:
        print("Unexpected answer")
        return
    print(line)


if __name__ == "__main__":
    main()