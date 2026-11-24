from twttr import shorten


def test_shorten_lowercase():
    assert shorten("twitter") == "twttr"

def test_shorten_uppercase():
    assert shorten("TWITTER") == "TWTTR"


def test_shorten_only_vowels():
    assert shorten("euouae") == ""

def test_shorten_numbers_and_space():
    assert shorten("Number 07") == "Nmbr 07"

def test_shorten_no_vowels():
    assert shorten("myth") == "myth"



