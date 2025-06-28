from typing import List

def find_max(words: List[str]) -> str:
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    >>> find_max(['name', 'of', 'string'])
    'string'
    >>> find_max(['name', 'enam', 'game'])
    'enam'
    >>> find_max(['aaaaaaa', 'bb', 'cc'])
    'aaaaaaa'
    """

    unique_chars = []
    for word in words:
        unique_chars.append(len(set(word)))
    max_unique = max(unique_chars)
    result = []
    for i, word in enumerate(words):
        if unique_chars[i] == max_unique:
            result.append(word)
    result.sort()
    return result[-1]
