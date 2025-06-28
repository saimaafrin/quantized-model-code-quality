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


    if not 1 <= number <= 1000:
        raise ValueError('The value of the given argument must be between 1 and 1000')

    result = ""
    for char, value in ROMAN_NUMERALS_MAP.items():
        while number >= value:
            result += char
            number -= value

    return result
