from typing import Dict

def histogram(test: str) -> Dict[str, int]:
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    >>> histogram('a b c')
    { 'a': 1, 'b': 1, 'c': 1 }
    >>> histogram('a b b a')
    { 'a': 2, 'b': 2 }
    >>> histogram('a b c a b')
    { 'a': 2, 'b': 2 }
    >>> histogram('b b b b a')
    { 'b': 4 }
    >>> histogram('')
    {  }

    """

    # Split the string by spaces, make it lowercase and create a histogram
    histo = {}
    for letter in test.lower().split():
        if letter in histo:
            histo[letter] += 1
        else:
            histo[letter] = 1
    # find the max count
    max_count = max(histo.values())
    # create a new histogram with only the letters with the max count
    return {k: v for k, v in histo.items() if v == max_count}
