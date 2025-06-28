def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    # I want to avoid using the `set` and `len` built-in functions,
    # so I'll write the implementation here by hand
    # to better understand how the problem can be solved
    # https://stackoverflow.com/a/1233202/938111
    # 1. Convert input string to list of chars
    chars: list = list(string.lower())
    # 2. Sort the list of chars
    chars.sort()
    # 3. Find the first different element
    # and count how many different elements are there
    counter = 0
    last = None
    for x in chars:
        if last != x:
            last = x
            counter += 1
    # 4. Return the counter
    return counter
