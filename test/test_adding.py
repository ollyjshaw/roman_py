from roman.roman import roman_reverse
from roman.roman import roman_convert
from roman.roman import roman_add


def test_one_add_one():
    assert roman_add("I", "I") == "II"


def test_lots():
    x = range(1, 1000, 1)
    for n in x:
        added = n + (n+1)
        next_n = n + 1
        assert roman_add(roman_convert(n), roman_convert(next_n)) == roman_convert(added)