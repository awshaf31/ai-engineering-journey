import pytest

from average_scores import parse_score, average


def test_parse_score_int() -> None:
    assert parse_score("80") == 80.0


def test_parse_score_str() -> None:
    assert parse_score("abc") is None


def test_parse_score_above_100_returns_none() -> None:
    assert parse_score("150") is None


def test_parse_score_negative() -> None:
    assert parse_score("-1") is None


def test_parse_score_100() -> None:
    assert parse_score("100") == 100.0


def test_parse_score_zero() -> None:
    assert parse_score("0") == 0.0


def test_parse_score_float() -> None:
    assert parse_score("3.5") == 3.5


def test_average_list() -> None:
    assert average([80.0, 90.0, 70.0]) == 80.0


def test_average_list_raises() -> None:
    with pytest.raises(ValueError):
        average([])