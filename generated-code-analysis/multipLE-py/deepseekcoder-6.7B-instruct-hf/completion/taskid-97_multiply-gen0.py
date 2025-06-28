def multiply(a: int, b: int) -> int:
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    >>> multiply(148, 412)
    16
    >>> multiply(19, 28)
    72
    >>> multiply(2020, 1851)
    0
    >>> multiply(14, -15)
    20
    """

    # getting last digit of the numbers
    last_digit_a = abs(a) % 10
    last_digit_b = abs(b) % 10
    # returning their multiplication
    return last_digit_a * last_digit_b
