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

    import re
    from collections import Counter

    # Split the string by whitespace to get a list of words
    words = re.split('\s', test)

    # Count the occurrences of each word using the Counter class
    counts = Counter(words)

    # Filter out the words that occur most frequently
    counts = {word: count for word, count in counts.items() if count == counts.most_common()[0][1]}

    return counts
