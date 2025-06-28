def is_nested(string: str) -> bool:
    """
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    >>> is_nested('[[]]')
    True
    >>> is_nested('[]]]]]]][[[[[]')
    False
    >>> is_nested('[][]')
    False
    >>> is_nested('[]')
    False
    >>> is_nested('[[][]]')
    True
    >>> is_nested('[[]][[')
    True
    """

    count_open_brackets = 0
    count_close_brackets = 0
    flag = False
    for bracket in string:
        if bracket == '[':
            count_open_brackets += 1
        if bracket == ']':
            count_close_brackets += 1
            if count_close_brackets > count_open_brackets:
                flag = True
    if flag and count_open_brackets == count_close_brackets:
        return True
    return False
