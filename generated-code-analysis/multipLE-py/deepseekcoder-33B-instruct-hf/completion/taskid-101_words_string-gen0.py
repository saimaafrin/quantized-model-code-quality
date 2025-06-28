from typing import List

def words_string(s: str) -> List[str]:
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    >>> words_string('Hi, my name is John')
    ['Hi', 'my', 'name', 'is', 'John']
    >>> words_string('One, two, three, four, five, six')
    ['One', 'two', 'three', 'four', 'five', 'six']
    """

    words = s.split()
    result = []
    for word in words:
        if ',' in word:
            word = word.replace(',', '')
        result.append(word)
    return result
