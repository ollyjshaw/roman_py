from roman.roman import roman_convert

def test_one():
    answer = roman_convert(1)
    assert answer == "I"
