from plates import is_valid


def test_is_valid_cs50_is_valid() -> None:
    assert is_valid("CS50")


def test_is_valid_cs05_is_invalid() -> None:
    assert not is_valid("CS05")


def test_is_valid_cs50p_is_invalid() -> None:
    assert not is_valid("CS50P")


def test_is_valid_h_is_invalid() -> None:
    assert not is_valid("H")


def test_is_valid_aaa222_is_valid() -> None:
    assert is_valid("AAA222")


def test_is_valid_aaa22a_is_invalid() -> None:
    assert not is_valid("AAA22A")


def test_is_valid_punctuation_is_invalid() -> None:
    assert not is_valid("CS50.5")
    assert not is_valid("PI3.14")
