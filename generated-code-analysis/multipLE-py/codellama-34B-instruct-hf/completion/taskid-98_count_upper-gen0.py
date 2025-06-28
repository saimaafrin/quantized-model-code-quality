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

    vowels = 'AEIOU'
    count = 0
    for index, char in enumerate(s):
        if char in vowels and index % 2 == 0:
            count += 1
    return count
