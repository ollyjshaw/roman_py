from roman.roman import roman_convert


def test_one():
    answer = roman_convert(1)
    assert answer == "I"


def test_three():
    answer = roman_convert(3)
    assert answer == "III"


def test_four():
    answer = roman_convert(4)
    assert answer == "IV"


def test_five():
    answer = roman_convert(5)
    assert answer == "V"