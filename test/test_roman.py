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


def test_eight():
    answer = roman_convert(8)
    assert answer == "VIII"


def test_nine():
    answer = roman_convert(9)
    assert answer == "IX"


def test_ten():
    answer = roman_convert(10)
    assert answer == "X"


def test_nineteen():
    answer = roman_convert(19)
    assert answer == "XIX"


def test_49():
    answer = roman_convert(49)
    assert answer == "XLIX"


def test_50():
    answer = roman_convert(50)
    assert answer == "L"


def test_99():
    answer = roman_convert(99)
    assert answer == "XCIX"


def test_100():
    answer = roman_convert(100)
    assert answer == "C"


def test_499():
    answer = roman_convert(499)
    assert answer == "CDXCIX"

def test_500():
    answer = roman_convert(500)
    assert answer == "D"