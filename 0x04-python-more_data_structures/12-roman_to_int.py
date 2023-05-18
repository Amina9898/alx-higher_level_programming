#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40,
    'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500,
    'CM': 900, 'M': 1000}
    summ = 0
    num = 0
    for char in reversed(roman_string):
        value = roman.get(char, 0)
        if value < num:
            summ -= value
        else:
            summ += value
        num = value
    return summ
