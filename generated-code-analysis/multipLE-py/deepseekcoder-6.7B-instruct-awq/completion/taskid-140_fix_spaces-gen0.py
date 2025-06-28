def fix_spaces(text: str) -> str:
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    >>> fix_spaces(' Example')
    'Example'
    >>> fix_spaces(' Example 1')
    'Example_1'
    >>> fix_spaces(' Example 2')
    '_Example_2'
    >>> fix_spaces(' Example 3')
    '_Example-3'
    """

    res = ''
    cnt = 0
    for i in text:
        if i == ' ':
            cnt += 1
            if cnt <= 2:
                res += '_'
        else:
            if cnt > 2:
                res += '-'
            res += i
            cnt = 0
    return res.lstrip('_')
