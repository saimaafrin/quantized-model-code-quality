def circular_shift(x: int, shift: int) -> str:
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    '21'
    >>> circular_shift(12, 2)
    '12'
    """

    num_digits = len(str(x))
    shifted = x % 10**num_digits + x // 10**num_digits
    shifted %= 10**num_digits
    if shifted > num_digits:
        shifted -= 10**num_digits
    return str(shifted)
