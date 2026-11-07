import pytest

from dict_practice import cart_total
from list_practice import evens, largest
from safe_functions import safe_int


prices = {"apple": 2.5, "pear": 3.0, "milk": 1.5}


def test_safe_int_valid_positive() -> None:
    assert safe_int("42") == 42


def test_safe_int_valid_negative() -> None:
    assert safe_int("-7") == -7


def test_safe_int_valid_zero() -> None:
    assert safe_int("0") == 0


def test_safe_int_text_returns_none() -> None:
    assert safe_int("abc") is None


def test_safe_int_empty_returns_none() -> None:
    assert safe_int("") is None


def test_evens_empty_list() -> None:
    assert evens([1, 3]) == []


def test_evens_list() -> None:
    assert evens([2, 4]) == [2, 4]


def test_largest_positive() -> None:
    assert largest([2, 8, 5]) == 8


def test_largest_negative() -> None:
    assert largest([-1, -8, -4]) == -1


def test_largest_empty_list_raises() -> None:
    with pytest.raises(ValueError):
        largest([])

def test_cart_total_adds_prices() -> None:
    assert cart_total(prices, ["apple", "milk", "apple"]) == 6.5

def test_cart_total_missing_key() -> None:
    assert cart_total(prices, ["kiwi"]) == 0.0