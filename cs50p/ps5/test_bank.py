from bank import value


def test_value_greeting_capital():
    assert value("Hello") == 0
    assert value("HELLO") == 0


def test_value_hey():
    assert value("Hey") == 20


def test_value_what_s_up():
    assert value("What's up?") == 100


def test_value_hello_with_space():
    assert value(" hello") == 0


def test_value_capital_h():
    assert value("How you doing?") == 20



