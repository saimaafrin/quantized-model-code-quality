def count_upper(s: str) -> int:
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    >>> count_upper('aBCdEf')
    1
    >>> count_upper('abcdefg')
    0
    >>> count_upper('dBBE')
    0
    """

    # define the set of uppercase vowels
    upper_vowels = {'A', 'E', 'I', 'O', 'U'}
    # split the string into individual characters
    chars = list(s)
    # use list comprehension to count the number of uppercase vowels at even indices
    count = sum(1 for i in range(len(chars)) if chars[i] in upper_vowels and i % 2 == 0)
    return count
