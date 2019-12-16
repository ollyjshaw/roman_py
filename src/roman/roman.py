def roman_convert(number_to_convert):
    all_i = "I" * number_to_convert
    all_i = all_i.replace("IIIIIIIII", "IX")
    all_i = all_i.replace("IIIII", "V")
    all_i = all_i.replace("IIII", "IV")
    return all_i
