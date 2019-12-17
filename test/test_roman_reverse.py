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


def test_five():
    answer = roman_reverse('V')
    assert answer == 5


def test_9():
    answer = roman_reverse('IX')
    assert answer == 9


def test_10():
    answer = roman_reverse('X')
    assert answer == 10


def test_19():
    answer = roman_reverse('XIX')
    assert answer == 19


def test_49():
    answer = roman_reverse("XLIX")
    assert answer == 49


def test_50():
    answer = roman_reverse("L")
    assert answer == 50

def test_99():
    answer = roman_reverse("XCIX")
    assert answer == 99


def test_100():
    answer = roman_reverse("C")
    assert answer == 100


def test_499():
    answer = roman_reverse("CDXCIX")
    assert answer == 499


def test_500():
    answer = roman_reverse("D")
    assert answer == 500


def test_999():
    answer = roman_reverse("CMXCIX")
    assert answer == 999


def test_1000():
    answer = roman_reverse("M")
    assert answer == 1000