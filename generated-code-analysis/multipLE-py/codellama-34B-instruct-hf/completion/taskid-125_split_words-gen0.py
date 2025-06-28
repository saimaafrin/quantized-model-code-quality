from typing import Union, List

def split_words(txt: str) -> Union[List[str], int]:
    """
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    >>> split_words('Hello world!')
    ['Hello', 'world!']
    >>> split_words('Hello,world!')
    ['Hello', 'world!']
    >>> split_words('abcdef')
    3
    """


    # get a list of all the words by splitting on whitespace
    words = txt.split()

    # if the list has more than one element, return it
    if len(words) > 1:
        return words

    # get a list of all the words by splitting on commas
    words = txt.split(',')

    # if the list has more than one element, return it
    if len(words) > 1:
        return words

    # otherwise return the number of lower-case letters with odd order in the alphabet
    return sum(1 for c in txt if 'a' <= c.lower() <= 'z')
