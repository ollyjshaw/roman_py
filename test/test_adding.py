from roman.roman import roman_reverse
from roman.roman import roman_convert
from roman.roman import roman_add
from hypothesis import given
import hypothesis.strategies as st


def test_one_add_one():
    assert roman_add("I", "I") == "II"


def test_lots():
    x = range(1, 1000, 1)
    for n in x:
        added = n + (n+1)
        next_n = n + 1
        assert roman_add(roman_convert(n), roman_convert(next_n)) == roman_convert(added)


@given(st.integers(1, 1000), st.integers(1, 1000))
def test_add_via_property(x, y):
    assert roman_add(roman_convert(x), roman_convert(y)) == roman_convert(x+y)


@given(st.integers(1, 1000))
def test_convert_via_property(x):
    assert roman_reverse(roman_convert(x)) == x
