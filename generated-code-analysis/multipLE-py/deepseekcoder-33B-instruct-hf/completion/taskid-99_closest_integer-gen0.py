def closest_integer(value: str) -> int:
    """
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer('10')
    10
    >>> closest_integer('15.3')
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    """


    if '.' in value:
        dot_position = value.index('.')
        int_part = value[:dot_position]
        frac_part = value[dot_position + 1:]

        if int_part[0] == '-':
            if int(frac_part[0]) >= 5:
                return int(int_part) - 1
            else:
                return int(int_part)
        else:
            if int(frac_part[0]) >= 5:
                return int(int_part) + 1
            else:
                return int(int_part)
    else:
        return int(value)
