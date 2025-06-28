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

    upper_vowels = ['A', 'E', 'I', 'O', 'U']
    return sum([1 for i in range(len(s)) if s[i] in upper_vowels and i % 2 == 0])
