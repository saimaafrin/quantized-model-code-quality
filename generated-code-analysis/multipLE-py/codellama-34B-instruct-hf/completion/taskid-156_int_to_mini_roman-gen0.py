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

    ROMAN_NUMERAL_MAP = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm'
    }
    result = ''
    for i, numeral in enumerate(ROMAN_NUMERAL_MAP):
        while number % numeral < number:
            result += ROMAN_NUMERAL_MAP[numeral]
            number -= numeral
        if number in ROMAN_NUMERAL_MAP:
            result += ROMAN_NUMERAL_MAP[number]
            number = 0
        if number == 0:
            break
    return result
