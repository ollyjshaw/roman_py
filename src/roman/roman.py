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
