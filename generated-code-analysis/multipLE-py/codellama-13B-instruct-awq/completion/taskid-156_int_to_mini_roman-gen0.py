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

    if number <= 0:
        return str(number)

    # Initialize the result as an empty string
    result = ""

    # Base cases
    if number >= 1000:
        result += "m"
        number -= 1000
    if number >= 900:
        result += "cm"
        number -= 900
    if number >= 500:
        result += "d"
        number -= 500
    if number >= 400:
        result += "cd"
        number -= 400
    if number >= 100:
        result += "c"
        number -= 100
    if number >= 90:
        result += "xc"
        number -= 90
    if number >= 50:
        result += "l"
        number -= 50
    if number >= 40:
        result += "xl"
        number -= 40
    if number >= 10:
        result += "x"
        number -= 10
    if number >= 9:
        result += "ix"
        number -= 9
    if number >= 5:
        result += "v"
        number -= 5
    if number >= 4:
        result += "iv"
        number -= 4
    if number >= 1:
        result += "i"
        number -= 1

    return result
