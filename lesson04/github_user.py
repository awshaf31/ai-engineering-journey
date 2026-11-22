

def parse_user(data: dict) -> str | None:
    """Return login name, number of public repos. handle missing data."""
    name = data.get("name") or "no name"
    try:
        return f'{data["login"]}: {name}, {data["public_repos"]} public repos'
    except KeyError:
        return None
