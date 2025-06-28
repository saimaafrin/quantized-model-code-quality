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

    number = int(number)
    if number < 1 or number > 1000:
        raise ValueError
    # Convert number to string of roman numerals
    roman_numerals = ''
    num_to_roman_char = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm',
    }
    for value in sorted(num_to_roman_char.keys()):
        while number >= value:
            roman_numerals += num_to_roman_char[value]
            number -= value
    return roman_numerals
