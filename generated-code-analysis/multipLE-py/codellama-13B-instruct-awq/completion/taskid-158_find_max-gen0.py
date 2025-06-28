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

    # Find the word with maximum unique characters
    unique_chars = 0
    selected_word = ''
    for word in words:
        word_set = set(word)
        if len(word_set) > unique_chars:
            unique_chars = len(word_set)
            selected_word = word
        elif len(word_set) == unique_chars:
            if word < selected_word:
                selected_word = word
    return selected_word
