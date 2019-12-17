def roman_convert(number_to_convert):
    all_i = "I" * number_to_convert
    all_i = all_i.replace("IIIIIIIIII", "X")
    all_i = all_i.replace("IIIIIIIII", "IX")
    all_i = all_i.replace("IIIII", "V")
    all_i = all_i.replace("IIII", "IV")
    all_i = all_i.replace("XXXXXXXXXX", "C")
    all_i = all_i.replace("XXXXXXXXX", "XC")
    all_i = all_i.replace("XXXXX", "L")
    all_i = all_i.replace("XXXX", "XL")
    all_i = all_i.replace("CCCCCCCCCC", "M")
    all_i = all_i.replace("CCCCCCCCC", "CM")
    all_i = all_i.replace("CCCCC", "D")
    all_i = all_i.replace("CCCC", "CD")

    return all_i


def roman_reverse(string_value):
    strip_to_i = string_value
    strip_to_i = strip_to_i.replace("CD", "CCCC")
    strip_to_i = strip_to_i.replace("D", "CCCCC")
    strip_to_i = strip_to_i.replace("CM", "CCCCCCCCC")
    strip_to_i = strip_to_i.replace("M", "CCCCCCCCCC")
    strip_to_i = strip_to_i.replace("XL", "XXXX")
    strip_to_i = strip_to_i.replace("L", "XXXXX")
    strip_to_i = strip_to_i.replace("XC", "XXXXXXXXX")
    strip_to_i = strip_to_i.replace("C", "XXXXXXXXXX")
    strip_to_i = strip_to_i.replace("IV", "IIII")
    strip_to_i = strip_to_i.replace("V", "IIIII")
    strip_to_i = strip_to_i.replace("IX", "IIIIIIIII")
    strip_to_i = strip_to_i.replace("X", "IIIIIIIIII")
    number_is = len(strip_to_i)
    return number_is


def roman_add(r1, r2):
    i1 = roman_reverse(r1)
    i2 = roman_reverse(r2)
    added = i1 + i2
    return roman_convert(added)
