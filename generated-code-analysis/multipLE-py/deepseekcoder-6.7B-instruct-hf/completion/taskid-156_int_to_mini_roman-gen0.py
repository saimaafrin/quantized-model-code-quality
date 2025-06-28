def int_to_mini_roman(number: int) -> str:
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19)
    'xix'
    >>> int_to_mini_roman(152)
    'clii'
    >>> int_to_mini_roman(426)
    'cdxxvi'
    """

    # Mapping from integer to roman numeral
    roman_numerals = {
        1: 'i',
        4: 'iv',
        5: 'v',
        9: 'ix',
        10: 'x',
        40: 'xl',
        50: 'l',
        90: 'xc',
        100: 'c',
        400: 'cd',
        500: 'd',
        900: 'cm',
        1000: 'm'
    }

    # Sorting the keys in descending order
    keys = sorted(roman_numerals.keys(), reverse=True)

    # Initializing result
    result = ''

    # For each key in the sorted list of keys
    for key in keys:
        # While the number is greater than or equal to the key
        while number >= key:
            # Append the corresponding roman numeral to the result
            result += roman_numerals[key]
            # Subtract the key from the number
            number -= key
    # Return the result
    return result
