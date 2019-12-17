from roman.roman import roman_reverse


def test_one():
    answer = roman_reverse('I')
    assert answer == 1


def test_three():
    answer = roman_reverse('III')
    assert answer == 3


def test_four():
    answer = roman_reverse('IV')
    assert answer == 4
