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

    spaces = 0
    result = ''
    for letter in text:
        if letter == ' ':
            spaces += 1
            if spaces > 2:
                result += '-'
            else:
                result += '_'
        else:
            result += letter
            spaces = 0
    return result.strip('_')
