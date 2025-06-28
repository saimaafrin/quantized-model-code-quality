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

    max_count = 0
    max_string = ""
    for word in words:
        if len(set(word)) > max_count:
            max_count = len(set(word))
            max_string = word
        elif len(set(word)) == max_count and word < max_string:
            max_string = word

    return max_string
