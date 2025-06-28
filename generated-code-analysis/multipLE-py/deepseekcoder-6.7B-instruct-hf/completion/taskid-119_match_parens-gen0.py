from typing import List

def match_parens(lst: List[str]) -> str:
    """
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    >>> match_parens(['()(', ')'])
    'Yes'
    >>> match_parens([')', ')'])
    'No'
    """

    # your code here
    str1, str2 = lst[0], lst[1]
    open_count_1, open_count_2 = str1.count('('), str2.count('(')
    close_count_1, close_count_2 = str1.count(')'), str2.count(')')

    if open_count_1 < close_count_1 and open_count_2 > close_count_2:
        return 'Yes'
    elif open_count_1 > close_count_1 and open_count_2 < close_count_2:
        return 'Yes'
    elif open_count_1 == close_count_1 and open_count_2 == close_count_2:
        return 'Yes'
    else:
        return 'No'
