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

    if base <= 0:
        raise ValueError("base has to be positive.")
    # if base > 9:
    #     raise NotImplementedError("base has to be less than 10.")

    if x < 0:
        is_negative = True
    else:
        is_negative = False

    if is_negative:
        x *= -1
    str_x = str(x)

    # convert the number to a string
    result = ""
    while x > 0:
        x, rem = divmod(x, base)
        result = str(rem) + result
    # add zeroes to the left of the string
    result = (len(str_x) - len(result)) * "0" + result
    if is_negative:
        result = "-" + result
    return result
