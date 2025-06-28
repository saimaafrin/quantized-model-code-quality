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

    counter = 0
    if len(string) < 2:
        return False

    for i in range(len(string)):
        if string[i] == '[':
            counter += 1
            if counter > 1:
                return True
        else:
            counter -= 1
            if counter == 0:
                return False
    return False
