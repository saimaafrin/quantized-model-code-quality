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

    if len(lst[0]) + len(lst[1]) == 1:
        return 'No'

    count1 = 0
    count2 = 0
    for i in range(len(lst[0])):
        if lst[0][i] == '(':
            count1 += 1
        else:
            count1 -= 1
        if count1 < 0:
            return 'No'
    for i in range(len(lst[1])):
        if lst[1][i] == '(':
            count2 += 1
        else:
            count2 -= 1
        if count2 < 0:
            return 'No'
    if count1 + count2 == 0:
        return 'Yes'
    return 'No'
