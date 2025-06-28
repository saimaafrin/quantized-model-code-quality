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


    # first concat the strings in every possible way
    # then for each string check if it is good
    # if any string is good return 'Yes'
    # else return 'No'

    def is_good(s: str) -> bool:
        """
        Returns True if the given string is good.
        """
        # TODO: implement your solution here
        # hint: you may find it useful to use a stack to keep track of the
        # balance of parentheses.
        # hint2: you may find it useful to use the count method to check how many
        # open/close parentheses there are in the string.
        # hint3: think about how you can use the information from hint2 to
        # determine if a string is good or not.
        return False

    def concatenate_strings(a: str, b: str) -> str:
        """
        Returns the concatenation of the two given strings.
        """
        return a + b

    # main
    concatenated_strings: List[str] = [concatenate_strings(a, b) for a in lst for b in lst]
    good_strings: List[str] = [s for s in concatenated_strings if is_good(s)]
    if good_strings:
        return 'Yes'
    else:
        return 'No'
