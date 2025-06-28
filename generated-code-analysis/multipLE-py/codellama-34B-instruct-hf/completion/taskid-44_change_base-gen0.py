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

    num_list = []
    while x > 0:
        num_list.append(x % base)
        x = x // base
    return ''.join(str(i) for i in num_list[::-1])
