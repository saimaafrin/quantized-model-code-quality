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

    if not txt:
        return 0
    if not txt.split():
        if not txt.split(','):
            return 0
        else:
            return len(list(filter(lambda x: ord(x) % 2 == 1, [ord(x) for x in txt.split(',')[0]])))
    else:
        return [x for x in txt.split()]
