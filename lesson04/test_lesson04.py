import pytest

from greet_args import get_name
from github_user import parse_user


def test_parse_user_normal() -> None:
    assert parse_user({"login": "sam", "name": "Sam Lee", "public_repos": 3}) == "sam: Sam Lee, 3 public repos"


def test_parse_user_missing_login_returns_none() -> None:
    assert parse_user({"name": "Sam Lee", "public_repos": 3}) is None


def test_parse_user_missing_key_returns_no_name() -> None:
    assert parse_user({"login": "sam", "name": None, "public_repos": 3}) == "sam: no name, 3 public repos"


def test_parse_user_missing_public_repos_returns_none() -> None:
    assert parse_user({"login": "sam", "name": "Sam Lee"}) is None


def test_parse_user_raises_empty_dict_return_none() -> None:
    assert parse_user({}) is None


def test_get_name_good_name() -> None:
    assert get_name(["greet_args.py", "Awshaf"]) == "Awshaf"


def test_get_name_too_few_args() -> None:
    with pytest.raises(ValueError):
        get_name(["greet_args.py"])


def test_get_name_too_many_args() -> None:
    with pytest.raises(ValueError):
        get_name(["greet_args.py", "Awshaf", "Ahmath"])