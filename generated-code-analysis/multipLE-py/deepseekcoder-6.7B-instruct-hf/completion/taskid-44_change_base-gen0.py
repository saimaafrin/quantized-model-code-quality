def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """

    assert 2 <= base <= 10, "Base must be between 2 and 10"
    if x < base:
        return str(x)
    else:
        return change_base(x // base, base) + str(x % base)
