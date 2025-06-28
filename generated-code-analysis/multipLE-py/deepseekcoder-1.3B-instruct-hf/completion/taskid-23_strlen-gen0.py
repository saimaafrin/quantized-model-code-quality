def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """

    # return len(string)
    count = 0
    for _ in string:
        count += 1
    return count
