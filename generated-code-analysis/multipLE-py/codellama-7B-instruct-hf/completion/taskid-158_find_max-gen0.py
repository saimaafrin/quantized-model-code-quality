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

    # Your code here
    if not words:
        return ""

    count_map = {}
    for word in words:
        for letter in word:
            if letter not in count_map:
                count_map[letter] = 1
            else:
                count_map[letter] += 1
    max_unique_chars = 0
    max_unique_word = ""
    for word in words:
        unique_chars = 0
        for letter in word:
            if letter not in count_map:
                continue
            if count_map[letter] > 1:
                unique_chars += 1
        if unique_chars > max_unique_chars or \
                (unique_chars == max_unique_chars and word < max_unique_word):
            max_unique_chars = unique_chars
            max_unique_word = word
    return max_unique_word
