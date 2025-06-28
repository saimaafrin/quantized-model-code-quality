def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    count = 0
    step = 0
    while step < len(string) - len(substring) + 1:
        if string[step:step+len(substring)] == substring:
            count += 1
        step += 1
    return count
