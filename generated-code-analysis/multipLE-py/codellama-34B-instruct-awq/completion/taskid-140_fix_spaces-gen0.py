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

    if len(text) > 1:
        if text.count(" ") == 1:
            text = text.replace(" ", "_")
        elif text.count(" ") >= 2:
            text = text.replace("  ", "-", 1)
            text = text.replace(" ", "_")
    return text
